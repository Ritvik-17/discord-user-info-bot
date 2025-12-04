# main.py — modernized for 2025 (py-cord / discord.py v2+ style)
import os
from dotenv import load_dotenv
import discord
from discord.ui import View, Button

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("Missing DISCORD_TOKEN in environment")

intents = discord.Intents.default()
intents.members = True  # needed for server-member info

# Use discord.Bot (py-cord / modern discord lib)
bot = discord.Bot(intents=intents)

# --- Config / small globals ---
banned_users = []   # placeholder (your original code referenced banned_users). :contentReference[oaicite:6]{index=6}
NO_AUTORESPONSE_GUILDS = set()
COLOR_DICTIONARY = {"0": "Blue","1": "Grey","2": "Green","3": "Yellow","4": "Red","5": "Pink"}

# --- Reusable Views (buttons) converted from original code's Views. --- :contentReference[oaicite:7]{index=7}
class SupportView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="Support server", url="https://discord.com/invite/gzaz9SSkkW"))
        self.add_item(Button(label="Example", url="https://cdn.discordapp.com/attachments/912924429057675274/949286662360403978/unknown.png"))

class InviteView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="Invite", url="https://discord.com/oauth2/authorize?client_id=888985968554688512&permissions=414464867393&scope=bot%20applications.commands"))

# --- Utility helpers (kept behavior similar to original) ---
def bool_to_yesno(b: bool) -> str:
    return "Yes" if b else "No"

def color_matcher(avatar_str_segment: str) -> str:
    return COLOR_DICTIONARY.get(avatar_str_segment, "Unknown")

async def build_user_embed(user: discord.User, guild: discord.Guild | None, mention_mode: bool):
    """Return a discord.Embed with user info (replicates original fields)."""
    nitro = False
    try:
        if user.avatar and user.avatar.is_animated():
            nitro = True
    except Exception:
        nitro = False

    created_str = user.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

    # Hypesquad flags (best-effort replicate)
    hypesquads = ["brilliance", "bravery", "balance", "none"]
    list_num = 3
    try:
        pf = user.public_flags
        if getattr(pf, "hypesquad_brilliance", False): list_num = 0
        if getattr(pf, "hypesquad_bravery", False): list_num = 1
        if getattr(pf, "hypesquad_balance", False): list_num = 2
    except Exception:
        pass

    # Is user a member of current guild?
    member_in_guild = False
    server_member = None
    if guild:
        server_member = guild.get_member(user.id)
        member_in_guild = server_member is not None

    embed = discord.Embed(title="User Information", color=discord.Color.from_rgb(117,255,255))
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

    # If in guild, add join/roles/boost info
    if server_member:
        joined = server_member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p") if server_member.joined_at else "Unknown"
        top_role = server_member.top_role.name if server_member.top_role else "None"
        boosting_since = server_member.premium_since or "Not boosting this server"
        embed.add_field(
            name="In Guild Information",
            value=(
                f"**`Join date`** - {joined}\n"
                f"**`Nick name`** - {server_member.nick or 'None'}\n"
                f"**`Boosting server`** - {boosting_since}\n"
                f"**`Top role`** - {top_role}"
            ),
            inline=False
        )

    return embed

async def build_guild_embed(guild: discord.Guild):
    """Return a discord.Embed with guild info (replicates original)."""
    guild_desc = guild.description or "No description"
    created_str = guild.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")
    mfa_map = ["low","medium","high","highest"]
    sec_level = mfa_map[guild.mfa_level] if guild.mfa_level < len(mfa_map) else "unknown"

    # count text channels and categories & bots
    text_channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
    categories = [c for c in guild.categories]
    member_count = guild.member_count or sum(1 for _ in guild.members)
    bot_count = sum(1 for m in guild.members if m.bot)

    embed = discord.Embed(title="Guild Information", color=discord.Color.from_rgb(117,255,255))
    embed.description = (
        f"**`Guild name -`** {guild.name}\n"
        f"**`Guild description -`**\n{guild_desc}\n"
        f"**`Member count -`** {member_count}\n"
        f"**`Bots -`** {bot_count}\n"
        f"**`Created at -`** {created_str}\n"
        f"**`Owner id -`** {guild.owner_id}\n"
        f"**`Boost level -`** {guild.premium_tier}\n"
        f"**`Security level -`** {sec_level}\n"
        f"**`Roles -`** {len(guild.roles)}\n"
        f"**`Text channels -`** {len(text_channels)}\n"
        f"**`Categories -`** {len(categories)}\n"
        f"**`NSFW level -`** {getattr(guild, 'nsfw_level', 'unknown')}"
    )
    return embed

# --- Slash commands (help/ping/this/info/site/etc) ---
@bot.slash_command(name="help", description="Get a list of all commands and how to use the bot")
async def help_cmd(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        description="**Type `/info id:<id>` to get the information of the user or guild.**",
        color=discord.Color.from_rgb(117,255,255)
    )
    embed.add_field(name="User information", value="`/info`", inline=False)
    embed.add_field(name="Guild information", value="`/info` (guild id)`", inline=False)
    embed.add_field(name="General commands", value="`/help`, `/example`, `/about`, `/ping`, `/support`", inline=False)
    await ctx.respond(embed=embed, view=SupportView())

@bot.slash_command(name="ping", description="Check bot latency")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"latency ping is {round(bot.latency * 1000)} ms")

@bot.slash_command(name="example", description="View an example image to know how to use the bot")
async def example(ctx: discord.ApplicationContext):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/912924429057675274/949286662360403978/unknown.png")
    embed.color = discord.Color.purple()
    await ctx.respond(embed=embed)

@bot.slash_command(name="support", description="Need help? Support information")
async def support(ctx: discord.ApplicationContext):
    await ctx.respond(
        "If there are any issues with the bot:\n• try /help or /example\n• make sure the bot has Embed and Send permissions\n• join our support server",
        view=SupportView()
    )

@bot.slash_command(name="this", description="Get information about yourself")
async def this(ctx: discord.ApplicationContext):
    embed = await build_user_embed(ctx.author, ctx.guild, mention_mode=False)
    await ctx.respond(embed=embed)

@bot.slash_command(
    name="info",
    description="Get information about a user or guild",
)
async def info(ctx: discord.ApplicationContext, id: str):
    # simple banned check
    if ctx.author.id in banned_users:
        return await ctx.respond("You are not allowed to use this bot.", ephemeral=True)

    # Try parse mention
    try:
        # mention like <@!123> or <@123>
        if id.startswith("<@") and id.endswith(">"):
            uid = int(''.join(ch for ch in id if ch.isdigit()))
            user = await bot.fetch_user(uid)
            embed = await build_user_embed(user, ctx.guild, mention_mode=True)
            return await ctx.respond(embed=embed)
    except Exception:
        pass

    # Try as user id
    try:
        maybe_int = int(id)
        # try user first
        try:
            user = await bot.fetch_user(maybe_int)
            embed = await build_user_embed(user, ctx.guild, mention_mode=False)
            return await ctx.respond(embed=embed)
        except discord.NotFound:
            # try guild
            guild = bot.get_guild(maybe_int) or await bot.fetch_guild(maybe_int)
            if guild:
                embed = await build_guild_embed(guild)
                return await ctx.respond(embed=embed)
            raise
    except ValueError:
        return await ctx.respond("Invalid id. Provide a numeric user or guild id, or a mention.", ephemeral=True)
    except discord.Forbidden:
        return await ctx.respond("I don't have access to that guild's info.", ephemeral=True)
    except Exception as e:
        return await ctx.respond(f"Error: {e}", ephemeral=True)

# --- Events ---
@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"Logged in as {bot.user} (id: {bot.user.id})")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"/help | on {len(bot.users)} users!"))

# Run
if __name__ == "__main__":
    bot.run(TOKEN)
