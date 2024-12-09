import logging
from logging.config import dictConfig

def setup_logging():
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "app.log",
                "formatter": "detailed",
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        },
    }
    dictConfig(logging_config)

# 전역 logger 객체 생성
logger = logging.getLogger("app")