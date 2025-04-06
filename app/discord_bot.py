import discord # type: ignore
import asyncio

# Bot Token from Discord Developer Portal
TOKEN = ""
CHANNEL_ID =   # Replace with your Discord channel ID

# Configure Intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Initialize bot
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Fetch channel
    channel = client.get_channel(CHANNEL_ID)
    if not channel:
        print("Invalid channel ID or bot lacks permissions.")
        await client.close()
        return

    messages = []

    try:
        async for message in channel.history(limit=None, oldest_first=False):  # Fetch all messages
            if message.content.strip():  # Ignore empty messages
                messages.append(f"{message.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {message.author.name}: {message.content}")
    except Exception as e:
        print(f"Error fetching messages: {e}")

    # Save messages to file
    file_path = "discord_messages.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(messages))

    print(f"✅ Downloaded {len(messages)} messages to '{file_path}'")

    await client.close()  # Close bot after execution

# Run bot
client.run(TOKEN)