import logging

def init_log_config():
    # 设置日志级别为 INFO（INFO 及以上级别都会输出）
    logging.basicConfig(level=logging.INFO)

    logging.debug("调试信息")  # 不会输出（低于 INFO）
    logging.info("普通信息")   # 输出
    logging.warning("警告信息")  # 输出