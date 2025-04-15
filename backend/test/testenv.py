import os
import logging as log

from backend.utils.log_config import init_log_config
if __name__ == "__main__":
    init_log_config()
    print(os.environ.get("DS_ALI_API_KEY"))
    log.warning("hello")
    log.info("world")