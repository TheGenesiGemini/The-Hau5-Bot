import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from colorama import init, Fore, Style
from datetime import datetime

# Inicializar colorama
init()

# Crear directorio de logs si no existe
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

class ColoredFormatter(logging.Formatter):
    """Formateador de logs con colores para consola"""
    
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
    }
    
    def format(self, record):
        log_message = super().format(record)
        return f"{self.COLORS.get(record.levelname, '')}{log_message}{Style.RESET_ALL}"

class BotLogger:
    """Clase mejorada para manejar el logging del bot con rotación de archivos"""
    
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Nivel más bajo para capturar todo
        
        # Evitar propagación al logger raíz
        self.logger.propagate = False
        
        # Configurar handlers si no existen
        if not self.logger.handlers:
            # Configurar handler para consola
            self._setup_console_handler()
            
            # Configurar handler para archivo con rotación
            self._setup_file_handler()
    
    def _setup_console_handler(self):
        """Configurar el handler para la consola con colores"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)  # Solo INFO y superiores a consola
        
        formatter = ColoredFormatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def _setup_file_handler(self):
        """Configurar el handler para archivo con rotación"""
        log_file = LOG_DIR / 'binance_redpacket.log'
        
        # Rotación: 5 archivos de 5MB cada uno
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=5*1024*1024,  # 5MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)  # Capturar todo a archivo
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def _log_with_context(self, level: str, message: str, **context):
        """Método base para logging con contexto adicional"""
        extra = {k: v for k, v in context.items() if v is not None}
        if extra:
            context_str = ' | '.join(f'{k}={v}' for k, v in extra.items())
            message = f"{message} | {context_str}"
        self.logger.log(level, message)
    
    def info(self, message: str, **context):
        self._log_with_context(logging.INFO, message, **context)
    
    def warning(self, message: str, **context):
        self._log_with_context(logging.WARNING, message, **context)
    
    def error(self, message: str, **context):
        self._log_with_context(logging.ERROR, message, **context)
    
    def debug(self, message: str, **context):
        self._log_with_context(logging.DEBUG, message, **context)
    
    def success(self, code: str, amount: float, currency: str, **context):
        """Registra un canje exitoso con contexto adicional"""
        message = f"✅ CANJE EXITOSO - Código: {code} - {amount} {currency}"
        self.info(message, code=code, amount=amount, currency=currency, **context)
    
    def duplicate(self, code: str, **context):
        """Registra un código duplicado"""
        message = f"⚠️  CÓDIGO DUPLICADO - {code} ya fue procesado anteriormente"
        self.warning(message, code=code, **context)
    
    def invalid(self, code: str, reason: str, **context):
        """Registra un código inválido con la razón"""
        message = f"❌ CÓDIGO INVÁLIDO - {code}: {reason}"
        self.error(message, code=code, reason=reason, **context)
    
    def processing(self, code: str, **context):
        """Registra el inicio del procesamiento de un código"""
        message = f"🔄 PROCESANDO - Código: {code}"
        self.info(message, code=code, **context)
    
    def api_error(self, code: str, status_code: int = None, response: str = None, **context):
        """Registra un error de la API con detalles"""
        message = f"❌ ERROR DE API - Código: {code}"
        if status_code:
            message += f" | Status: {status_code}"
        self.error(message, code=code, status_code=status_code, response=response, **context)

# Instancia global del logger
logger = BotLogger("BinanceRedPacket")

# Ejemplo de uso:
if __name__ == "__main__":
    logger.info("Iniciando aplicación")
    logger.success("ABC123", 0.001, "BTC", wallet="mi_wallet")
    logger.duplicate("ABC123", source="telegram")
    logger.invalid("INVALID123", "Formato incorrecto")
    logger.api_error("XYZ789", 429, "Rate limit exceeded")
