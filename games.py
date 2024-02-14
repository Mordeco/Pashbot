import random

def play_flip_coin(message, bot):
    user_id = message.author.id
    if " " not in message.content:
        await message.channel.send("Please specify the amount and 'heads' or 'tails' after '!flip'.")
        return
    
    try:
        amount_str, guess = message.content.split()[1:]
        amount = int(amount_str)
    except ValueError:
        await message.channel.send("Invalid amount. Please enter a number.")
        return
    
    if manage_currency.get_balance(user_id) < amount:
        await message.channel.send("Insufficient funds.")
        return
    
    coin_side = random.choice(["heads", "tails"])
    if coin_side == guess:
        manage_currency.deposit_coins(user_id, amount * 2)
        response = f"Congratulations! You guessed {coin_side} correctly and won {amount * 2} {manage_currency.currency_name}!"
    else:
        manage_currency.withdraw_coins(user_id, amount)
        response = f"Sorry, the coin landed on {coin_side}. You lost {amount} {manage_currency.currency_name}."
    
    await message.channel.send(response)

# Example usage for testing
# play_flip_coin(message, bot)
