import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    filename="logs.log", filemode="w"
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)