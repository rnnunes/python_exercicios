
import hikari
import lightbulb

bot = lightbulb.BotApp(token=open('token/token_discord.txt', 'r').read(),default_enabled_guilds=(int(open('id_servidor.txt', 'r').read())))

@bot.command
@lightbulb.command('msg_r1','Saudações mortais')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Opa, 100%?*')

bot.run() 
