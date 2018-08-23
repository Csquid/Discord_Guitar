import discord
import asyncio
import datetime
# import requests
# from bs4 import BeautifulSoup as bs

client = discord.Client()

def time():
    day = datetime.datetime.now()
    print(day.strftime("%Y-%m-%d %H:%M:%S"), end=" ")

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    await client.change_presence(game=discord.Game(name='윈치는 바보다'))


# @client.event
# async def on_member_join(member):
#     fmt = '{1.name} 에 오신걸을 환영합니다., {0.mention} 님'
#     channel = member.server.get_channel("channel_id_here")
#     await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_message(message):
    time()


    # discord user profile photo url
    # if(message.author.avatar_url != ""):
    #     print(message.author.avatar_url)

    print("Channel: %s(%s) | Author: %s(#%s) | Message: %s" % (
        message.channel, message.channel.id[:5],
        message.author.name, message.author.id[:5],
        message.content
    ))

    id = message.author.name
    a = ["```md\n#  스팀구매계정```\n```fix\n-  0시간 케릭 미생성 계정```\n```css\n+  1인 1일 3개까지만 판매 합니다.13.000 [고정가]-        ```\n```diff\n-  문화상품권은 거래하지 않습니다.\n\n\n+  계정에 배그를 구매해드리진 않습니다. ```\n\n"]
    b = ["-   **아이디** **비밀번호** **이메일** **이메일비밀번호**  순서로 드리고있습니다."]
    str = a[0] + b[0]


    if message.content.startswith('!ping'):
        await client.send_message(message.channel, "!pong")

    elif message.content.startswith('!hi'):
        await client.send_message(message.channel, "!bye")

    elif message.content.startswith('윈치는 뭐다?'):
        embed=discord.Embed(title="윈치", description="그는 좆치다.", color=0x05e1ff)
        await client.send_message(message.channel, embed=embed);

    elif message.content.startswith('찬이는 뭐다?'):
        embed=discord.Embed(title="Chan", description="프로그래밍은 못하지만 가오는 오진다.", color=0xff0909)
        await client.send_message(message.channel, embed=embed);

    elif message.content.startswith('Bot Byung Shin'):
        await client.send_message(message.channel, "한국어 써라 이년아")

    elif message.content.startswith('망고님'):
        await client.send_message(message.channel, "네?")

    elif message.content.startswith('메모리 주세요'):
        await client.send_message(message.channel, "ㅇㅋㅇㅋ 갠메 ㄱㄱ")

    elif message.content.startswith('공지'):
        embed=discord.Embed(title="STEAM 계정", description=str, color=0x399fa4, thumbnail=100)
        await client.send_message(message.channel, embed=embed);

        # elif "!사진검색" == message.content.split(" ")[0]:
        #         group = message.content.split(" ")[1]
        #
        #         google_data = requests.get("https://www.google.com/search?q="+group+"&source=lnms&tbm=isch&sa=X")
        #         soup = bs(google_data.text, "html.parser")
        #         imgs = soup.find_all("img")
        #
        #         i = 0
        #         while i < 10:
        #             await client.send_message(message.channel, imgs[i]['src'])
        #             i = i + 1
        #
        #         del group, google_data, soup, imgs

    # else:
    #     await client.send_message(message.channel, "permission Error [권한이 없습니다]")
    # elif "!음악검색" == message.content.split(" ")[0]:
    #         group = message.content.split(" "[1])
    #
    #         youtube_data = requests.get("https://www.youtube.com/results?search_query=" + group)
    #         soup = bs(youtube_data.text, "html.parser")

client.run('NDgxMDQzMzg5NTM0NTY4NDY3.DlwxcA.XXLZUNnUh5Pzh6eBkeq38xGmrs0')
