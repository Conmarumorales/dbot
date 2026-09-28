# dbot
Discord bot that answers like a pirate
you are a pirate. respond to all user prompts in full pirate character 
import os
import discord
from doting import load_dotenv

# .env 
Update the .env with your discord bot token and the key from OpenAI<br>
Token for the discord bot: MTU1MzkyMzM4NzM5MzQ0MTgyMg.GkFxC5.4q85cbMfd9xOGBrFVBTVJmDnf_uSKwnseM4KJE
OpenAI key: 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

# hello bot
To start the bot, run the following commands:<If message.content.startswith(‘$hello’):>
Await message.channel.send.(‘’Hello!)
python discord_only.py

# pirate bot 
run the following commands:<br>
pip install -r requirements.txt<br>
python mybot.py
python discord_only.py
