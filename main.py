import re
import discord 
import os
from discord import guild
from discord.ext.commands.core import command
from discord.flags import Intents
from discord_slash import SlashCommand , SlashContext
from asyncio.tasks import wait
from collections import UserList
from discord_components import DiscordComponents,ButtonStyle,Button,InteractionEventType, component 
from discord import message
from discord_components.dpy_overrides import fetch_message, send
from yarl import URL
from discord.ext import commands


intents = discord.Intents().all()
client = commands.Bot(command_prefix='info: ',  intents=intents )
token  = "ODg4OTg1OTY4NTU0Njg4NTEy.YUaqsw.hEeRaJapSDeFYylXrSCwf9zrQQ0"
native_client = discord.Client()

#cleaning
client.remove_command("help")

@client.event
async def on_ready():
    print('On ready: We have logged in as {0.user}'.format(client))    
    await client.change_presence(status=discord.Status.online , activity= discord.Game('info: help'))

@client.event
async def on_guild_join(guild):  
    for channel in guild.channels:        
        try:           
            await channel.send("Hi i'm discord user info bot thanks for adding  me !! \nType `info: help` for a list for a list of commands and type info: example to view an example of how to use me.\n\nenjoy using the bot :))")
            #link = await channel.create_invite(max_age = 0 , max_uses =  0)
            print("joined server {guildid} named {guildname} whos invite is {link}".format(guildid = guild.id , guildname = guild.names))
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
async def on_message(message):
 
 if(message.content.startswith("info:")): 
    print("command_used author: {author} content: {message_} authorid: {authorid} guildid: {guildid} channelid: {channelid} guild name: {guildname}".format(author = message.author.name , message_ = message.content,authorid = message.author.id , guildid =message.guild.id,channelid = message.channel.id , guildname = message.guild.name))
    used_guild_command = False
    if message.author == client.user:
        return    
    con_mes = message.content
    
    try:
      if(int(con_mes[5:None])): 
          used_main_command = True
          try:
            await client.fetch_user(int(con_mes[5:None]))
            used_guild_command = False
          except:
            await client.fetch_guild(int(con_mes[5:None]))
            used_guild_command = True
    except:
        used_main_command = False
    
 
    if message.content.startswith("info:") :
      if(used_main_command == True and used_guild_command == False):
        try:
          id = int(message.content[6:None])    
          discorduser = await client.fetch_user(id)
          nitro = False
          member_in_guild = False
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

          for mem_id in message.guild.members:
               if(mem_id.id == discorduser.id):
                   member_in_guild = True
         
          
          embed = discord.Embed() 
          embed.title =  "__User information__"
          embed.description = f"**`User name -`** {discorduser.name}#{discorduser.discriminator} \n**`display/server name`** - {discorduser.display_name} \n**`Created at-`**  - {discorduser.created_at} \n**`has nitro`** - {nitro} \n**`hypesquad`** - {hypesquads[list_num]} \n**`mention`** - <@{discorduser.id}>\n**`is bot`**- {discorduser.bot} \n**`alloted color`**- {discorduser.default_avatar} \n**`server join date`** - we are working on this feature \n**`status`** - we are working on this feature \n**`Avatar url -`** {discorduser.avatar_url} \n**`in this server -`** {member_in_guild}"               
          embed.set_thumbnail(url=discorduser.avatar_url)
          embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
          embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
          #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: how to guild id` to know how to get a users or guilds id")
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          await message.reply(embed = embed)
        except:
          await message.reply(":warning: An error has occured retry or please contact support server if the error continues and make sure you have entered the syntax right :warning:" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
     
      if(used_main_command == True and used_guild_command == True):
       try:
      
        g_id = int(message.content[6:None])
        guild_new = await client.fetch_guild(g_id)
        membercount = "we are woking on this feature"
        guild_desciption = guild_new.description
        guild_made_at = guild_new.created_at

        embed = discord.Embed() 
        embed.title =  "__Guild information__"
        embed.set_thumbnail(url=guild_new.icon_url)
        embed.description = "**`Guild name -`** {name} \n **`Guild description -`** {desc} \n **`member count -`** {mem_count} , \n **`created at -`** {created_at}".format(name = guild_new , desc = guild_desciption , mem_count = membercount , created_at = guild_made_at)
        embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
        embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
        #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: how to guild id` to know how to get a users or guilds id")
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed)
       except Exception as err:
           await message.replay("⚠ An error has occured most probably as the bot couldnt acces the server we will fix this issue soon type info: report bug and report this issue error code {error_code} ⚠".format(error_code = err))

   
   
    if (message.content.startswith("info: ping")):
         await message.reply(f'latency ping is {round (client.latency * 1000)} ms')
   
    if(message.content.startswith("info: server count")):
        if(message.author.id == 764736831643975693):
         await message.reply("I'm in " + str(len(client.guilds)) + " servers!")
        else:
         await message.reply(":hammer_pick: this feature is still under development and will be available soon! :hammer_pick:")
     

    if(message.content.startswith("info: vote")):
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Vote for the bot" 
         embed2.description = "**Voting the bot would be really great and you can support our development this way, thanks a lot if you have voted \n\n• [top.gg](https://top.gg/bot/888985968554688512) \n• [discord bot list](https://discordbotlist.com/bots/discord-user-info-bot/upvote) ** \n\nclick the buttons below to visit the pages :))"        
         embed2.set_footer(text= "requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
         embed2.color = discord.Color.green()
         await message.channel.send(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Top.gg" , url =  "https://top.gg/bot/846634813322166302/vote") ,
           Button(style=ButtonStyle.URL , label="Discord bot list" , url =  "https://discordbotlist.com/bots/dank-tax-calculator/upvote") ,           
           ]]) 

    if(message.content.startswith("info: site list")):   
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Site list" 
         embed2.description = "**A list of sites where out bot is available at \n\n• top.gg \n• discord bot list \n• discord bots.gg \n• infinity bot list \n• discord extreme list **\n\nvisit those pages by clicking the buttons below"        
         embed2.set_footer(text= "requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
         embed2.color = discord.Color.from_rgb( 117, 255, 255 )
         await message.reply(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="top.gg" , url =  "https://top.gg/bot/846634813322166302") ,
           Button(style=ButtonStyle.URL , label="Discord bot list" , url =  "https://discordbotlist.com/bots/discord-user-info-bot") ,
           #Button(style=ButtonStyle.URL , label="Infinity bot list" , url =  "Currently not available") 
           #Button(style=ButtonStyle.URL , label="Discord bots.gg" , url =  "Currently not available") ,
           Button(style=ButtonStyle.URL , label="Discord extreme list" , url =  "https://discordextremelist.xyz/en-US/bots/888985968554688512")
           ]])  
    if(message.content.startswith("info: privacy")):
        await message.reply("```We dont store any user information and log only the guilds joined and commands used by the user and delete the data within few days also we store the data offline ie locally so that no-one can access it or breach into it !! \n\n➤ why we need the data and how we use it \nwe use it to improve user experience and know how the bot is doing with the users \n\n➤ who do we share the data \nwe dont share it to anyone and it is limited to our servers and local copies \n\n➤ how to contact or request to delete your data \nvisit https://ritthedev.itch.io/ and there are various ways listed over there to contact us if we didnt respond any where then , mail us at ritthedevcontact@gmail.com or join our support server and in the #support channel ask @developmentteam to delete your data we will do it within 24 hrs \n\nThank you !```")

    if(message.content.startswith("info: how to get id")):
        embed = discord.Embed()  
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/890899791574347786/bn.png")
        embed.color = discord.Color.purple()
        await message.reply(embed = embed) 

    if(message.content.startswith("info: report bug")):
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Report a bug 🛠" 
         embed2.description = "**Reporting bugs would be really great and would improve the bot for many users using it**"        
         embed2.add_field(name="__How to report a bug__" , value = "➤ join our community server and in #bug-reports send ur bug and we will fix it soon and infom you \n➤ visit our sub-reddit page and post your bug \n➤ mail your bug to ✉ ritthedevcontact@gmail.com and we will reply soon \nthank you !!" , inline= False)
         embed2.set_footer(text= "requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
         embed2.color = discord.Color.dark_orange()
         await message.channel.send(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Discord server" , url =  "https://discord.gg/RW2J349bdu") ,
           Button(style=ButtonStyle.URL , label="Sub-reddit" , url =  "https://www.reddit.com/r/ritthedev_community/") , 
           Button(style=ButtonStyle.URL , label="Mail us" , url =  "https://mail.google.com/mail/u/0/#inbox?compose=new")                     
           ]])      
 
   

    await client.process_commands(message)



#loading cogs and extintions
os.chdir(os.getcwd())
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    

client.run(token)    