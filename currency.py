import json
import random

# Replace with your currency name if needed
currency_name = "Pash Coins"

# Data structure for user balances
currency_data = {}

def load_data(data_file):
    try:
        with open(data_file, "r") as f:
            global currency_data
            currency_data = json.load(f)
    except FileNotFoundError:
        pass

def save_data(data_file):
    with open(data_file, "w") as f:
        json.dump(currency_data, f)

def check_balance(message, bot):
    user_id = message.author.id
    if user_id not in currency_data:
        currency_data[user_id] = 0
    balance = currency_data[user_id]
    await message.channel.send(f"Your {currency_name} balance: {balance}")

def earn_coins(message, bot):
    user_id = message.author.id
    cooldown = 60  # Adjust cooldown time in seconds
    last_work = currency_data.get("last_work", {}).get(user_id, 0)
    current_time = time.time()
    if current_time - last_work < cooldown:
        time_left = cooldown - (current_time - last_work)
        response = f"You can work again in {int(time_left)} seconds."
    else:
        amount = random.randint(10, 25)  # Adjust earning range
        currency_data[user_id] += amount
        currency_data["last_work"][user_id] = current_time
        response = f"You earned {amount} {currency_name} from work!"
    await message.channel.send(response)

def claim_daily(message, bot):
    user_id = message.author.id
    cooldown = 86400  # Adjust daily claim cooldown in seconds
    last_claim = currency_data.get("last_claim", {}).get(user_id, 0)
    current_time = time.time()
    if current_time - last_claim < cooldown:
        time_left = cooldown - (current_time - last_claim)
        response = f"You can claim your daily bonus again in {int(time_left)} seconds."
    else:
        streak = currency_data.get("streak", {}).get(user_id, 0) + 1
        amount = 10 + streak * 2  # Adjust base and streak bonus
        currency_data[user_id] += amount
        currency_data["last_claim"][user_id] = current_time
        currency_data["streak"][user_id] = streak
        response = f"You claimed your daily bonus of {amount} {currency_name} (streak: {streak})!"
    await message.channel.send(response)

if __name__ == "__main__":
    load_data("currency_data.json")
    # Example usage (for testing)
    print(check_balance("test_user"))
    print(earn_coins("test_user"))
    print(claim_daily("test_user"))
    save_data("currency_data.json")
