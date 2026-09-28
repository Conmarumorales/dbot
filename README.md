import os import discord
from dotenv import load_dotenv
from openai import OpenAI
# Cargar variables de entorno desde el archivo env
Load_dotenv()
DEEPSEEK_API_KEY = os. geten(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)
DISCORD_TOKEN = os. geten(MTU1MzkyMzM4NzM5MzQ0MTgyMg.GkFxC5.4q85cbMfd9xOGBrFVBTVJmDnf_uSKwnseM4KJE)
# Inicializar el cliente compatible con la API de DeepSk
deepseek_client = OpenAI (
api_key=DEEPSEEK_API_KEY,
base_url="https://api.deepseek.com"
def call_deepseek(question) :
completion = deepseek_client.chat.completions.createl
model="deepseek-chat", # Usa "deepseek-chat" para DeepSeek-V3 o
"deepseek-reasoner" para DeepSeek-R1
messages=l
If message.content.startswith(‘$hello’): 
Await message.channel.send.(‘’Hello!)
"role": "system"
"content": "You are a pirate. Respond to all user prompts in full
pirate character."
"role": "user",
"content": question,
},
)
response = completion.choices [0].message. content
python discord_only.py
