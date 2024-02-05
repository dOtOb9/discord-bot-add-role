import discord


intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():

    for guild in bot.guilds:

        roles = guild.roles


        for member in guild.members:
            print(member.display_name)

            role_list = []
            for role in member.roles:
                role_list.append(role.name)

            print(role_list)

            for part in ['Vn.', 'Vc.', 'Va.', 'Cb.', '弦', '金管打', '木管']:
                if (part in role_list) and ('現役' in role_list):
                    for role in roles:
                        if (role.name == part + '&現役'):
                            await member.add_roles(role)
                            print(f'{member.display_name}に{role.name}を付与しました。')

    print('Finish!')


bot.run('DISCORD_TOKEN')