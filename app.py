import uvicorn
import os

from backend.utils.log_config import init_log_config

if __name__ == "__main__":
    init_log_config()
    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=["backend"],  # 只监视 backend 目录
        reload_excludes=["node_modules", "uploads"]  # 排除这些目录
    ) 