# main.py — optimized for low RAM (Discloud-friendly) with /about group

import os
import asyncio
from aiohttp import web
from dotenv import load_dotenv
import discord
from discord.ui import View, Button
from discord.commands import SlashCommandGroup

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("Missing DISCORD_TOKEN in environment")

# -------------------------------
#   INTENTS + LOW RAM SETTINGS
# -------------------------------

intents = discord.Intents.none()  # absolutely minimum RAM
intents.guilds = True             # required for slash commands
intents.members = False           # no member cache
intents.presences = False         # no presence events
intents.messages = False          # no message events

bot = discord.Bot(
    intents=intents,
    member_cache_flags=discord.MemberCacheFlags.none(),
    chunk_guilds_at_startup=False,   # <<<< MOST IMPORTANT
)

# Disable message cache entirely
bot._connection.max_messages = 0
# -------------------------------
#   CONSTANTS / GLOBALS
# -------------------------------
banned_users = []  # your original placeholder
NO_AUTORESPONSE_GUILDS = set()
COLOR_DICTIONARY = {
    "0": "Blue", "1": "Grey", "2": "Green",
    "3": "Yellow", "4": "Red", "5": "Pink"
}

# -------------------------------
#   SMALL HELPERS
# -------------------------------

def LogIdentifier(ctx, tag: str):
    """Lightweight logging helper so commands can annotate actions without heavy state."""
    try:
        guild_part = f"guild={ctx.guild.id}" if getattr(ctx, "guild", None) else "DM"
        print(f"[{tag}] author={ctx.author} ({ctx.author.id}) {guild_part}")
    except Exception:
        print(f"[{tag}] (log failed)")

def bool_to_yesno(b):
    return "Yes" if b else "No"

def color_matcher(x):
    return COLOR_DICTIONARY.get(x, "Unknown")

# -------------------------------
#   BUTTON VIEWS
# -------------------------------

class SupportView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="Support server", url="https://discord.com/invite/gzaz9SSkkW"))
        self.add_item(Button(label="Example", url="https://cdn.discordapp.com/attachments/912924429057675274/949286662360403978/unknown.png"))

class InviteView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="Invite", url="https://discord.com/oauth2/authorize?client_id=888985968554688512&permissions=414464867393&scope=bot%20applications.commands"))

class AboutView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        url = "https://discord.com/invite/gzaz9SSkkW"
        url2 = "https://ritthedev.itch.io/"
        self.add_item(discord.ui.Button(label="Support server", url=url))
        self.add_item(discord.ui.Button(label="Developer portfolio", url=url2))

# -------------------------------
#   USER EMBED (low RAM version)
# -------------------------------

async def build_user_embed(user: discord.User, guild: discord.Guild | None, mention_mode: bool):
    # nitro detection
    nitro = False
    try:
        if user.avatar and user.avatar.is_animated():
            nitro = True
    except:
        nitro = False

    created_str = user.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

    # Hypesquad logic
    hypesquads = ["brilliance", "bravery", "balance", "none"]
    list_num = 3
    try:
        pf = user.public_flags
        if getattr(pf, "hypesquad_brilliance", False): list_num = 0
        if getattr(pf, "hypesquad_bravery", False): list_num = 1
        if getattr(pf, "hypesquad_balance", False): list_num = 2
    except:
        pass

    # Fetch single member only when needed
    server_member = None
    if guild:
        try:
            server_member = await guild.fetch_member(user.id)
        except:
            server_member = None

    embed = discord.Embed(
        title="User Information",
        color=discord.Color.from_rgb(117, 255, 255)
    )

    embed.description = (
        f"**`User name`** - {user.name}#{user.discriminator}\n"
        f"**`User id`** - {user.id}\n"
        f"**`Created at`** - {created_str}\n"
        f"**`Has nitro`** - {bool_to_yesno(nitro)}\n"
        f"**`Hypesquad`** - {hypesquads[list_num]}\n"
        f"**`Mention`** - <@{user.id}>\n"
        f"**`Is bot?`** - {bool_to_yesno(user.bot)}\n"
        f"**`Alloted color`** - {color_matcher(str(user.default_avatar)[41:42] if user.default_avatar else '')}\n"
        f"**`Bug Hunter`** - {bool_to_yesno(getattr(user.public_flags, 'bug_hunter', False))}\n"
        f"**`Early supporter`** - {bool_to_yesno(getattr(user.public_flags, 'early_supporter', False))}\n"
        f"**`Avatar url`** - [Click here]({avatar_url})"
    )

    if server_member:
        joined = server_member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p") if server_member.joined_at else "Unknown"
        top_role = server_member.top_role.name if server_member.top_role else "None"
        boosting = server_member.premium_since or "Not boosting this server"

        embed.add_field(
            name="In Guild Information",
            value=(
                f"**`Join date`** - {joined}\n"
                f"**`Nick name`** - {server_member.nick or 'None'}\n"
                f"**`Boosting server`** - {boosting}\n"
                f"**`Top role`** - {top_role}"
            ),
            inline=False
        )

    return embed

# -------------------------------
#   GUILD EMBED (low RAM version)
# -------------------------------

async def build_guild_embed(guild: discord.Guild):
    guild_desc = guild.description or "No description"
    created_str = guild.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
    sec_map = ["low", "medium", "high", "highest"]
    sec = sec_map[guild.mfa_level] if guild.mfa_level < len(sec_map) else "unknown"

    member_count = guild.member_count or "Unknown"
    bot_count = "Unknown"   # to avoid iterating all members

    text_channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
    categories = guild.categories

    embed = discord.Embed(
        title="Guild Information",
        color=discord.Color.from_rgb(117,255,255)
    )

    embed.description = (
        f"**`Guild name -`** {guild.name}\n"
        f"**`Guild description -`**\n{guild_desc}\n"
        f"**`Member count -`** {member_count}\n"
        f"**`Bots -`** {bot_count}\n"
        f"**`Created at -`** {created_str}\n"
        f"**`Owner id -`** {guild.owner_id}\n"
        f"**`Boost level -`** {guild.premium_tier}\n"
        f"**`Security level -`** {sec}\n"
        f"**`Roles -`** {len(guild.roles)}\n"
        f"**`Text channels -`** {len(text_channels)}\n"
        f"**`Categories -`** {len(categories)}\n"
        f"**`NSFW level -`** {getattr(guild, 'nsfw_level', 'unknown')}"
    )

    return embed

# -------------------------------
#   ABOUT GROUP
# -------------------------------

about = SlashCommandGroup("about", "about bot command")

@bot.slash_command(name="about", description="Know about the developers and the bot!")
async def about_cmd(ctx: discord.ApplicationContext):

    LogIdentifier(ctx, "about")

    embed = discord.Embed(
        title="About Bot",
        description=(
            "This bot's purpose is to fetch the **maximum information** about a user or server using their ID.\n"
            "Unlike other bots, this one is **specialized** for info lookup."
        ),
        color=discord.Color.from_rgb(117, 255, 255)
    )

    embed.add_field(
        name="__Total Users__",
        value="Unknown (low-RAM mode)",
        inline=True
    )
    embed.add_field(
        name="__Total Servers__",
        value=f"{len(bot.guilds)} servers!",
        inline=True
    )
    embed.add_field(
        name="__Version__",
        value="v2.9",
        inline=True
    )

    # Bot avatar
    try:
        me = await bot.fetch_user(bot.user.id)
        embed.set_thumbnail(url=me.avatar.url)
    except:
        pass

    embed.set_footer(
        text="A project by RitTheDev#0519",
        icon_url="https://cdn.discordapp.com/avatars/764736831643975693/29372d85837ce1b747e98297a3e00b93.png?size=1024"
    )

    await ctx.respond(embed=embed, view=AboutView())

# -------------------------------
#   SLASH COMMANDS (other)
# -------------------------------

@bot.slash_command(name="help", description="Get a list of all commands and how to use the bot")
async def help_cmd(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        description="**Type `/info id:<id>` to get the information of the user or guild.**",
        color=discord.Color.from_rgb(117,255,255)
    )
    embed.add_field(name="User information", value="`/info`", inline=False)
    embed.add_field(name="Guild information", value="`/info (guild id)`", inline=False)
    embed.add_field(name="General commands", value="`/help`, `/example`, `/about bot`, `/ping`, `/support`", inline=False)
    await ctx.respond(embed=embed, view=SupportView())

@bot.slash_command(name="ping", description="Check bot latency")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"latency ping is {round(bot.latency * 1000)} ms")

@bot.slash_command(name="example", description="View an example image to know how to use the bot")
async def example(ctx: discord.ApplicationContext):
    embed = discord.Embed(color=discord.Color.purple())
    embed.set_image(url="https://cdn.discordapp.com/attachments/912924429057675274/949286662360403978/unknown.png")
    await ctx.respond(embed=embed)

@bot.slash_command(name="support", description="Need help? Support information")
async def support(ctx: discord.ApplicationContext):
    await ctx.respond(
        "If there are any issues with the bot:\n• try /help or /example\n• make sure the bot has Embed and Send permissions\n• join our support server",
        view=SupportView()
    )

@bot.slash_command(name="this", description="Get information about yourself")
async def this(ctx: discord.ApplicationContext):
    embed = await build_user_embed(ctx.author, ctx.guild, False)
    await ctx.respond(embed=embed)

@bot.slash_command(name="info", description="Get information about a user or guild")
async def info(ctx: discord.ApplicationContext, id: str):
    if ctx.author.id in banned_users:
        return await ctx.respond("You are not allowed to use this bot.", ephemeral=True)

    # mention <@123>
    try:
        if id.startswith("<@") and id.endswith(">"):
            uid = int(''.join(ch for ch in id if ch.isdigit()))
            user = await bot.fetch_user(uid)
            embed = await build_user_embed(user, ctx.guild, True)
            return await ctx.respond(embed=embed)
    except:
        pass

    # numeric id
    try:
        maybe = int(id)

        # Try user
        try:
            user = await bot.fetch_user(maybe)
            embed = await build_user_embed(user, ctx.guild, False)
            return await ctx.respond(embed=embed)
        except discord.NotFound:
            pass

        # Try guild (local first)
        guild = bot.get_guild(maybe)
        if guild:
            embed = await build_guild_embed(guild)
            return await ctx.respond(embed=embed)

        # fetch guild
        guild = await bot.fetch_guild(maybe)
        embed = await build_guild_embed(guild)
        return await ctx.respond(embed=embed)

    except ValueError:
        return await ctx.respond("Invalid id. Provide a numeric user or guild id, or a mention.", ephemeral=True)
    except discord.Forbidden:
        return await ctx.respond("I don't have access to that guild's info.", ephemeral=True)
    except Exception as e:
        return await ctx.respond(f"Error: {e}", ephemeral=True)

# -------------------------------
#   EVENTS
# -------------------------------

@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"Logged in as {bot.user} (id: {bot.user.id})")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"/help | on {len(bot.guilds)} servers!"
        )
    )

# -------------------------------
#   RUN BOT
# -------------------------------
async def handle_health(request):
    return web.Response(text="OK")

async def start_web_server():
    port = int(os.environ.get("PORT", 10000))  # Render provides $PORT
    app = web.Application()
    app.router.add_get("/", handle_health)
    app.router.add_get("/healthz", handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"HTTP server started on 0.0.0.0:{port}")
async def main():
    # start the HTTP server first (so Render can see it quickly)
    await start_web_server()

    # then start the bot (this call is non-blocking here because we're in the same loop)
    # NOTE: bot.start is coroutine — unlike bot.run
    try:
        await bot.start(TOKEN)
    finally:
        await bot.close()

if __name__ == "__main__":
    # run the combined webserver + bot in asyncio
    asyncio.run(main())
