import discord
from discord.ext import commands
import json
import random
from currency import manage_currency
from banks import manage_banks
from games import play_flip_coin
from help import send_help

# Your Discord bot token here
bot_token = "YOUR_BOT_TOKEN"

# Data file 
currency_data_file = "currency_data.json"
banks_data_file = "banks_data.json"

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    load_data(currency_data_file, banks_data_file)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # global commands
    if message.content.startswith("!balance"):
        await manage_currency.check_balance(message, bot)
    elif message.content.startswith("!work"):
        await manage_currency.earn_coins(message, bot)
    elif message.content.startswith("!daily"):
        await manage_currency.claim_daily(message, bot)
    elif message.content.startswith("!createbank"):
        await manage_banks.create_bank(message, bot)
    elif message.content.startswith("!addmember"):
        await manage_banks.add_member(message, bot)
    elif message.content.startswith("!deposit"):
        await manage_banks.deposit_to_bank(message, bot)
    elif message.content.startswith("!withdraw"):
        await manage_banks.withdraw_from_bank(message, bot)
    elif message.content.startswith("!requestloan"):
        await manage_banks.request_loan(message, bot)
    elif message.content.startswith("!repayloan"):
        await manage_banks.repay_loan(message, bot)
    elif message.content.startswith("!leaderboard"):
        if "users" in message.content:
            await manage_currency.show_richest_users(message, bot)
        elif "banks" in message.content:
            await manage_banks.show_richest_banks(message, bot)
        else:
            await message.channel.send("Invalid leaderboard type. Use '!leaderboard users' or '!leaderboard banks'.")
    elif message.content.startswith("!flip"):
        await play_flip_coin(message, bot)
    elif message.content.startswith("!help"):
        await send_help(message, bot)
    else:
        await message.channel.send("Invalid command. Use '!help' for a list of commands.")

@bot.command()
async def shutdown(ctx):
    if ctx.author.id == owner_id:  # Replace with your bot owner ID
        await bot.logout()
        print("Bot shutting down...")
    else:
        await ctx.send("You don't have permission to shut down the bot.")

# Data management functions
def load_data(currency_path, banks_path):
    try:
        with open(currency_path, "r") as f:
            manage_currency.currency_data = json.load(f)
        with open(banks_path, "r") as f:
            manage_banks.banks_data = json.load(f)
    except FileNotFoundError:
        pass

def save_data(currency_path, banks_path):
    with open(currency_path, "w") as f:
        json.dump(manage_currency.currency_data, f)
    with open(banks_path, "w") as f:
        json.dump(manage_banks.banks_data, f)

bot.run(bot_token)
