import asyncio
import httpx
import random
from datetime import datetime, timedelta
from typing import Literal, Dict, Optional

from core.binance.api import BinanceAPI
from core.logger import logger


class RedpacketHandler:
    TYPES = Literal[
        "processed", "claimed", "captcha", "too_many_requests", "session_expired"
    ]

    def __init__(self) -> None:
        self.processed_codes: Dict[str, dict] = {}  # Almacena códigos y su estado
        self.stats = {
            'total_processed': 0,
            'successful': 0,
            'failed': 0,
            'invalid': 0,
            'total_amount': 0.0,
            'currency': 'USDT'
        }
        self.last_successful_claim = None
        self.retry_attempts = 1  # Solo un intento por código

    async def handle_response(self, response: httpx.Response) -> TYPES:
        """
        Handle the response codes/messages/data an return the according type.

        :response: httpx.Response
        :return: Literal[...]
        """
        response_json = response.json()
        data = response_json.get("data", None)
        code = response_json.get("code", None)

        if response_json["success"]:
            currency = response_json["data"]["currency"]
            amount = response_json["data"]["grabAmountStr"]
            print(f"[ CLAIMED ] {amount} {currency}")
            return "claimed"

        elif data and "validateId" in data:
            print(f"[ WARNING ] Captcha detected: sleeping for 1 hour.")
            return "captcha"

        elif code not in [
            "100002001",
            "403067",
            "403802",
            "403803",
            "PAY4001COM000",
        ]:
            print(f"[ ERROR] An unexpected return type: {response_json}")
            return "processed"

        match code:
            case "100002001":
                print(
                    "Session expired, please re-enter new credentials in core/config.py"
                )
                return "session_expired"
            case "403067":
                print("Too many requests: sleeping for 1 hour")
                return "too_many_requests"
            case "403802":
                print("Redpacket is already fully-claimed.")
                return "processed"
            case "403803":
                print("Invalid repacket code entered.")
                return "processed"
            case "PAY4001COM000":
                print("Invalid repacket code entered.")
                return "processed"

    def show_stats(self) -> None:
        """Muestra estadísticas de los canjes"""
        stats = self.stats
        logger.info("\n" + "="*50)
        logger.info("📊 ESTADÍSTICAS DE CANJES")
        logger.info("="*50)
        logger.info(f"✅ Canjes exitosos: {stats['successful']}")
        logger.info(f"❌ Fallidos: {stats['failed']}")
        logger.info(f"🚫 Inválidos: {stats['invalid']}")
        logger.info(f"💰 Total canjeado: {stats['total_amount']:.8f} {stats['currency']}".rstrip('0').rstrip('.'))
        if self.last_successful_claim:
            last_claim = (datetime.now() - self.last_successful_claim).total_seconds()
            logger.info(f"⏱  Último canje exitoso: {int(last_claim//60)} minutos y {int(last_claim%60)} segundos atrás")
        logger.info("="*50 + "\n")

    async def handle_codes(self, code: str) -> None:
        """Manejo ultra rápido de códigos"""
        if code in self.processed_codes:
            return
            
        self.processed_codes[code] = True
        
        try:
            # Intento directo sin esperar confirmación
            response = await BinanceAPI().request_redpacket(code)
            response_json = response.json()
            
            if response_json.get('success', False):
                data = response_json['data']
                amount = data['grabAmountStr'].split()[0]  # Mantener como string para evitar redondeo
                currency = data['currency']
                print(f"[+] {code} - {amount} {currency}")
                self.stats['successful'] += 1
                try:
                    self.stats['total_amount'] += float(amount)
                except:
                    pass
                self.stats['currency'] = currency
            else:
                print(f"[-] {code} - INVÁLIDO")
            
        except Exception:
            pass  # Ignorar errores para máxima velocidad
