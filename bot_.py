import discord
import discostack

async def send_message(message, user_message):
    print(user_message)
    try:
        response = discostack.handle_reponse(user_message)
        await message.author.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTAzODQ2OTU1NjQwODE1NjI5MQ.GqVSrS.UDdwlLYsOW4JcaLhROLDFhDzQWWjQlHM3IbOhI"
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if user_message[0] == "!":
            user_message = user_message[1:]
            await send_message(message, user_message)

    client.run(TOKEN)