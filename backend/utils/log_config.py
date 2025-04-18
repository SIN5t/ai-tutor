import logging
import os
from logging.handlers import RotatingFileHandler

def init_log_config():
    """初始化日志配置"""
    # 确保日志目录存在
    log_dir = "/var/log"
    os.makedirs(log_dir, exist_ok=True)
    
    # 主日志配置
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),  # 控制台输出
            RotatingFileHandler(
                filename=f'{log_dir}/app.log',
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=5
            )
        ]
    )
    
    # 特别设置某些库的日志级别
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('uvicorn').setLevel(logging.INFO)