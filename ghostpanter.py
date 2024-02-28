import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='/', intents=intents)

forbidden_channel_ids = [
    1074286502160388108,
    1109156478343987210,
    1074892134961905774,
    1074364271372279990,
    1074953412111777882
]

@bot.command()
async def server(ctx):
    if ctx.channel.id in forbidden_channel_ids:
        await ctx.author.send("Вы не можете использовать эту команду в этом канале.")
        return

    embed = discord.Embed(
        title="𝐋𝐮𝐧𝐚𝐫𝐖𝐨𝐫𝐥𝐝",  # Название сервера
        description="Майнкрафт сервер LunarWorld",  # Описание сервера
        color=0x8A2BE2  # Фиолетовый цвет
    )

    embed.add_field(name="𝐦𝐋𝐋𝐖𝐞𝐞𝐞", value="Пиар администратор, главный администратор, создатель", inline=False)
    embed.add_field(name="𝐂𝐫𝐲𝐏𝐚𝐧𝐭𝐞𝐫𝟏𝟒", value="Технический администратор, главный администратор, создатель", inline=False)

    await ctx.send(embed=embed)

bot.run("MTIxMjE1NjkwMzkyNTIyNzU2MQ.GbwmwY.HtupSMbWvLTLQikYKT_KNjL9TTBlwuqVlQFkAw")