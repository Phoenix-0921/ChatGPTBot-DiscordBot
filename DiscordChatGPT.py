import os
import discord
from discord.ext import commands
import openai

# 设置你的 Discord 机器人的令牌
token = os.getenv('DISCORD_TOKEN')

# 设置你的 ChatGPT API Token
openai.api_key = os.getenv('OPENAI_API')

# intents是要求機器人的權限
intents = discord.Intents.all()
# 创建 Discord 客户端
bot = commands.Bot(command_prefix='/',intents = intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
@bot.command()
async def ask(ctx, *, question):
    if question:
        # 使用 ChatGPT 进行对话
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # 使用 ChatGPT 引擎
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
                ],
        max_tokens=150  # 根據需要調整
        )

        answer = response.choices[0].message.content

        # 将 ChatGPT 的回答发送回 Discord
        await ctx.send(answer)
    else:
        await ctx.send("请提供问题")

bot.run(token)
