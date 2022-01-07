import discord 
import os
from discord import guild
from discord import user
from discord.ext.commands import bot
from discord.ext.commands.converter import clean_content
from discord.ext.commands.core import check, command
from discord.flags import Intents
from discord_slash import SlashCommand , SlashContext, context
from asyncio.tasks import wait
from collections import UserList
from discord_components import DiscordComponents,ButtonStyle,Button,InteractionEventType, component 
from discord import message
from discord_components.dpy_overrides import fetch_message, send
from yarl import URL
from discord.ext import commands
from discord_slash import SlashCommand , SlashContext
from discord_slash.utils.manage_commands import create_choice , create_option

intents = discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix='info: ',  intents=intents)
token  = "ODg4OTg1OTY4NTU0Njg4NTEy.YUaqsw.hEeRaJapSDeFYylXrSCwf9zrQQ0"
native_client = discord.Client()
slash = SlashCommand(client , sync_commands= True)

#cleaning
client.remove_command("help")
limit_count = 0
# , guild_ids=[888989551027163146 , 834089778215125002]

@slash.slash(name="help" , description="Get a list of all commands and how to use the bot")
async def help(ctx:SlashContext):
        message = ctx.message
        embed = discord.Embed()   
        #embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)                 
        embed.title= "Information help"
        embed.description = "**• Type `info: userid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/) \n• Click [here](https://discord.com/api/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands) to add me into another server  \n• feel free to join our support server [here](https://discord.gg/RW2J349bdu)**"
        embed.add_field(name="__Main commands__" , value="`help` , `example` , `info: id`  , `info: guildid` ,`how to get id` , `support` ,`this` , `thisg`" , inline= False)
        embed.add_field(name="__Other commands__" , value="`ping` , `vote` , `info: id help` , `nitro users`, `site list` , `server count` , `privacy policy` , `report bug` , `who made you` , `updates`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await ctx.reply(embed = embed)  
        print("used slash command")     
        

@client.event
async def on_ready():
    print('On ready: We have logged in as {0.user}'.format(client))    
    await client.change_presence(status=discord.Status.online , activity= discord.Game('info: help'))
   
    '''for i in client.guilds:
      print(i.owner.id)'''

    '''for i in client.guilds:
     print(i.id)'''


    '''
           bot_count_new = 0  for bot_count_mem in client.get_guild(i.id).members:
      if bot_count_mem.bot:
        bot_count_new = bot_count_new + 1 '''
     #print(str(i.member_count) + "," + str(bot_count_new))

    '''for i in range(0,160):      
       try:          
         guild =  client.guilds[i]
         channel = guild.text_channels[0]     
       
         if(guild.id == 834089778215125002):
          link = await channel.create_invite(max_age = 0)          
          print(link)
         else:
            print("not the guild searching .....")
       except:
           print("error with {guildid}".format(guildid = guild.id))
           i = i + 1 '''
     
    


 
@client.event
async def on_guild_join(guild): 
    print("joined server {guildid} named {guildname}".format(guildid = guild.id , guildname = guild.name )) 
    for channel in guild.channels:        
        try:   
         embed = discord.Embed()   
         embed.set_footer(text= "Enjoy using the bot :))")                         
         embed.description = "**Hi i'm User information bot ,Thanks for adding  me !!** \n\nType `info: help` for a list for a list of commands and type `info: example` to view an example of how to use me."        
         embed.color = discord.Color.from_rgb( 117, 255, 255 )             
         await channel.send(embed=embed, components = 
         [[Button(style=ButtonStyle.URL, label="Support server", url="https://discord.gg/RW2J349bdu") , 
         Button(style=ButtonStyle.URL, label="Example", url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png"), Button(style=ButtonStyle.URL, label="Invite", url="https://discord.com/api/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands")
         ]])
        #await channel.send("Hi i'm User information bot ,Thanks for adding  me !! \n\nType `info: help` for a list for a list of commands and type `info: example` to view an example of how to use me.\n\nenjoy using the bot :)")
        #link = await channel.create_invite(max_age = 0 , max_uses =  0)      
         break
        except:
          continue


@client.event       
async def on_guild_remove(guild):
       #print("left {guildid} named {guildname}".format(guildid =guild.id , guildname =  guild.name))
       for channel in guild.channels:        
        try:                        
            #link = await channel.create_invite(max_age = 0 , max_uses =  0)
            print("left server {guildid} named {guildname} ".format(guildid = guild.id , guildname = guild.name ))
            break
        except:            
            continue


@client.event
async def on_message(message):
 try:
  if(message.content.startswith("info:")): 
    
    print("command_used author: {author} content: {message_} authorid: {authorid} guildid: {guildid} channelid: {channelid} guild name: {guildname}".format(author = message.author.name , message_ = message.content,authorid = message.author.id , guildid =message.guild.id,channelid = message.channel.id , guildname = message.guild.name))
    used_guild_command = True
    used_main_command = True

    if message.author == client.user:
        return    
    con_mes = message.content
    
    try:
       try:
        if message.content.index("@") == 7:
         if(int(con_mes[9:-1])):                   
            used_main_command = True             
       except:
        if(int(con_mes[5:None])):                   
            used_main_command = True           
                    
    except:
        #print(message.content.index("@"))
        used_main_command = False 
      
 
    try:
     try:
      try:
        if message.content.index("@") == 7:
         await client.fetch_user(int(con_mes[9:-1]))
         used_guild_command = False
      except:
         await client.fetch_user(int(con_mes[5:None]))
         used_guild_command = False     
    
     except:
      await client.fetch_guild(int(con_mes[5:None]))  
      used_guild_command = True
    
     

    except Exception as error_new:
      #print(str(error_new))
      if( str(error_new) != "403 Forbidden (error code: 50001): Missing Access" or str(error_new)[0:10] == "invalid literal for int() with base 10: ' help'"):
       #await message.reply("```⚠ a_n error has occured make sure you entered the bots command right or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs ⚠ ```" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
       pass

    if(message.content == "info: this"):
      used_main_command = True
      used_guild_command = False
    if(message.content == "info: thisg"):
      used_guild_command = True
      used_main_command = True

    if message.content.startswith("info:") :
    
      if(used_main_command == True and used_guild_command == False):
        
        try:          
          if message.content == "info: this":
           id = int(message.author.id)
          else:
           try:
            if message.content.index("@") == 7:
             id = int(message.content[9:-1]) 
           except:
             id = int(message.content[6:None])           
          

          discorduser = await client.fetch_user(id)
          nitro = False
          member_in_guild = False       
          #discorduserprofile  = await client.fetch_user_profile(id)      
          #checking hypesquad
          list_num = 3
          hypesquads = ["brilliance" , "bravery" ,"balance" , "none"]
          if(discorduser.public_flags.hypesquad_brilliance == True): list_num = 0
          if(discorduser.public_flags.hypesquad_bravery == True): list_num = 1
          if(discorduser.public_flags.hypesquad_balance == True): list_num = 2
          #if(discorduser.public_flags.hypesquad == False): list_num = 3
          #in the server methods          
          server_member = ""          
          for member in message.guild.members:
            if(member.id == discorduser.id):
              server_member = member

          if str(discorduser.avatar_url).__contains__(".gif"): nitro = True
          
          mobile =""
          boosting_since = ""

          for mem_id in message.guild.members:
               if(mem_id.id == discorduser.id):
                   member_in_guild = True

         
          
          embed = discord.Embed() 
          embed.title =  "__User Information__"
          embed.description = f"**`User name -`** {discorduser.name}#{discorduser.discriminator} \n**`Display/Server name`** - {discorduser.display_name} \n**`Created at-`**  - {discorduser.created_at} \n**`Has nitro`** - {nitro} \n**`Hypesquad`** - {hypesquads[list_num]} \n**`Mention`** - <@{discorduser.id}>\n**`Is bot?`**- {discorduser.bot} \n**`Alloted color`**- {discorduser.default_avatar} \n**`Avatar url -`** {discorduser.avatar_url} \n**`In this server -`** {member_in_guild}"               
          embed.set_thumbnail(url=discorduser.avatar_url)
          embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)          
          if(member_in_guild == True):                     
           if(server_member.is_on_mobile()): mobile = "yes" 
           else: mobile = "Not using mobile currently"
           if(server_member.premium_since == None): boosting_since = "Not boosting this server"
           else: boosting_since = server_member.premium_since
           embed.add_field(name="__In Guild Information__" ,value="**`Join date`** - {date} \n**`Activity`** - {activity} \n**`Status`** - {status} \n**`Nick name`** - {nick} \n**`Boosting server`** - {boosting_since} \n**`On mobile`** - {mobile} \n**`Top role`** - {top_role}".format(date = server_member.joined_at , activity = server_member.activity ,status = server_member.desktop_status , nick = server_member.nick , mobile = mobile   , boosting_since = boosting_since , top_role = server_member.top_role) , inline= False)
          #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: id help` to know how to get a users or server id")
          #embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          await message.reply(embed = embed)
        except Exception as err:
          await message.reply("```⚠ An error has occured make sure you entered the bots command right and the id correctly or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs Error Code - {err} ⚠ ```".format(err = err), components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
          pass
     
      if(used_main_command == True and used_guild_command == True):
       #print("UsedGuild")
       try:
       
        if message.content == "info: thisg":
           g_id = int(message.guild.id)
        else:
           g_id = int(message.content[6:None])
      
        
        guild_new = await client.fetch_guild(g_id)

        bot_count = 0
        for bot_count_mem in client.get_guild(g_id).members:
          if bot_count_mem.bot:
            bot_count = bot_count + 1

        guild_desciption = guild_new.description
        guild_made_at = guild_new.created_at
        owner = guild_new.owner_id      
        boost_tier = guild_new.premium_tier        
        member_count = client.get_guild(g_id).member_count
        subscribers = len(client.get_guild(g_id).premium_subscribers)
        #for member in client.get_guild(g_id):
          #member_count += 1
        security_level= "none"
        security_level_num = guild_new.mfa_level
        security_levels = ["low" , "medium" , "high" , "highest"]      
        security_level = security_levels[security_level_num]

        embed = discord.Embed() 
        embed.title =  "__Guild Information__"
        embed.set_thumbnail(url=guild_new.icon_url)
        embed.description = "**`Guild name -`** {name} \n **`Guild description -`** \n{desc} \n **`Member count -`** {mem_count} \n**`Bots -`** {bot_count} \n **`Created at -`** {created_at} \n**`Owner id -`** {owner} \n**`Boost level -`** {boosters} \n**`Security level -`** {sec_level} \n**`Boosters -`** {subs} ".format(name = guild_new , desc = guild_desciption , mem_count = member_count , created_at = guild_made_at ,owner = owner , boosters = boost_tier , sec_level = security_level , subs = subscribers , bot_count = bot_count)
        #embed.description = "name - {name}".format(name = guild_new.name)
        embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
        #embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
        #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: how to guild id` to know how to get a users or guilds id")
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed)
        
       except Exception as err:
           await message.reply("```⚠ An error has occured most probably as the bot couldnt acces the server we will fix this issue soon type info: report bug and report this issue error code: {error_code} ⚠ ```".format(error_code = err) , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu")]])

    '''if(message.content.startswith("info: help")):
        
        embed = discord.Embed()   
        embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)                 
        embed.title= "Information help"
        embed.description = "**• Type `info: userid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/)**"
        embed.add_field(name="__Main commands__" , value="`help` , `example` , `info: id`  , `info: guild-id` ,`how to get id` , `support`" , inline= False)
        embed.add_field(name="__Other commands__" , value="`ping` , `vote` , `info: id help` , `nitro users`, `site list` , `server count` , `privacy policy` , `report bug` , `who made you` , `updates`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed) '''  
   
    if (message.content.startswith("info: ping")):
         await message.reply(f'latency ping is {round (client.latency * 1000)} ms')
    
    if (message.content.startswith("info: nitro users")):
         
        
         guild_id = message.guild.id
         if(len(client.get_guild(guild_id).members) > 6000):
          print("```your server has too many members to scan for ie more than thousand fetching nitro users isnt currently available for servers with more than 1000 members```")
          return
         guild_new_members = client.get_guild(guild_id).members              
         nitro_users = [] 
         for member in guild_new_members:
          if(str(member.avatar_url).__contains__(".gif")):
            nitro_users.append(member.id)         
         if(nitro_users == []):
           await message.reply("We found no users with nitro in this guild ,if you Feel this is an error please type `info: report bug` to report this issue !" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu")]])        
         else: 
          await message.reply(nitro_users)         
   
    if(message.content.startswith("info: server count")):
       
         await message.reply("I'm in " + str(len(client.guilds)) + " servers!")
         #else:
         #await message.reply(":hammer_pick: this feature is still under development and will be available soon! :hammer_pick:")
     

    if(message.content.startswith("info: vote")):
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Vote for the bot" 
         embed2.description = "**Voting the bot would be really great and you can support our development this way, thanks a lot if you have voted \n\n• [top.gg](https://top.gg/bot/888985968554688512) \n• [discord bot list](https://discordbotlist.com/bots/discord-user-info-bot/upvote) ** \n\nclick the buttons below to visit the pages :))"        
         embed2.set_footer(text= "requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
         embed2.color = discord.Color.green()
         await message.channel.send(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Top.gg" , url =  "https://top.gg/bot/888985968554688512") ,
           Button(style=ButtonStyle.URL , label="Discord bot list" , url =  "https://discordbotlist.com/bots/discord-user-info-bot") ,           
           ]]) 

    if(message.content.startswith("info: site list")):   
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Site list" 
         embed2.description = "**A list of sites where out bot is available at \n\n• top.gg \n• discord bot list \n• discord bots.gg \n• infinity bot list \n• discord extreme list **\n\nvisit those pages by clicking the buttons below"        
         embed2.set_footer(text= "requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
         embed2.color = discord.Color.from_rgb( 117, 255, 255 )
         await message.reply(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Top.gg" , url =  "https://top.gg/bot/888985968554688512") ,
           Button(style=ButtonStyle.URL , label="Discord bot list" , url =  "https://discordbotlist.com/bots/discord-user-info-bot") ,
           Button(style=ButtonStyle.URL , label="Infinity bot list" , url =  "https://infinitybotlist.com/bots/888985968554688512/")] ,[
           Button(style=ButtonStyle.URL , label="Fateslist.xyz" , url =  "https://fateslist.xyz/bot/888985968554688512") ,           
           Button(style=ButtonStyle.URL , label="Discord extreme list" , url =  "https://discordextremelist.xyz/en-US/bots/888985968554688512"),
           Button(style=ButtonStyle.URL , label="Our website" , url =  "https://discord-user-info-bot.glitch.me/")
           ]])  
    if(message.content.startswith("info: privacy policy")):
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
    if message.content.startswith("info: invite"):
        await message.reply( " ` click the invite button to add me into your server !!! ` " , 
           components = [
           [Button(style=ButtonStyle.URL, label="invite", url="https://discord.com/api/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands") , Button(style=ButtonStyle.URL, label="Support server", url="https://discord.gg/RW2J349bdu")]
           ])

    if message.content == "info: id help":
          embed = discord.Embed()
          embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)
          embed.add_field(name="__User id__" ,value="type `info: how to get id` to get someones discord id and type `info: (paste the id here)` to get a users information" , inline= False) 
          embed.add_field(name="__Server id__" ,value="using similar process after turning on developer mode right click on the server icon and click copy id and type `info: (paste the id here)` to get a servers information note:- due to discord API policies we can retrive information from the servers if the bot is in that server" , inline= False) 
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          await message.reply(embed = embed ,components = [
            [Button(style= ButtonStyle.URL , label="user example" , url ="https://cdn.discordapp.com/attachments/890895848773419038/896286726010568724/unknown.png"),
            Button(style= ButtonStyle.URL , label="server example" , url ="https://cdn.discordapp.com/attachments/890895848773419038/896286468887167026/unknown.png"),
            Button(style= ButtonStyle.URL , label="Support server" , url ="https://discord.gg/RW2J349bdu")
            ]])
    
    '''if message.content.startswith("info: leave") and message.author.id == 764736831643975693:
      to_leave = client.get_guild(int(con_mes[12:None])) 
      print("left"+ " , " + str(to_leave.name) + " , " + str(len(client.guilds)) )
      await to_leave.leave()
      #print(int(con_mes[12:None]))'''
      

      #print("hello")

    if(message.content.startswith("info:help")):
      await message.reply("it's `info: help` ,dont forget the space bud !!")
    
    if(message.content.startswith("info: who made you")):
     if(message.author.id == 764736831643975693):
       await message.reply("you made me and  asking me who made you how dumb lol")
     else:
      await message.reply("**RitTheDeV#0519** made me and {author_name} you are most welcomed join our community server :)".format(author_name = message.author.name) , components = [[ Button(style=ButtonStyle.URL, label="Support server", url="https://discord.gg/RW2J349bdu" ), Button(style=ButtonStyle.URL, label="Join Sub-reddit", url="https://www.reddit.com/r/ritthedev_community/" ), Button(style=ButtonStyle.URL, label="View our projects", url="https://ritthedev.itch.io")]])  
 except Exception as err:
   try:
     print(int(con_mes[5:None]))
   except:
    await message.reply("```⚠ An or has occured make sure you entered the bots command right or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs (line 380)⚠ ```" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
    pass

 await client.process_commands(message)


 
 



#loading cogs and extintions
os.chdir(os.getcwd())
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    

client.run(token)    