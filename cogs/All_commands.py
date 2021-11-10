import discord 
import os
from discord.ext.commands import bot, errors
from discord.ext.commands import cog
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command
from discord.flags import Intents
from discord_slash import SlashCommand , SlashContext, client
from asyncio.tasks import wait
from collections import UserList
from discord_components import DiscordComponents,ButtonStyle,Button,InteractionEventType, component 
from discord import message
from discord_components.dpy_overrides import send
from yarl import URL
from discord.ext import commands
from discord_slash import cog_ext





class All_commands(commands.Cog):

 def __init__(self , client) :
     self.client = client
     
 @commands.Cog.listener()
 async def on_ready(self):
     print("On ready: bot is online cog listener")

 @commands.Cog.listener()
 async def on_command_error(self, ctx, error):
   '''       if(message == "info: ping"):
            return
        print(message)
        await ctx.send("``` An error has occured retry or please contact support server if the error continues and make sure you have entered the syntax right ```" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.gg/RW2J349bdu") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]]) '''

   '''cog_ext.cog_slash(name="how to get id" , description="Will explain how to get someones discord id to use this bot" , guild_ids=[888989551027163146])
 async def how_to_get_id(self , ctx):
        #embed = discord.Embed()  
        #embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/890899791574347786/bn.png")
        #embed.color = discord.Color.purple()
        #await ctx.reply(embed = embed)
        await ctx.send("testing")'''
   #print("command used or there is an error with {err}".format(err = error))
   pass


 @commands.command()
 async def help(self,ctx):
        message = ctx.message
        embed = discord.Embed()   
        embed.set_footer(text= "requested by {clientname}#{clientdiscriminator}|| Hope you have a great time using the bot :))  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator), icon_url=message.author.avatar_url)                 
        embed.title= "Information help"
        embed.description = "**• Type `info: userid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/)**"
        embed.add_field(name="__Main commands__" , value="`help` , `example` , `info: id`  , `info: guild-id` ,`how to get id` , `support`" , inline= False)
        embed.add_field(name="__Other commands__" , value="`ping` , `vote` , `info: id help` , `nitro users`, `site list` , `server count` , `privacy policy` , `report bug` , `who made you` , `updates`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed, components = 
        [[Button(style=ButtonStyle.URL, label="Support server", url="https://discord.gg/RW2J349bdu") , 
         Button(style=ButtonStyle.URL, label="Example", url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png"),
         Button(style=ButtonStyle.URL, label="Vote for us", url="https://top.gg/bot/888985968554688512/vote")
         ]])       
  
 @commands.command()
 async def example(self,ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png")
        embed.color = discord.Color.purple()
        await ctx.reply(embed = embed)
                  
 @commands.command()
 async def invite(self,ctx):
           await ctx( " ` click the invite button to add me into your server !!! ` " , 
           components = [
           [Button(style=ButtonStyle.URL, label="invite", url="https://discord.com/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands") , Button(style=ButtonStyle.URL, label="Support server", url="https://discord.gg/RW2J349bdu")]
           ])
 @commands.command()
 async def support(self,ctx):     
    await ctx.reply("if there are any issues with the bot \n \n`possible fixes -` \n➤ make sure you entered the command's syntax right. \n➤ try info: help or info: example. \n➤ make sure you gave the bot permissions to embed,message and etc. \n➤ join the support server and in the #support ask for help or report this and we will help you within 24hrs of time. \n➤ if nothing works contact us at ritthedevcontact@gmail.com ." , components = [
           [Button(style=ButtonStyle.URL, label="Support server", url="https://discord.gg/RW2J349bdu") ,  Button(style=ButtonStyle.URL, label="Example", url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png")]
           ]) 
 @commands.command()
 async def updates(self,ctx):     
    await ctx.reply("```md\nDiscord user info bot v2.0 (Global release)\n\n#New \n- how to get id improved along with its command syntax\n- bot is rewritten with discord.ext frame work and cogs\n- added help slash command\n- added support command\n- added who made you command\n- added vote,privacy policy,report bug,site list commands\n- added nitro users command\n- added updates command\n\n#Changes\n- snipe command removed to run the bot smoothly\n- minor changes in help command and embed components\n- added a buch of new details about a user and server\n- server count command can be accesed by anyone now\n\n#bug fixes\n- fixed errors with guild id\n- fixed bot not responding for privacy policy\n- fixed components redirecting to wrong links\n```") 

 @commands.command()
 async def id(self,ctx):  
     await ctx.reply("```Please enter the id of the user instead of the word 'ID' type info: example for more information```") 

                        

def setup(client):
 client.add_cog(All_commands(client))








#old code

'''
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

'''