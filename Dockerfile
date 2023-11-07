FROM python:3.9

# 設置工作目錄
WORKDIR /DiscordBot

# 複製應用程式程式碼到容器中
COPY . /DiscordBot

# 安裝應用程式的依賴
RUN pip install -r requirements.txt

# 指定應用程式的入口命令
CMD ["python", "DiscordChatGPT.py"]
