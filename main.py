import discord
import random

client = discord.Client()

fiso_hints = ["how", "wen", "when", "claim", "closed", "couldn't", "can't", "min", "mint"]
testnet_hints = ["wen", "when", "reward"]
bender_quotes = ["Listen, you fat internet nerd!",
                 "Shit got a bit more classy in here.",
                 "I guess if you want children beaten, you have to do it yourself.",
                 "Oh wait, you're serious. Let me laugh even harder.",
                 "Everybody's a jerk. You, me, that jerk over there. That's my philosophy.",
                 "I'm so embarrassed. I wish everybody else was dead."]

@client.event
async def on_ready():
    print('\nWe are logged in as {0.user}'.format(client))

@client.event
# Listen for an incomming message
async def on_message(message):

    # If the author is the robot itself, then do nothing!
    if message.author == client.user:
        return
    # If the user asks
    if message.content.endswith("?"):
        user_question = message.content.lower()
        if "fiso" in user_question:
            if any(x in user_question for x in fiso_hints):
                await message.reply(benderize("\nFISO is already finished!"))
        elif "testnet" in user_question:
            if any(x in user_question for x in mint_hints):
                await message.reply(benderize("\nAs the process for reviewing feedback is manual, it will take its time for testnet participants to receive rewards." +
                    "\nPlease stay tuned on our channels for updates!"))

def benderize(answer):
    return random.choice(bender_quotes) + answer

client.run('<bot token goes here>')