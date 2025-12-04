from logging import exception
from pydoc import cli
from urllib.request import urlopen
import discord 
from discord.ext.commands.core import check, command
from discord_slash import SlashCommand , SlashContext, context
from discord_components import DiscordComponents,ButtonStyle,Button,InteractionEventType, component 
from discord_components.dpy_overrides import fetch_message, send
from discord.ext import commands
from discord_slash import SlashCommand , SlashContext
from discord_slash.utils.manage_commands import create_choice , create_option
from discord.ui import View
from discord.commands import Option
from discord.commands import SlashCommandGroup


#Variables
intents = discord.Intents().default()
intents.members = True
client = discord.Bot(intents=intents)
#debug_guilds=[888989551027163146,834089778215125002] 
token  = ""
#slash = SlashCommand(client , sync_commands= True)


no_autoresponse_guilds=[]
ColorDictonary =	{"0": "Blue","1": "Grey","2": "Green","3": "Yellow","4": "Red","5": "Pink"}

''' Old Vars
#client = commands.Bot(command_prefix='info: ',  intents=intents)
#native_client = discord.Client()
#cleaning
#client.remove_command("help")
guild_ids=[834089778215125002]
'''

#Views
class HelpCommandView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://discord.com/invite/gzaz9SSkkW"
        url2 = f"https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png"
        url3 =f"https://discord.com/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands"
        self.add_item(discord.ui.Button(label="Support server", url=url))
        self.add_item(discord.ui.Button(label="Example", url=url2))
        self.add_item(discord.ui.Button(label="Invite", url=url3))

class IdHelpView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://discord.com/invite/gzaz9SSkkW"
        url3 = f"https://cdn.discordapp.com/attachments/890895848773419038/896286468887167026/unknown.png"
        url2 = f"https://cdn.discordapp.com/attachments/890895848773419038/896286726010568724/unknown.png"
        self.add_item(discord.ui.Button(label="Support server", url=url))
        self.add_item(discord.ui.Button(label="User example", url=url2))
        self.add_item(discord.ui.Button(label="Server example", url=url3))     

class SupportView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://discord.com/invite/gzaz9SSkkW"
        url2 = f"https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png"
        self.add_item(discord.ui.Button(label="Support server", url=url))
        self.add_item(discord.ui.Button(label="Example", url=url2))  

class SupportServerView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://discord.com/invite/gzaz9SSkkW"
        self.add_item(discord.ui.Button(label="Support server", url=url))
    

class AboutView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://discord.com/invite/gzaz9SSkkW"
        url2 = f"https://ritthedev.itch.io/"
        self.add_item(discord.ui.Button(label="Support server", url=url))
        self.add_item(discord.ui.Button(label="Developer portfolio", url=url2))     


class VoteView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://top.gg/bot/888985968554688512"
        url2 = f"https://discordbotlist.com/bots/discord-user-info-bot"
        self.add_item(discord.ui.Button(label="Top.gg", url=url))
        self.add_item(discord.ui.Button(label="Discord bot list", url=url2))    

class SiteListView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://top.gg/bot/888985968554688512"
        url2 = f"https://discordbotlist.com/bots/discord-user-info-bot"
        url3= f"https://infinitybotlist.com/bots/888985968554688512/"
        url4= f"https://discordextremelist.xyz/en-US/bots/888985968554688512"
        url5= f"https://discord-user-info-client.glitch.me/"
        self.add_item(discord.ui.Button(label="Top.gg", url=url))
        self.add_item(discord.ui.Button(label="Discord bot list", url=url2))  
        self.add_item(discord.ui.Button(label="Infinity bot list", url=url3))  
        self.add_item(discord.ui.Button(label="Discord extreme list", url=url4))          
        self.add_item(discord.ui.Button(label="Our website", url=url5))  

class ReportBugView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url = f"https://discord.com/invite/gzaz9SSkkW"
        url2 = f"https://ritthedev.itch.io/"
        url3 = f"http://alecs-survival.glitch.me/creators/faq/mailtolink.html"
        self.add_item(discord.ui.Button(label="Support server", url=url))
        self.add_item(discord.ui.Button(label="Mail us", url=url3))
        self.add_item(discord.ui.Button(label="Contact developer", url=url2))  

class InviteView(discord.ui.View):
    def __init__(self):
        super().__init__()    
        url=f"https://discord.com/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands"
        self.add_item(discord.ui.Button(label="Invite", url=url))  

#groups
nitro = SlashCommandGroup("nitro", "nitro users command")
site = SlashCommandGroup("site", "site list command")
privacy = SlashCommandGroup("privacy", "privacy policy command")
report = SlashCommandGroup("report", "report bug command")
about = SlashCommandGroup("about", "about bot command")
@nitro.command(name="users" , description="Get a list of nitro users in your server !")
async def nitrousers(ctx:SlashContext):
         LogIdentifier(ctx , "nitro users")
         guild_id = ctx.guild.id
         if(len(client.get_guild(guild_id).members) > 10000):
          print("```your server has too many members to scan for ie more than thousand fetching nitro users isnt currently available for servers with more than 10000 members```")
          await ctx.respond("Your server has more then 10000 members to use this command please contact RitTheDev#0519")
          return
         guild_new_members = client.get_guild(guild_id).members              
         nitro_users = []          
         for member in guild_new_members:
          try:
           if(str(member.avatar.url).__contains__(".gif")):            
            nitro_users.append(str(member.mention))
            if(len(nitro_users) > 180):          
               await ctx.respond("Hang on ! There are too many people with nitro in this server to fit in a message , Dm RitTheDev#0519 (bot's developer) for the full list !"  ,view = SupportServerView())
               break
          except:
            continue
         nitro_users_new = "".join(str(item) + "\n" for item in nitro_users)  
         embed = discord.Embed()  
         embed.title= "Nitro users"
         embed.description = nitro_users_new               
         embed.color = discord.Color.from_rgb( 117, 255, 255 )     
         if(nitro_users == []):
           await ctx.respond("```We found no users with nitro in this guild ,if you Feel this is an error please type info: report bug to report this issue !```" , view = SupportServerView())        
         else: 
          #await message.reply("`Here is a list of nitro users in your server with thier discord id's - `\n\n" + str(nitro_users_new))         
          await ctx.respond(embed=embed)

@site.command(name="list" , description="Know the sites our bot is available")
async def sitelist(ctx:SlashContext):  
         LogIdentifier(ctx , "site list")
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Site list" 
         embed2.description = "**A list of sites where out bot is available at \n\n• top.gg \n• discord bot list \n• discord bots.gg \n• infinity bot list \n• discord extreme list **\n\nvisit those pages by clicking the buttons below"        
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator}".format(clientname = ctx.author.name , clientdiscriminator = ctx.author.discriminator))
         embed2.color = discord.Color.from_rgb( 117, 255, 255 )
         await ctx.respond(embed=embed2,view = SiteListView())

@privacy.command(name="policy" , description="Privacy, Thats us !!")
async def privacypolicy(ctx:SlashContext):
     LogIdentifier(ctx , "privacy policy")  
     await ctx.respond("```We dont store any user information and log only the guilds joined and commands used by the user and delete the data within few days also we store the data offline ie locally so that no-one can access it or breach into it !! \n\n➤ why we need the data and how we use it \nwe use it to improve user experience and know how the bot is doing with the users \n\n➤ who do we share the data \nwe dont share it to anyone and it is limited to our servers and local copies \n\n➤ how to contact or request to delete your data \nvisit https://ritthedev.itch.io/ and there are various ways listed over there to contact us if we didnt respond any where then , mail us at ritthedevcontact@gmail.com or join our support server and in the #support channel ask @developmentteam to delete your data we will do it within 24 hrs \n\nThank you !```")

@report.command(name="bug" , description="Found a bug? , then please report it")
async def reportbug(ctx:SlashContext):
         LogIdentifier(ctx , "report bug")    
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Report a bug 🛠" 
         embed2.description = "**Reporting bugs would be really great and would improve the bot for many users using it**"        
         embed2.add_field(name="__How to report a bug__" , value = "➤ join our community server and in #bug-reports send ur bug and we will fix it soon and infom you \n➤ visit our sub-reddit page and post your bug \n➤ mail your bug to ✉ ritthedevcontact@gmail.com and we will reply soon \nthank you !!" , inline= False)
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator} ".format(clientname = ctx.author.name , clientdiscriminator = ctx.author.discriminator))
         embed2.color = discord.Color.dark_orange()
         await ctx.respond(embed=embed2  ,view = ReportBugView()) 

@about.command(name="bot" , description="Know about the developers and the bot!")
async def aboutbot(ctx:SlashContext):
        LogIdentifier(ctx , "aboutbot")
        embed = discord.Embed()   
        embed.set_footer(text= "A project by RitTheDev#0519" , icon_url="https://cdn.discordapp.com/avatars/764736831643975693/29372d85837ce1b747e98297a3e00b93.png?size=1024")                 
        embed.title= "About Bot"        
        embed.description = "This bot's core purpose is to get user information from an id , maybe you can do this with other bots but they are very limited ,User information bot is better and dedicated for this purpose with maximum information about a user or server !"
        embed.add_field(name="__Total Users__" , value= str(len(client.users)) +" users !" , inline= True)
        embed.add_field(name="__Total Servers__" , value="Used in " + str(len(client.guilds)) + " servers!" , inline= True)
        embed.add_field(name="__Version__" , value="v2.8" , inline= True)        
        discorduser = await client.fetch_user(888985968554688512)   
        embed.set_thumbnail(url= discorduser.avatar.url)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await ctx.respond(embed = embed,view = AboutView())



client.add_application_command(nitro)
client.add_application_command(site)
client.add_application_command(privacy)
client.add_application_command(report)
client.add_application_command(about)




#Functions
def LogIdentifier(ctx , command):
 print("command_used author: {author} content: {message_} authorid: {authorid} guildid: {guildid} channelid: {channelid} guild name: {guildname} (slash command)".format(author = ctx.author.name , message_ = command,authorid = ctx.author.id , guildid = ctx.guild.id,channelid = ctx.channel.id , guildname = ctx.guild.name))

def BooltoString(Bool):
  if(Bool == True):
    return "Yes"
  else:
    return "No"


def ColorMatcher(Number):
  return ColorDictonary[Number]

async def Userinformation(id , ctx):
       try:
         
          discorduser = await client.fetch_user(id)          
          nitro = False
          member_in_guild = False       
          list_num = 3
          hypesquads = ["brilliance" , "bravery" ,"balance" , "none"]
          if(discorduser.public_flags.hypesquad_brilliance == True): list_num = 0
          if(discorduser.public_flags.hypesquad_bravery == True): list_num = 1
          if(discorduser.public_flags.hypesquad_balance == True): list_num = 2       
          server_member = ""          
          for member in ctx.guild.members:
            if(member.id == discorduser.id):
              server_member = member
          try:          
            if str(discorduser.avatar.url).__contains__(".gif"): nitro = True
          except:
            nitro = False 
          
          mobile =""
          boosting_since = ""
         
         
         


          for mem_id in ctx.guild.members:
               if(mem_id.id == discorduser.id):
                   member_in_guild = True
          try:
           Avatar_url = discorduser.avatar.url
          except:
           Avatar_url = str(discorduser.default_avatar)
          ucc =  discorduser.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
          embed = discord.Embed() 
          embed.title =  "__User Information__"
          embed.description = f"**`User name`** - {discorduser.name}#{discorduser.discriminator} \n**`User id`** - {discorduser.id} \n**`Display/Server name`** - {discorduser.display_name} \n**`Created at`**  - {ucc} \n**`Has nitro`** - {BooltoString(nitro)} \n**`Hypesquad`** - {hypesquads[list_num]} \n**`Mention`** - <@{discorduser.id}>\n**`Is bot?`** - {BooltoString(discorduser.bot)} \n**`Alloted color`** - {str(ColorMatcher(str(discorduser.default_avatar)[41:42]))} \n**`Bug Hunter`** - {BooltoString(discorduser.public_flags.bug_hunter)} \n**`Early supporter`** - {BooltoString(discorduser.public_flags.early_supporter)} \n**`Early verified bot developer`** - {BooltoString(discorduser.public_flags.early_verified_bot_developer)} \n**`In this server`** - {BooltoString(member_in_guild)}  \n**`Avatar url`** - {Avatar_url}"               
          try:
           embed.set_thumbnail(url=discorduser.avatar.url)
          except:
            embed.set_thumbnail(url=discorduser.default_avatar)
          embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = ctx.author.name , clientdiscriminator = ctx.author.discriminator))          
          if(member_in_guild == True):                     
           if(server_member.is_on_mobile()): mobile = "yes" 
           else: mobile = "Not using mobile currently"
           if(server_member.premium_since == None): boosting_since = "Not boosting this server"
           else: boosting_since = server_member.premium_since
           embed.add_field(name="__In Guild Information__" ,value="**`Join date`** - {date} \n**`Activity`** - {activity} \n**`Status`** - {status} \n**`Nick name`** - {nick} \n**`Boosting server`** - {boosting_since} \n**`On mobile`** - {mobile} \n**`Top role`** - {top_role}".format(date = server_member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p") , activity = server_member.activity ,status = server_member.desktop_status , nick = server_member.nick , mobile = mobile   , boosting_since = boosting_since , top_role = server_member.top_role) , inline= False)
          #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: id help` to know how to get a users or server id")
          #embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          return embed
       except Exception as err:
          await ctx.reply("```⚠ An error has occured make sure you entered the bots command right and the id correctly or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs Error Code - {err} ⚠ ```".format(err = err), view = SupportView())
          pass

async def GuildInformation(g_id,ctx):
        guild_new = await client.fetch_guild(g_id)
        #print("Running 1")
        #for bot_count_mem in client.get_guild(g_id).members:
         # if bot_count_mem.bot:
          #  bot_count = bot_count + 1
        guild_desciption = guild_new.description
        guild_made_at = guild_new.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
        owner = guild_new.owner_id      
        boost_tier = guild_new.premium_tier        
        #member_count = client.get_guild(g_id).member_count   
        #subscribers = 0 #len(client.get_guild(g_id).premium_subscribers) 
        #for member in client.get_guild(g_id):
          #member_count += 1
        security_level= "none"
        security_level_num = guild_new.mfa_level
        security_levels = ["low" , "medium" , "high" , "highest"]      
        security_level = security_levels[security_level_num]

          


        embed = discord.Embed() 
        embed.title =  "__Guild Information__"
        text_channel_list = []
        categories_count =[]
        member_count = 0
        bot_count =0 
        for server in client.guilds:          
          if(server.id == guild_new.id):
           for member in server.members:
                member_count = member_count + 1
                if member.bot == True:
                 bot_count = bot_count + 1
           for category in server.categories:
             categories_count.append(category)
           for channel in server.channels:
            if str(channel.type) == 'text':
             text_channel_list.append(channel)
        #print("Running 1")
        try:
         embed.set_thumbnail(url=guild_new.icon.url)
        except:
          pass

        ucc =  guild_new.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
        embed.description = "**`Guild name -`** {name} \n **`Guild description -`** \n{desc} \n **`Member count -`** {mem_count} \n**`Bots -`** {bot_count} \n **`Created at -`** {ucc_} \n**`Owner id -`** {owner} \n**`Boost level -`** {boosters} \n**`Security level -`** {sec_level} \n**`Roles -`** {Rolecount}\n**`Text channels -`** {tcc}\n**`Categories -`** {cc}\n**`NSFW level -`** {NSFW_level} ".format(
          name = guild_new , desc = guild_desciption , mem_count = member_count , created_at = guild_made_at
           ,owner = owner , boosters = boost_tier , sec_level = security_level ,
           bot_count = bot_count , Rolecount = len(guild_new.roles) , NSFW_level = guild_new.nsfw_level , cc = len(categories_count) , tcc = len(text_channel_list) , ucc_ = ucc
          )
        #embed.description = "name - {name}".format(name = guild_new.name)
        embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = ctx.author.name , clientdiscriminator = ctx.author.discriminator))
        #embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
        #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: how to guild id` to know how to get a users or guilds id")
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        return embed        
    #except Exception as err:
           #await ctx.respond("```⚠ An error has occured most probably as the bot couldnt access the server we will fix this issue soon type info: report bug and report this issue error code: {error_code} ⚠ ```".format(error_code = err) , view = SupportView())   
           #return                                                                

#Slash commands   
@client.slash_command(name="help" , description="Get a list of all commands and how to use the bot")
async def help(ctx:SlashContext):
        LogIdentifier(ctx , "help")
        embed = discord.Embed()           
        embed.title= "Information help"
        embed.description = "**• Type `info: userid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/) **"
        embed.add_field(name="__Main commands__" , value="`help` , `example` , `info: id`  , `info: guildid` ,`how to get id`,`autoinfo` , `support`,`this` ,`thisg` ,`invite`,`about bot` " , inline= False)
        embed.add_field(name="__Other commands__" , value="`ping` , `vote` , `info: id help` , `nitro users`, `site list` , `privacy policy` , `report bug` , `who made you` , `updates`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await ctx.respond(embed=embed , view = HelpCommandView())  

@client.slash_command(name="ping" , description="Know the bot's latency !")
async def ping(ctx:SlashContext):
        LogIdentifier(ctx , "ping")
        await ctx.respond(f'latency ping is {round (client.latency * 1000)} ms')        

@client.slash_command(name="example" , description="View an example image to know how to use the bot.")
async def example(ctx:SlashContext):
        LogIdentifier(ctx , "example")
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png")
        embed.color = discord.Color.purple()
        await ctx.respond(embed=embed) 

@client.slash_command(name="idhelp" , description="Know about using the bot for a user and server")
async def id_help(ctx:SlashContext):
          LogIdentifier(ctx , "id")
          embed = discord.Embed()
          embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = ctx.author.name , clientdiscriminator = ctx.author.discriminator))
          embed.add_field(name="__User id__" ,value="type `info: how to get id` to get someones discord id and type `info: (paste the id here)` to get a users information" , inline= False) 
          embed.add_field(name="__Server id__" ,value="using similar process after turning on developer mode right click on the server icon and click copy id and type `info: (paste the id here)` to get a servers information note:- due to discord API policies we can retrive information from the servers if the bot is in that server" , inline= False) 
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          await ctx.respond(embed = embed ,view = IdHelpView())

@client.slash_command(name="howtogetid" , description="Know how to copy as user/server id")
async def how_to_get_id(ctx:SlashContext):
        LogIdentifier(ctx , "how to get id")
        embed = discord.Embed()  
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/890899791574347786/bn.png")
        embed.color = discord.Color.purple()
        await ctx.respond(embed = embed) 

@client.slash_command(name="support" , description="Need help? Dont worry We got you ")
async def support(ctx:SlashContext):
        LogIdentifier(ctx , "support")
        await ctx.respond("if there are any issues with the bot \n \n`possible fixes -` \n➤ make sure you entered the command's syntax right. \n➤ try info: help or info: example. \n➤ make sure you gave the bot permissions to embed,message and etc. \n➤ join the support server and in the #support ask for help or report this and we will help you within 24hrs of time. \n➤ if nothing works contact us at ritthedevcontact@gmail.com ." , view = SupportView() )

@client.slash_command(name="this" , description="Know information about yourself")
async def this(ctx:SlashContext):
        LogIdentifier(ctx , "this")
        await ctx.respond(embed = await Userinformation(ctx.author.id , ctx)) 

@client.slash_command(name="thisg" , description="Know information about the guild you used the commmand in")
async def thisg(ctx:SlashContext):
        await ctx.respond(embed = await GuildInformation(ctx.guild.id , ctx)) 

@client.slash_command(name="info" , description="Get information about a user or guild")
async def information(
    ctx: discord.ApplicationContext,
    id: Option(str, "Enter the guild or server id , or mention a user."),
    #gender: Option(str, "Choose your gender", choices=["Male", "Female", "Other"]),
    #age: Option(int, "Enter your age", min_value=1, max_value=99, default=18)
):
   LogIdentifier(ctx , "info command {id}".format(id=id))
   used_guild_command = True
   try:
     try:  
      try:  
       if id.index("@") == 1:                      
         await client.fetch_user(int(id[3:-1]))
         id_new = id[3:-1]
         used_guild_command = False   
      except:
        await client.fetch_user(int(id))
        used_guild_command = False    
        id_new = id 
     except:
      await client.fetch_guild(int(id))
      used_guild_command = True
   except Exception as err:
          await ctx.respond("```⚠ An error has occured make sure you entered the bots command right and the id correctly or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs Error Code - {err} ⚠ ```".format(err = err),view = SupportView())
          return
   
   if(used_guild_command == False):
     await ctx.respond(embed = await Userinformation(id_new,ctx)) 
   try:
    if(used_guild_command == True):
     await ctx.respond(embed = await GuildInformation(id , ctx))
   except Exception as err:
           await ctx.respond("```⚠ An error has occured most probably as the bot couldnt access the server we will fix this issue soon type info: report bug and report this issue error code: {error_code} ⚠ ```".format(error_code = err) , view = SupportView())   
           pass  


@client.slash_command(name="vote" , description="Support us by vote for the bot ,its free !!")
async def vote(ctx:SlashContext):
         LogIdentifier(ctx , "about bot")
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Vote for the bot" 
         embed2.description = "**Voting the bot would be really great and you can support our development this way, thanks a lot if you have voted \n\n• [Top.gg](https://top.gg/bot/888985968554688512) \n• [Discord bot list](https://discordbotlist.com/bots/discord-user-info-bot/upvote) ** \n\nclick the buttons below to visit the pages :))"        
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator}".format(clientname = ctx.author.name , clientdiscriminator = ctx.author.discriminator))
         embed2.color = discord.Color.green()
         await ctx.respond(embed=embed2 ,view = VoteView()) 

@client.slash_command(name="whomadeyou" , description="Know about the developers!")
async def whomadeyou(ctx:SlashContext):
     LogIdentifier(ctx , "who made you")
     if(ctx.author.id == 764736831643975693):
       await ctx.respond("you made me and  asking me who made you how dumb lol")
     else:
      await ctx.respond("**RitTheDev#0519** made me and {author_name} you are most welcomed join our community server :)".format(author_name = ctx.author.name), view =  AboutView())              


@client.slash_command(name="updates" , description="View the recent update the bot has recieved")
async def updates(ctx:SlashContext): 
   LogIdentifier(ctx , "updates") 
   await ctx.respond("```md\nUser information bot v2.8 (Update)\n\n#New\n-  Added addtional information like Bug hunter , Early supporter , and Early verified bot developer\n\n#Changes \n- Make some minor UI changes \n-  Changed True/false system to Yes/No \n\n#bug fixes \n-  Fixed date system in few places.```", view = SupportServerView())



@client.slash_command(name="invite" , description="Invite me into another server !!")
async def invite(ctx:SlashContext):
         LogIdentifier(ctx , "invite")    
         await ctx.respond( " ` Click the invite button to add me into your server !!! ` " , view = InviteView())   
      
      
''' 
Archieve slash commands

@client.slash_command(name="id" , description="Enter parameter instead of /id")
async def id(ctx:SlashContext):
        LogIdentifier(ctx , "id")
        await ctx.respond("```Please enter the id of the user instead of the word 'ID' the input should look something like info: 764736831643975693 & type info: example for more information```") 
@client.slash_command(name="guildid" , description="Enter parameter instead of /guildid")
async def guild_id(ctx:SlashContext):
          LogIdentifier(ctx , "guildid")
          await ctx.respond("```Please enter the id of the guild instead of the word 'guildid' the input should look something like info: 834089778215125002 & type info: example for more information```")  

@client.slash_command(name="nitrousers" , description="Get a list of nitro users in your server !")
async def nitrousers(ctx:SlashContext):
         LogIdentifier(ctx , "nitro users")
         guild_id = ctx.guild.id
         if(len(client.get_guild(guild_id).members) > 10000):
          print("```your server has too many members to scan for ie more than thousand fetching nitro users isnt currently available for servers with more than 10000 members```")
          await ctx.respond("Your server has more then 10000 members to use this command please contact RitTheDev#0519")
          return
         guild_new_members = client.get_guild(guild_id).members              
         nitro_users = []          
         for member in guild_new_members:
          try:
           if(str(member.avatar.url).__contains__(".gif")):            
            nitro_users.append(str(member.mention))
            if(len(nitro_users) > 180):          
               await ctx.respond("Hang on ! There are too many people with nitro in this server to fit in a message , Dm RitTheDev#0519 (bot's developer) for the full list !"  ,view = SupportServerView())
               break
          except:
            continue
         print("Running")
         nitro_users_new = "".join(str(item) + "\n" for item in nitro_users)  
         embed = discord.Embed()  
         embed.title= "Nitro users"
         embed.description = nitro_users_new               
         embed.color = discord.Color.from_rgb( 117, 255, 255 )     
         if(nitro_users == []):
           await ctx.respond("```We found no users with nitro in this guild ,if you Feel this is an error please type info: report bug to report this issue !```" , view = SupportServerView())        
         else: 
          #await message.reply("`Here is a list of nitro users in your server with thier discord id's - `\n\n" + str(nitro_users_new))         
          await ctx.respond(embed=embed)

'''

    

#Events
@client.event
async def on_ready():
    print('On ready: We have logged in as {0.user}'.format(client))    
    await client.change_presence(status=discord.Status.online , activity = discord.Activity(type=discord.ActivityType.watching, name="info: help | on {users} users !".format(users = len(client.users))))
    #for guild_id in client.guilds:  guild_ids.append(guild_id.id)    

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
         [[Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW") , 
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

 if message.author == client.user:
        return
 try:  
  if(str(message.guild.id) in no_autoresponse_guilds):
    print("Didnt run automated information as owner prefered not to")
    pass
  else:
   if(len(message.content) == 18 and int(message.content)):
     try:
          print("Used automated information !! author: {author} content: {message_} authorid: {authorid} guildid: {guildid} channelid: {channelid} guild name: {guildname}".format(author = message.author.name , message_ = message.content,authorid = message.author.id , guildid =message.guild.id,channelid = message.channel.id , guildname = message.guild.name))          
          await message.reply(embed = await Userinformation(message.content , message))
     except Exception as Err:
      print(Err)
 except Exception as Err:
  pass
 try:  
  if(message.content.startswith("info:")):         
    print("command_used author: {author} content: {message_} authorid: {authorid} guildid: {guildid} channelid: {channelid} guild name: {guildname}".format(author = message.author.name , message_ = message.content,authorid = message.author.id , guildid =message.guild.id,channelid = message.channel.id , guildname = message.guild.name))
    used_guild_command = True
    used_main_command = True
    con_mes = message.content 
    if message.author == client.user:
        return    
    
    
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
       #await message.reply("```⚠ a_n error has occured make sure you entered the bots command right or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs ⚠ ```" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.com/invite/gzaz9SSkkW") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
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
          try:          
            if str(discorduser.avatar.url).__contains__(".gif"): nitro = True
          except:
            nitro = False 
          
          mobile =""
          boosting_since = ""

          for mem_id in message.guild.members:
               if(mem_id.id == discorduser.id):
                   member_in_guild = True
          try:
           Avatar_url = discorduser.avatar.url
          except:
           Avatar_url = str(discorduser.default_avatar)
          
          embed = discord.Embed() 
          embed.title =  "__User Information__"
          ucc =  discorduser.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
          #NoSpaces embed.description = f"**`User name`** {discorduser.name}#{discorduser.discriminator} \n**`User id`**{discorduser.id} \n**`Display/Server name`** {discorduser.display_name} \n**`Created at-`** {ucc} \n**`Has nitro`** {nitro} \n**`Hypesquad`** {hypesquads[list_num]} \n**`Mention`** <@{discorduser.id}>\n**`Is bot?`** {discorduser.bot} \n**`Alloted color`** {str(ColorMatcher(str(discorduser.default_avatar)[41:42]))} \n**`Bug Hunter`** {discorduser.public_flags.bug_hunter} \n**`Early supporter`** {discorduser.public_flags.early_supporter} \n**`Early verified bot developer`** {discorduser.public_flags.early_verified_bot_developer} \n**`In this server`** {member_in_guild}  \n**`Avatar url`** {Avatar_url}"               
          #OnlyDashes (outside)
          embed.description = f"**`User name`** - {discorduser.name}#{discorduser.discriminator} \n**`User id`** - {discorduser.id} \n**`Display/Server name`** - {discorduser.display_name} \n**`Created at`**  - {ucc} \n**`Has nitro`** - {BooltoString(nitro)} \n**`Hypesquad`** - {hypesquads[list_num]} \n**`Mention`** - <@{discorduser.id}>\n**`Is bot?`** - {BooltoString(discorduser.bot)} \n**`Alloted color`** - {str(ColorMatcher(str(discorduser.default_avatar)[41:42]))} \n**`Bug Hunter`** - {BooltoString(discorduser.public_flags.bug_hunter)} \n**`Early supporter`** - {BooltoString(discorduser.public_flags.early_supporter)} \n**`Early verified bot developer`** - {BooltoString(discorduser.public_flags.early_verified_bot_developer)} \n**`In this server`** - {BooltoString(member_in_guild)}  \n**`Avatar url`** - {Avatar_url}"               
          #OnlyDashes (inside)
          #embed.description = f"**`User name -`** {discorduser.name}#{discorduser.discriminator} \n**`User id -`**{discorduser.id} \n**`Display/Server name -`** {discorduser.display_name} \n**`Created at -`** {ucc} \n**`Has nitro -`** {nitro} \n**`Hypesquad -`** {hypesquads[list_num]} \n**`Mention -`** <@{discorduser.id}>\n**`Is bot? -`** {BooltoString(discorduser.bot)} \n**`Alloted color -`** {str(ColorMatcher(str(discorduser.default_avatar)[41:42]))} \n**`Bug Hunter -`** {BooltoString(discorduser.public_flags.bug_hunter)} \n**`Early supporter -`** {BooltoString(discorduser.public_flags.early_supporter)} \n**`Early verified bot developer -`** {BooltoString(discorduser.public_flags.early_verified_bot_developer)} \n**`In this server -`** {member_in_guild}  \n**`Avatar url -`** {Avatar_url}"               
          
          try:
           embed.set_thumbnail(url=discorduser.avatar.url)
          except:            
            embed.set_thumbnail(url=discorduser.default_avatar)
          embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))          
          if(member_in_guild == True):                     
           if(server_member.is_on_mobile()): mobile = "yes" 
           else: mobile = "Not using mobile currently"
           if(server_member.premium_since == None): boosting_since = "Not boosting this server"
           else: boosting_since = server_member.premium_since
           embed.add_field(name="__In Guild Information__" ,value="**`Join date`** - {date} \n**`Activity`** - {activity} \n**`Status`** - {status} \n**`Nick name`** - {nick} \n**`Boosting server`** - {boosting_since} \n**`On mobile`** - {mobile} \n**`Top role`** - {top_role}".format(date = server_member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p") , activity = server_member.activity ,status = server_member.desktop_status , nick = server_member.nick , mobile = mobile   , boosting_since = boosting_since , top_role = server_member.top_role) , inline= False)
          #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: id help` to know how to get a users or server id")
          #embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          
          await message.reply(embed = embed)
        except Exception as err:
          await message.reply("```⚠ An error has occured make sure you entered the bots command right and the id correctly or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs Error Code - {err} ⚠ ```".format(err = err), components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.com/invite/gzaz9SSkkW") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
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
        guild_made_at = guild_new.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
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

        text_channel_list = []
        categories_count =[]
        for server in client.guilds:
          if(server.id == guild_new.id):
           for category in server.categories:
             categories_count.append(category)
           for channel in server.channels:
            if str(channel.type) == 'text':
             text_channel_list.append(channel)

        try:
         embed.set_thumbnail(url=guild_new.icon.url)
        except:
          pass
        embed.description = "**`Guild name -`** {name} \n **`Guild description -`** \n{desc} \n **`Member count -`** {mem_count} \n**`Bots -`** {bot_count} \n **`Created at -`** {created_at} \n**`Owner id -`** {owner} \n**`Boost level -`** {boosters} \n**`Security level -`** {sec_level} \n**`Boosters -`** {subs}\n**`Roles -`** {Rolecount}\n**`Text channels -`** {tcc}\n**`Categories -`** {cc}\n**`NSFW level -`** {NSFW_level} ".format(
          name = guild_new , desc = guild_desciption , mem_count = member_count , created_at = guild_made_at
           ,owner = owner , boosters = boost_tier , sec_level = security_level , subs = subscribers , 
           bot_count = bot_count , Rolecount = len(guild_new.roles), NSFW_level = guild_new.nsfw_level , cc = len(categories_count) , tcc = len(text_channel_list)
          )
        #embed.description = "name - {name}".format(name = guild_new.name)
        embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))
        #embed.add_field(name="__Note__" ,value="🛠 this is currently the beta version of the bot soon all the features will be released. 🛠")
        #embed.add_field(name="__Tips__" ,value="pro tip - type `info: how to get id` or `info: how to guild id` to know how to get a users or guilds id")
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
 
        await message.reply(embed = embed)
        
       except Exception as err:
           await message.reply("```⚠ An error has occured most probably as the bot couldnt access the server we will fix this issue soon type info: report bug and report this issue error code: {error_code} ⚠ ```".format(error_code = err) , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.com/invite/gzaz9SSkkW")]])
   
    if (message.content.startswith("info: ping")):
         await message.reply(f'latency ping is {round (client.latency * 1000)} ms')

    if (message.content.startswith("info: example")):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png")
        embed.color = discord.Color.purple()
        await message.reply(embed = embed)

    if (message.content.startswith("info: invite")):
        await message.reply( " ` click the invite button to add me into your server !!! ` " , 
           components = [
           [Button(style=ButtonStyle.URL, label="invite", url="https://discord.com/oauth2/authorize?client_id=888985968554688512&permissions=518822285025&scope=bot%20applications.commands") , Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW")]
           ])
    if (message.content.startswith("info: updates")):     
        await message.reply("```md\nUser information bot v2.8 (Update)\n\n#New\n-  Added addtional information like Bug hunter , Early supporter , and Early verified bot developer\n\n#Changes \n- Make some minor UI changes \n-  Changed True/false system to Yes/No \n\n#bug fixes \n-  Fixed date system in few places.```" , components = [
           [Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW")]
           ]) 
    
    if (message.content.startswith("info: support")):
          await message.reply("if there are any issues with the bot \n \n`possible fixes -` \n➤ make sure you entered the command's syntax right. \n➤ try info: help or info: example. \n➤ make sure you gave the bot permissions to embed,message and etc. \n➤ join the support server and in the #support ask for help or report this and we will help you within 24hrs of time. \n➤ if nothing works contact us at ritthedevcontact@gmail.com ." , components = [
           [Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW") ,  Button(style=ButtonStyle.URL, label="Example", url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png")]
           ])       
    if (message.content.startswith("info: nitro users")):                
         guild_id = message.guild.id
         if(len(client.get_guild(guild_id).members) > 10000):
          print("```your server has too many members to scan for ie more than thousand fetching nitro users isnt currently available for servers with more than 10000 members```")
          await message.reply("Your server has more then 10000 members to use this command please contact RitTheDev#0519")
          return
         guild_new_members = client.get_guild(guild_id).members              
         nitro_users = []          
         for member in guild_new_members:
          try:
           if(str(member.avatar.url).__contains__(".gif")):            
            nitro_users.append(str(member.mention))
            if(len(nitro_users) > 180):          
               await message.reply("Hang on ! There are too many people with nitro in this server to fit in a message , Dm RitTheDev#0519 (bot's developer) for the full list !"  , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.com/invite/gzaz9SSkkW")]])
               break
          except:
            continue
         nitro_users_new = "".join(str(item) + "\n" for item in nitro_users)  
         embed = discord.Embed()  
         embed.title= "Nitro users"
         embed.description = nitro_users_new               
         embed.color = discord.Color.from_rgb( 117, 255, 255 )     
         if(nitro_users == []):
           await message.reply("```We found no users with nitro in this guild ,if you Feel this is an error please type info: report bug to report this issue !```" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.com/invite/gzaz9SSkkW")]])        
         else: 
          #await message.reply("`Here is a list of nitro users in your server with thier discord id's - `\n\n" + str(nitro_users_new))         
          await message.reply(embed=embed)

          
    if(message.content == "info: help"):
        embed = discord.Embed()   
        embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))                          
        embed.title= "Information help"
        embed.description = "**• Type `info: userid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/) **"
        embed.add_field(name="__Main commands__" , value="`help` , `example` , `info: id`  , `info: guildid` ,`how to get id`,`autoinfo` , `support` ,`this` , `thisg` ,`invite` " , inline= False)
        embed.add_field(name="__Other commands__" , value="`ping` , `vote` , `info: id help` , `nitro users`, `site list` , `privacy policy` , `report bug` , `who made you` , `updates`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed, components = 
        [[Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW") , 
         Button(style=ButtonStyle.URL, label="Example", url="https://cdn.discordapp.com/attachments/890895848773419038/896350154406363156/unknown.png"),
         Button(style=ButtonStyle.URL, label="Vote for us", url="https://top.gg/bot/888985968554688512/vote")
         ]])     
    if(message.content.startswith("info: server count")):
      if str(message.author.id) == str(764736831643975693) or str(message.author.id) == str(859281032103329812):
        await message.reply("I'm used in "+ str(len(client.guilds)) +" servers!")
      else:
        await message.reply("We moved this command to `info: about bot`")
         
    if(message.content.startswith("info: about bot")):
        embed = discord.Embed()   
        embed.set_footer(text= "A project by RitTheDev#0519".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator) , icon_url="https://cdn.discordapp.com/avatars/764736831643975693/29372d85837ce1b747e98297a3e00b93.png?size=1024")                 
        embed.title= "About Bot"        
        embed.description = "This bot's core purpose is to get user information from an id , maybe you can do this with other bots but they are very limited ,User information bot is better and dedicated for this purpose with maximum information about a user or server !"
        embed.add_field(name="__Total Users__" , value= str(len(client.users)) +" users !" , inline= True)
        embed.add_field(name="__Total Servers__" , value="Used in " + str(len(client.guilds)) + " servers!" , inline= True)
        embed.add_field(name="__Version__" , value="v2.8" , inline= True)        
        discorduser = await client.fetch_user(888985968554688512)   
        embed.set_thumbnail(url= discorduser.avatar.url)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed, components = 
        [[Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW") , 
         Button(style=ButtonStyle.URL, label="Developer portfolio", url="https://ritthedev.itch.io/"),         
         ]])     
    if(message.content.startswith("info: autoinfo")):
         embed2 = discord.Embed()    
         embed2.title =  "Automated information" 
         embed2.description = "Enter a id and send that message without the bots syntax and the bot will respond to you , note this feature will work only till **[April30](http://alecs-survival.glitch.me/creators/faq/slashcommandsnotice.html)** \n You can toggle this off to your server by joining our support server and requesting for toggle off."        
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))
         embed2.color = discord.Color.green()
         await message.channel.send(embed=embed2 , components =[[Button(style=ButtonStyle.URL , label="Support server" , url =  "https://discord.com/invite/gzaz9SSkkW"), 
          Button(style=ButtonStyle.URL , label="Example" , url =  "https://cdn.discordapp.com/attachments/890895848773419038/936803394843189248/unknown.png"), 
          ]])
         
    if(message.content.startswith("info: vote")):
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Vote for the bot" 
         embed2.description = "**Voting the bot would be really great and you can support our development this way, thanks a lot if you have voted \n\n• [Top.gg](https://top.gg/bot/888985968554688512) \n• [Discord bot list](https://discordbotlist.com/bots/discord-user-info-bot/upvote) ** \n\nclick the buttons below to visit the pages :))"        
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))
         embed2.color = discord.Color.green()
         await message.channel.send(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Top.gg" , url =  "https://top.gg/bot/888985968554688512") ,
           Button(style=ButtonStyle.URL , label="Discord bot list" , url =  "https://discordbotlist.com/bots/discord-user-info-bot") ,           
           ]]) 

    if(message.content.startswith("info: site list")):   
         embed2 = discord.Embed()    
         embed2.title =  " <:emoji:890928633206677505> Site list" 
         embed2.description = "**A list of sites where out bot is available at \n\n• top.gg \n• discord bot list \n• discord bots.gg \n• infinity bot list \n• discord extreme list **\n\nvisit those pages by clicking the buttons below"        
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator}".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))
         embed2.color = discord.Color.from_rgb( 117, 255, 255 )
         await message.reply(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Top.gg" , url =  "https://top.gg/bot/888985968554688512") ,
           Button(style=ButtonStyle.URL , label="Discord bot list" , url =  "https://discordbotlist.com/bots/discord-user-info-bot") ,
           Button(style=ButtonStyle.URL , label="Infinity bot list" , url =  "https://infinitybotlist.com/bots/888985968554688512/")] ,[
           Button(style=ButtonStyle.URL , label="Fateslist.xyz" , url =  "https://fateslist.xyz/bot/888985968554688512") ,           
           Button(style=ButtonStyle.URL , label="Discord extreme list" , url =  "https://discordextremelist.xyz/en-US/bots/888985968554688512"),
           Button(style=ButtonStyle.URL , label="Our website" , url =  "https://discord-user-info-client.glitch.me/")
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
         embed2.set_footer(text= "Requested by {clientname}#{clientdiscriminator} ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))
         embed2.color = discord.Color.dark_orange()
         await message.channel.send(embed=embed2 , components = [[
           Button(style=ButtonStyle.URL , label="Discord server" , url =  "https://discord.com/invite/gzaz9SSkkW") ,
           Button(style=ButtonStyle.URL , label="Sub-reddit" , url =  "https://www.reddit.com/r/ritthedev_community/") , 
           Button(style=ButtonStyle.URL , label="Mail us" , url =  "https://mail.google.com/mail/u/0/#inbox?compose=new")                     
           ]])      

    if message.content == "info: id help":
          embed = discord.Embed()
          embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))
          embed.add_field(name="__User id__" ,value="type `info: how to get id` to get someones discord id and type `info: (paste the id here)` to get a users information" , inline= False) 
          embed.add_field(name="__Server id__" ,value="using similar process after turning on developer mode right click on the server icon and click copy id and type `info: (paste the id here)` to get a servers information note:- due to discord API policies we can retrive information from the servers if the bot is in that server" , inline= False) 
          embed.color = discord.Color.from_rgb( 117, 255, 255 )
          await message.reply(embed = embed ,components = [
            [Button(style= ButtonStyle.URL , label="user example" , url ="https://cdn.discordapp.com/attachments/890895848773419038/896286726010568724/unknown.png"),
            Button(style= ButtonStyle.URL , label="server example" , url ="https://cdn.discordapp.com/attachments/890895848773419038/896286468887167026/unknown.png"),
            Button(style= ButtonStyle.URL , label="Support server" , url ="https://discord.com/invite/gzaz9SSkkW")
            ]])
     
    if(message.content == "info: id"):
     await message.reply("```Please enter the id of the user instead of the word 'ID' the input should look something like info: 764736831643975693 & type info: example for more information```") 
    if(message.content == "info: guildid"):
     await message.reply("```Please enter the id of the guild instead of the word 'guildid' the input should look something like info: 834089778215125002 & type info: example for more information```")   
    if(message.content == "info: userid"):
      await message.reply("```Please enter the id of the user instead of the word 'userid' the input should look something like info: 764736831643975693 & type info: example for more information```") 

    if(message.content.startswith("info:help")):
     await message.reply("it's `info: help` ,dont forget the space bud !!")
      
    if(message.content.startswith("info: who made you")):
     if(message.author.id == 764736831643975693):
       await message.reply("you made me and  asking me who made you how dumb lol")
     else:
      await message.reply("**RitTheDev#0519** made me and {author_name} you are most welcomed join our community server :)".format(author_name = message.author.name) , components = [[ Button(style=ButtonStyle.URL, label="Support server", url="https://discord.com/invite/gzaz9SSkkW" ), Button(style=ButtonStyle.URL, label="Join Sub-reddit", url="https://www.reddit.com/r/ritthedev_community/" ), Button(style=ButtonStyle.URL, label="View our projects", url="https://ritthedev.itch.io")]])  
 except Exception as err:
   try:
     print(int(con_mes[5:None]))
   except Exception as err:
    await message.reply("```⚠ An error has occured make sure you entered the bots command right or try info: support or info: example , if nothing works try joining our support server and we will help you within 24hrs ⚠```" , components = [[Button(style=ButtonStyle.URL , label ="Support server" , url="https://discord.com/invite/gzaz9SSkkW") , Button(style= ButtonStyle.URL  , label= "View example" , url= "https://cdn.discordapp.com/attachments/890895848773419038/890895864053235722/unknown.png")]])
    print(err)
    pass


client.run(token)



''' old code  
#loading cogs and extintions
os.chdir(os.getcwd())
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
    Leave code
    if message.content.startswith("info: leave") and message.author.id == 764736831643975693:
      to_leave = client.get_guild(int(con_mes[12:None])) 
      print("left"+ " , " + str(to_leave.name) + " , " + str(len(client.guilds)) )
      await to_leave.leave()
      #print(int(con_mes[12:None]))
      

      #print("hello")
    for i in client.guilds:
      print(i.owner.id)

    for i in client.guilds:
     print(i.id)


    
           bot_count_new = 0  for bot_count_mem in client.get_guild(i.id).members:
      if bot_count_mem.bot:
        bot_count_new = bot_count_new + 1 
     #print(str(i.member_count) + "," + str(bot_count_new))

    for i in range(0,160):      
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
           i = i + 1 
     
    if(message.content.startswith("info: help")):
        
        embed = discord.Embed()   
        embed.set_footer(text= "Requested by {clientname}#{clientdiscriminator} | Hope you have a great time using the bot :)  ".format(clientname = message.author.name , clientdiscriminator = message.author.discriminator))                 
        embed.title= "Information help"
        embed.description = "**• Type `info: userid` to get the information of the user \n• Type `info: example ` to view a image of how to use me. \n• I was developed by [RitTheDev#0519](https://ritthedev.itch.io/)**"
        embed.add_field(name="__Main commands__" , value="`help` , `example` , `info: id`  , `info: guild-id` ,`how to get id` , `support`" , inline= False)
        embed.add_field(name="__Other commands__" , value="`ping` , `vote` , `info: id help` , `nitro users`, `site list` , `privacy policy` , `report bug` , `who made you` , `updates`" , inline= False)
        embed.add_field(name="__Syntax__" , value="**`info:` is my syntax**" , inline=False)
        #embed.add_field(name="__Note__" , value= "🛠this is currently the beta version of the bot soon all the features will be released join the support server to be updated.🛠" , inline= False)
        embed.color = discord.Color.from_rgb( 117, 255, 255 )
        await message.reply(embed = embed) 

'''