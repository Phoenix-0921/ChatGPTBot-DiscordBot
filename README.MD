編寫Discord GPT機器人
所需要下載模組
pip install discord.py
pip install dotenv
pip install openai

DiscordChatGPT.py已完成
從.env.example 填入
Discord機器人Token以及ChatGPT的API 即可執行開始使用

/ask (想問的問題) 機器人就會回答

PS.ChatGPT 關於 python opai 模組只支援到0.27 
   目前最新版本為1.1.1 

提問語法已從
openai.Completion.create
改成
openai.chat.completions.create
