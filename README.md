# xiaozhi_independent_demo
实现分离小智的对话逻辑

# 智能语音交互系统

## 功能特性
- 实时语音识别(ASR) 
- 文本到语音合成(TTS)
- 意图识别
- RESTful API服务

## 快速开始
git clone https://github.com/delusion22/xiaozhi_independent_demo.git

# 本地运行
pip install -r voice-core/requirements.txt
python voice-core/api/main.py
```

## 模型部署
1. 下载SenseVoiceSmall模型：
```bash
mkdir -p models/
wget https://your-model-host/SenseVoiceSmall.zip -P models/
unzip models/SenseVoiceSmall.zip
```

## API文档
`POST /ask`
- 输入：audio/text(可选)
- 输出：audio/text（可选）

## 项目结构
```
voice-core/
├── src/              # 核心模块
│   ├── asr/          # 语音识别
|   ├── intent/       # 意图识别
|   ├── llm/          # 模型实现
│   └── tts/          # 语音合成
├── api/              # fast接口文件
├── models/           # 模型文件
├── app_configs/      # 配置文件
└── requirements.txt  # 依赖清单
```

## 健康检查
```bash
curl http://localhost:8001/api/debug
```

## 许可证
Apache 2.0
