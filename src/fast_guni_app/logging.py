import logging.config

from gunicorn import glogging

LOG_CONFIG_DICT = {
    "version": 1,
    "formatters": {
        "standard": {"format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"}
    },
    "disable_existing_loggers": False,
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "INFO"},
        "fast_guni_app": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "gunicorn.error": {"handlers": ["default"], "level": "INFO"},
        "gunicorn.access": {"handlers": ["default"], "level": "INFO"},
    },
}


class UnifiedLogger(glogging.Logger):
    def setup(self, cfg):
        """Configure Gunicorn application logging configuration."""
        super().setup(cfg)
        logging.config.dictConfig(LOG_CONFIG_DICT)
