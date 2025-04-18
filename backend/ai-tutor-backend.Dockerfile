# 使用官方Python基础镜像
FROM python:3.10.12-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY ./app.py ./config.py ./main.py ./models.py ./
COPY ./utils/ ./utils/
COPY ./services/ ./services/


# 暴露端口
EXPOSE 8000

RUN mkdir -p /var/log && \
    touch /var/log/app.log && \
    chmod 777 /var/log/app.log

# 启动命令（生产环境不要使用--reload）
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8000"]