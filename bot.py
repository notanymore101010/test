import discord

TOKEN = "MTM0NDI5MTEyMTg1NzI5ODUyMw.Goo8qn.LOjO67U0lwkRFiMuBuh77Il3aKea23bg3ecLvU"

intents = discord.Intents.default()
intents.messages = True  # Ensure the bot can read messages
intents.message_content = True  # Enable message content access

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"📩 Message received: {message.content}")  # Debugging line

    if message.author == client.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("Hello!")

client.run(TOKEN)
