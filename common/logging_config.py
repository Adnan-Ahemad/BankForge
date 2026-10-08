"""Logging setup for BankForge services."""

from __future__ import annotations

import logging
from logging.config import dictConfig


def configure_logging(name: str = "bankforge") -> logging.Logger:
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
            }
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "formatter": "standard",
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            name: {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False,
            }
        },
    })
    return logging.getLogger(name)
