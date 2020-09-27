import discord
from discord.ext import commands
import asyncio
import datetime
bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

token = "NzE1MTcxOTA4NTg0MjEwNDcy.Xu4HEA.lSBu-rUFISyud2jdKoqGLLF2hO8"

@bot.command()
async def 공지(ctx,*,noticemessage):

    if ctx.author.id == 756045138542723082:

        from datetime import datetime

        now = datetime.now()
        time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name=":loudspeaker: Every Bot 공지", value="""{}

                                   """.format(noticemessage), inline=False)
        embed.add_field(name="봇 지원", value='\n'+'💌[koreanbots.dev](https://koreanbots.dev/bots/715171908584210472)\n 💌[top.gg](https://top.gg/bot/715171908584210472)\n 💌[Every Bot 초대링크](<https://discord.com/oauth2/authorize?client_id=715171908584210472&permissions=8&scope=bot>)\n 💌[Every Discord 지원](<https://discord.gg/pcEdgeh>)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/758976004646895616/758999798619176970/thumb_l_3EBC7E3D6D66FE217595432387EA4057.jpg")
        embed.set_footer(text=f"공지 전송자:  {ctx.author.name}  - 인증됨 {time}", icon_url=ctx.author.avatar_url)
    
        for guild in bot.guilds:
                senddone = False
                for channel in guild.text_channels:
                    try:
                        await channel.send(embed=embed)
                        print(f'공지성공! {guild} 서버의 {channel} 채널에 공지 발송!')
                        senddone = True
                        break
                    except:
                        print(f'{guild} 서버의 {channel} 채널에 공지 발송 실패... 다른 채널에 시도...')
                        pass
                if not senddone:
                    print(f'{guild} 서버에는 공지를 보낼수 있는곳이 없어.... 건너뛸게...')


bot.run(token)