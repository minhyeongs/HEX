import discord
import os
import random

# 인텐트 설정
intents = discord.Intents.all()
intents.messages = True  # 메시지 이벤트에 대한 인텐트 설정

# 디스코드 클라이언트 생성
client = discord.Client(intents=intents)

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# 봇이 메시지를 받았을 때 동작되는 코드
@client.event
async def on_message(message):
    # 봇이 보낸 메시지는 무시
    if message.author == client.user:
        return

    # 특정 단어가 포함되어 있을 때 랜덤으로 반응
    if '헥스야' in message.content:
        responses = ['Yes, my kitten?', '포옹<3', 'Hi, my Love Anna', "Remember that. i am your daddy."]
        response = random.choice(responses)
        await message.channel.send(response)

# 디스코드 봇 실행
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
