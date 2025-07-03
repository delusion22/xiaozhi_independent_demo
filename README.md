# xiaozhi_independent_demo
实现分离小智的对话逻辑

# 智能语音交互系统

## 功能特性
- 实时语音识别(ASR) 
- 文本到语音合成(TTS)
- 多模态对话管理
- RESTful API服务

## 快速开始
```bash
# 克隆仓库
git clone https://github.com/yourusername/xiaozhi-esp32-server
cd xiaozhi-esp32-server/main/xiaozhi-server/independent_demo



# 本地运行
pip install -r voice-core/requirements.txt
PYTHONPATH=$PWD python voice-core/demo.py
```

## 模型部署
1. 下载SenseVoiceSmall模型：
```bash
mkdir -p models/
wget https://your-model-host/SenseVoiceSmall.zip -P models/
unzip models/SenseVoiceSmall.zip
```

## API文档
`POST /api/v1/transcribe`
- 输入：audio/wav格式语音文件
- 输出：JSON格式文本结果

## 项目结构
```
voice-core/
├── src/              # 核心模块
│   ├── asr/          # 语音识别
│   └── tts/          # 语音合成
├── config/           # 配置文件
├── models/           # 模型文件
└── requirements.txt  # 依赖清单
```

## 健康检查
```bash
curl http://localhost:8000/health
```

## 许可证
Apache 2.0
