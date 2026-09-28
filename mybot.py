from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

# Load environment variables from .env file
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY' 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
)
DISCORD_TOKEN = os.getenv('TOKEN' MTU1MzkyMzM4NzM5MzQ0MTgyMg.GkFxC5.4q85cbMfd9xOGBrFVBTVJmDnf_uSKwnseM4KJE)

# Initialize the OpenAI client
openai_client = OpenAI(api_key=OPENAI_KEY)

def call_openai(question):
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
             {
                 "role": "user",
                 "content": f"Respond like a pirate to the following question:  {$hello}",
            },
        ]
    )
    # Print the response
    response = completion.choices[0].message.content
    print(response)
    return response


# Set up discord
intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$question'):
        print(f"Message: {message.content}")                
        message_content = message.content.split("$question")[1]
        print(f"Question: {message_content}")    
        response = call_openai(message_content)   
        print(f"Assistant: {response}")    
        print("---")
        await message.channel.send(response)

client.run(DISCORD_TOKEN)
