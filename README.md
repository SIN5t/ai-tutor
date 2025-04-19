# ai-tutor:AI助教

# 后端环境配置
1. cd backend
2. python -m vevn .venv
3. source .venv/bin/active
4. pip install -r requirements.txt

- 配置相关
cd config
cp config.template.py config.py

修改APIKEY，模型调用地址等信息
whisper替换为本地下载模型：
``` "whisper_model": "/home/ubuntu/software/py/ai-tutor/faster-whisper-tiny",  # 可选值: tiny, base, small, medium, large```

- 运行：python app.py

# 前端
下载nodejs依赖
检测依赖：
``` 
node -v
npm -v 
```

安装环境依赖：
npm install

开启项目
npm start



声明：项目修改自VideoChat，如有侵权，联系删除