FROM python:3.10

# 安装系统依赖
RUN apk add --no-cache \
    ffmpeg \
    opus-tools \
    sox \
    alsa-lib

# 设置工作目录
WORKDIR /app

# 安装Python依赖
COPY voice-core/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY voice-core/src ./src
COPY voice-core/config ./config
COPY voice-core/demo.py .

# 复制预训练模型
COPY models/SenseVoiceSmall /app/models/SenseVoiceSmall

# 设置环境变量
ENV PYTHONPATH=/app

# 启动命令
CMD ["python", "demo.py"]