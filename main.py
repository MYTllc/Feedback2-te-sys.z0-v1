import discord
from discord.ext import commands
import asyncio
import time
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('#'), intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Dev : Its.Zoro $", url="https://www.twitch.tv/tee"))
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id} Dev : Its.Zoro $')
    print(f'Bot ID : {bot.user.id} , All commands Loaded!!')


@bot.event
async def on_message(message):
  if message.author == bot.user or message.author.bot:
        return
  if message.content.startswith('اينماا') and str(message.author.id) == '747128911942385855':
        args = message.content[6:].strip().split(' ')
        user = message.mentions[0] if message.mentions else await bot.fetch_user(args[0])

        if not user:
            await message.reply('يرجى ذكر عضو صحيح.')
            return

        reason = ' '.join(args[1:]) or 'لا يوجد سبب'

        embed = discord.Embed(title='اينماا', color=0xff0000)
        embed.add_field(name='من قبل', value=f'<@{message.author.id}>', inline=False)
        embed.add_field(name='العضو الذي تم حظره', value=f'<@{user.id}>', inline=False)
        embed.add_field(name='السبب', value=reason, inline=False)
        embed.set_image(url='https://cdn.discordapp.com/attachments/1163901379220345014/1186022453634416751/New_Project_83_23679BC.gif?ex=6591bc7c&is=657f477c&hm=15f99bb667bc28380fa8d5e0eb9413c1498141525cb031e2b88c5c25fac50691&')

        await message.channel.send(embed=embed)
  elif message.content.startswith('اينماا'):
        await message.reply('نجب انت لست زورو الحقيقي, لا تسوي نفسك قوي')
  
  if message.author == bot.user or message.author.bot:
    return

  if message.content.startswith('+ping'):
    start_time = time.time()
    sent_message = await message.channel.send("يتم القياس...")
    end_time = time.time()
    ws_latency = (end_time - start_time) * 1000
    api_latency = round(bot.latency * 1000)
    round_trip_latency = (end_time - start_time) * 1000

    embed = discord.Embed(title="معلومات الاتصال",
                          description=f':ping_pong: **تأخير الاتصال بالخادم: {ws_latency:.2f} مللي ثانية**\n'
                                      f':robot: **تأخير الاتصال بواجهة البرمجة للتطبيقات: {api_latency} مللي ثانية**\n'
                                      f':arrows_counterclockwise: **تأخير الذهاب والعودة: {round_trip_latency:.2f} مللي ثانية**',
                          color=0xd5d35f)
    await sent_message.edit(content="", embed=embed)

  else:

    if message.content.startswith('#رابط'):  
        guild = message.guild
        channel = message.channel

        invite = await channel.create_invite(max_age=259200, unique=True)  

        embed = discord.Embed(title="𝐓𝐡𝐞 𝐄𝐦𝐩𝐢𝐫𝐞 𝐂𝐨𝐦𝐦𝐮𝐧𝐢𝐭𝐲",
                              color=0xd5d35f)
        embed.add_field(name="الرابط", value=invite.url, inline=False)
        embed.add_field(name="المدة", value="3 days", inline=False)
        embed.set_footer(text="Dev : Its.Zoro $")

        await message.author.send(embed=embed)
        await channel.send("تم ارسال الرابط في الخاص !!")

    elif message.channel.id == 1188943802287783946:
        member_username = message.author.name
        member_avatar_url = str(
            message.author.avatar.url) if message.author.avatar else str(
                message.author.default_avatar.url)

        embed = discord.Embed(title='𝐓𝐡𝐞 𝐄𝐦𝐩𝐢𝐫𝐞 𝐂𝐨𝐦𝐦𝐮𝐧𝐢𝐭𝐲',
                              description=message.content,
                              color=0xd5d35f)

        embed.set_author(name=member_username, icon_url=member_avatar_url)
        custom_image_url = "https://cdn.discordapp.com/emojis/1182419163784957954.gif?size=96&quality=lossless"
        embed.set_thumbnail(url=custom_image_url)

        sent_message = await message.channel.send(embed=embed)
        custom_emojis = [
            "<a:testarsvenom:1182418961611096075>", "<a:testarssgold:1182418931860901928>",
            "<a:testarsred:1182418900709806231>", "<a:testarsiron:1182418882032570388>", "<a:testarscyan:1182418870892503152>"
        ]

        for emoji in custom_emojis:
            await sent_message.add_reaction(emoji)

        additional_message = await message.channel.send("https://imgur.com/LaMGEnY")
        await asyncio.sleep(3)  # Delay to prevent multiple messages being sent
        await message.delete()



keep_alive()

bot.run('MTEzOTE2NzgxODQzMzE2NzM3MA.GWZ5bM.-vFpLsHS_Kku6U7_WerEtNTRhhUNMz-ahddPlM')
