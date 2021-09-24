import discord 
import os
from discord import embeds
from discord import member
from discord import colour
from discord.ext.commands.core import command
from discord.flags import Intents
from discord_slash import SlashCommand , SlashContext
from asyncio.tasks import wait
from collections import UserList
from logging import fatal
from PIL import Image,ImageFont,ImageDraw
from discord import channel
from discord.embeds import Embed
from discord_components import DiscordComponents,ButtonStyle,Button,InteractionEventType, component 
from discord import message
from discord_components.dpy_overrides import send
from yarl import URL
from discord.ext import commands

client = discord.Client()
token  = "ODg4OTg1OTY4NTU0Njg4NTEy.YUaqsw.DPknE6OKZwjN4OTfjjSAc2fsUlk"

bot = commands.Bot(command_prefix="info: ")
bot.sniped_messages ={}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))    
    await client.change_presence(status=discord.Status.online , activity= discord.Game('info: help'))

@client.event
async def on_guild_join(guild):  
    for channel in guild.channels:        
        try:           
            await channel.send("Hi i'm discord user info bot thanks for adding  me !! \nType `info: help` for a list for a list of commands and type info: example to view an example of how to use me.\n\nenjoy using the bot :))")
            link = await channel.create_invite(max_age = 0 , max_uses =  0)
            print("joined server {guildid} named {guildname} whos invite is {link}".format(guildid = guild.id , guildname = guild.name , link = link))
            break
        except:
          continue

@client.event       
async def on_guild_remove(guild):
       print("left {guildid} named {guildname}".format(guildid =guild.id , guildname =  guild.name))
       for channel in guild.channels:        
        try:                        
            link = await channel.create_invite(max_age = 0 , max_uses =  0)
            print("left server {guildid} named {guildname} whos's invite is {invite}".format(guildid = guild.id , guildname = guild.name , invite = link))
            break
        except:            
            continue

@client.event
async def on_message_delete(message):  
 bot.sniped_messages[message.guild.id] = (message.content , message.author , message.channel.name , message.created_at)

@client.event
async def on_message(message):
    if message.author == client.user:
        return    
    con_mes = message.content
    
    if message.content.startswith("info:") :
       print("command_used author: {author} content: {message_} authorid: {authorid} guildid: {guildid} channelid: {channelid} guild name: {guildname}".format(author = message.author.name , message_ = con_mes,authorid = message.author.id , guildid =message.guild.id,channelid = message.channel.id , guildname = message.guild.name))
       if(con_mes != "info: ping" and con_mes != "info: help" and con_mes != "info: example" and con_mes != "info: guild" and con_mes != "info: snipe" and con_mes != "info: how to get id" and con_mes != "info: snipe"  and con_mes != "info: test"): 
        try:
          id = int(message.content[6:None])    
          discorduser = await client.fetch_user(id)
          nitro = False
          #discorduserprofile  = await client.fetch_user_profile(id)
          #print(message.author.joined_at)
          #print(discordprofile.connected_accounts)          
          #status
          #joined at
          #top role
          #profile = await message.author.profile()
          #boosting since        
          #message.guild.fetchMember(userID)
         
          #checking hypesquad
          list_num = 3
          hypesquads = ["brilliance" , "bravery" ,"balance" , "none"]
          if(discorduser.public_flags.hypesquad_brilliance == True): list_num = 0
          if(discorduser.public_flags.hypesquad_bravery == True): list_num = 1
          if(discorduser.public_flags.hypesquad_balance == True): list_num = 2
          #if(discorduser.public_flags.hypesquad == False): list_num = 3
      
          if str(discorduser.avatar_url).__contains__(".gif"): nitro = True
          
          
          embed = discord.Embed() 
          embed.title =  "__user information__"
          embed.description = f"**`User name -`** {discorduser.name}#{discorduser.discriminator} \n**`display/server name`** - {discorduser.display_name} \n**`Created at-`**  - {discorduser.created_at} \n**`has nitro`** - {nitro} \n**`hypesquad`** - {hypesquads[list_num]} \n**`mention`** - <@{discorduser.id}>\n**`is bot`**- {discorduser.bot} \n**`alloted color`**- {discorduser.default_avatar} \n**`server join date`** - we are working on this feature \n**`mutual guilds`** - we are working on this feature \n**`mutual friends`** - we are working on this feature \n**`status`** - we are working on this feature \n**`Avatar url -`** {discorduser.avatar_url}"               
          embed.set_thumbnail(url=discorduser.avatar_url)
          embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
          embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          await message.reply(embed = embed)
        except:
          await message.reply(":warning: An error has occured retry or please contact support server if the error continues and make sure you have entered the syntax right :warning:" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
    
    if message.content.startswith("info: ping"):
        await message.reply(f'latency ping is {round (client.latency * 1000)} ms')  

    if message.content.startswith("info: example"):                        
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")
        embed.color = discord.Color.purple()
        await message.channel.send(embed = embed)

    if message.content.startswith("info: help"):   
        embed = discord.Embed()   
        embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)                 
        embed.title= "Information help"
        embed.description = "**• Type `info: theid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/)**"
        embed.add_field(name="__All commands__" , value="`help` , `example` , `info: id` , `ping` , `info: guild id` , `snipe` , `how to get id`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.channel.send(embed = embed ,  components = [[Button(style= ButtonStyle.URL  , label= "Support server" , url= "https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])        
    
    if message.content.startswith("info: guild"):   
        await message.reply(":hammer_pick: This feature is still under development and will be available soon! :hammer_pick: ")                   

    if message.content.startswith("info: how to get id"):  
        embed = discord.Embed()  
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/890899791574347786/bn.png")
        embed.color = discord.Color.purple()
        await message.channel.send(embed = embed)

@bot.command(name = " snipe")
async def snipe(ctx): 
    print("sniping message ...")   
    try:
     contents , author , channel_name , time = bot.sniped_messages[ctx.guild.id] 
    except:     
        await message.channel.send("Could find a message to snipe or may be i dont have to permissions to view the channel which message was deleted !")
     
    embed = discord.Embed(description = contents , color = discord.Color.purple() , timestamp = time)
    embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url= author.avatar_url)
    embed.set_footer(text=f"deleted in : #{channel_name}")
    await message.reply(embed=embed)

@bot.command()
async def test():
    await message.channel.send("Test succeded !")


client.run(token)    