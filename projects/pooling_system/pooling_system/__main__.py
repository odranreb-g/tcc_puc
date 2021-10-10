import logging
import sys
import sentry_sdk
from pooling import PoolingExecuter

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
root.addHandler(handler)
logger = logging.getLogger(__name__)


sentry_sdk.init(
    "https://e1fc87c1991d412aad19dc812385c9a1@o89421.ingest.sentry.io/6000492",
    traces_sample_rate=1.0,
)

if __name__ == "__main__":
    pooling = PoolingExecuter()
    pooling.process()
