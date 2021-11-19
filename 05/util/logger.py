import logging
import sys

LOG_FORMAT = "%(asctime)s -%(levelname)s - %(message)s"
logging.basicConfig(
    filename="labor-market.log",
    filemode="w",
    format = LOG_FORMAT,
    level=logging.DEBUG
)

LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(sys.stdout))
