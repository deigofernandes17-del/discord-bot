import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "DISCORD_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# SINCRONIZAR SLASH COMMANDS
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")

    print(f"{bot.user} está ONLINE!")


# ---------------------------
# /aviso
# ---------------------------
@bot.tree.command(name="aviso", description="Envia um aviso em um canal específico.")
@app_commands.describe(texto="Texto do aviso", canal="Canal onde enviar")
@app_commands.checks.has_permissions(manage_messages=True)
async def aviso(interaction: discord.Interaction, texto: str, canal: discord.TextChannel):
    await canal.send(f"📢 **AVISO:** {texto}")
    await interaction.response.send_message("Aviso enviado!", ephemeral=True)


# ---------------------------
# /falar (todos podem usar)
# ---------------------------
@bot.tree.command(name="falar", description="O bot fala o que você escrever.")
@app_commands.describe(texto="O que o bot deve falar")
async def falar(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message("Mensagem enviada!", ephemeral=True)
    await interaction.channel.send(texto)


# ---------------------------
# /ban
# ---------------------------
@bot.tree.command(name="ban", description="Bane um usuário.")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, membro: discord.Member, motivo: str = "Nenhum"):
    await membro.ban(reason=motivo)
    await interaction.response.send_message(f"{membro} foi banido! Motivo: {motivo}")


# ---------------------------
# /kick
# ---------------------------
@bot.tree.command(name="kick", description="Expulsa um usuário.")
@app_commands.checks.has_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, membro: discord.Member, motivo: str = "Nenhum"):
    await membro.kick(reason=motivo)
    await interaction.response.send_message(f"{membro} foi expulso! Motivo: {motivo}")


# ---------------------------
# /mute
# ---------------------------
@bot.tree.command(name="mute", description="Silencia um usuário.")
@app_commands.checks.has_permissions(moderate_members=True)
async def mute(interaction: discord.Interaction, membro: discord.Member, minutos: int):
    await membro.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minutos))
    await interaction.response.send_message(f"{membro} foi silenciado por {minutos} minutos!")


# ---------------------------
# /warn
# ---------------------------
@bot.tree.command(name="warn", description="Adverte um usuário.")
@app_commands.checks.has_permissions(manage_messages=True)
async def warn(interaction: discord.Interaction, membro: discord.Member, motivo: str):
    await interaction.response.send_message(f"{membro.mention} recebeu um aviso: **{motivo}**")


bot.run(TOKEN)
