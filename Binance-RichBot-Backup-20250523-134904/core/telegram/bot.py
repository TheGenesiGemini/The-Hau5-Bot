import asyncio
import random
from typing import List, Set
from telethon import TelegramClient, events

from core.config import config
from core.binance.redpacket import RedpacketHandler


class CodeProcessor:
    def __init__(self, handler):
        self.handler = handler
        self.processed_codes: Set[str] = set()
        print("🚀 Procesador de códigos iniciado (modo instantáneo)")
        
    async def add_code(self, code: str):
        if code in self.processed_codes:
            print(f"⏭️ Código ya procesado: {code}")
            return
            
        print(f"⚡ Procesando código: {code}")
        self.processed_codes.add(code)
        try:
            await self.handler.handle_codes(code)
        except Exception as e:
            print(f"❌ Error procesando código {code}: {e}")


class BaseClient:
    def __init__(self):
        self.CLIENT: TelegramClient = TelegramClient(
            config.CLIENT_NAME, config.API_ID, config.API_HASH
        )
        self.HANDLER = RedpacketHandler()
        self.processor = CodeProcessor(self.HANDLER)
        self.setup_event_handler()

    def setup_event_handler(self) -> None:
        @self.CLIENT.on(events.NewMessage())
        async def _(event: events.NewMessage.Event):
            try:
                # Obtener el texto del mensaje
                message_text = event.message.text or event.message.message
                if not message_text:
                    return
                
                # Búsqueda rápida de códigos de 8-11 caracteres alfanuméricos
                import re
                
                # Buscar códigos de 8 caracteres alfanuméricos en mayúsculas
                # que tengan al menos un número y una letra
                codes = re.findall(r'\b([A-Z0-9]{8})\b', message_text.upper())
                # Filtrar para asegurar que tenga al menos un número y una letra
                valid_codes = []
                seen = set()
                for code in codes:
                    if code not in seen and any(c.isalpha() for c in code) and any(c.isdigit() for c in code):
                        valid_codes.append(code)
                        seen.add(code)
                
                if valid_codes:
                    print(f"\n=== Nuevo mensaje en el chat {event.chat_id} ===")
                    print(f"Códigos válidos encontrados: {', '.join(valid_codes)}")
                    
                    # Procesar códigos inmediatamente
                    for code in valid_codes:
                        await self.processor.add_code(code)
                else:
                    print("No se encontraron códigos válidos en este mensaje.")
                            
            except Exception as e:
                print(f"\n[ERROR CRÍTICO] Error al procesar el mensaje: {str(e)}")

    def start(self)-> None:
        print("Starting the proccesses...")
        self.CLIENT.start()
        print("Telethon started, waiting for messages")
        self.CLIENT.run_until_disconnected()
