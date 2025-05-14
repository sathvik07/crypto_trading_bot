import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("TradingBotLogger")
logger.setLevel(logging.DEBUG)

rotating_handler = RotatingFileHandler("bot.log", maxBytes=1000000, backupCount=3)
rotating_handler.setLevel(logging.DEBUG)

error_handler = logging.FileHandler("error.log")
error_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
rotating_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(rotating_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)
