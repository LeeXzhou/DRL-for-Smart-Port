import logging

from rich.logging import RichHandler

__all__ = ["log"]


FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("DRL4SmartPort")
