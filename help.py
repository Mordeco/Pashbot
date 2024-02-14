def send_help(message, bot):
    # Create a formatted help message
    help_message = """**Available Commands:**

* **!balance:** Check your Pash Coin balance.
* **!work:** Earn Pash Coins by simulating work (cooldown and daily limit apply).
* **!daily:** Claim your daily bonus Pash Coins (cooldown and streak bonus apply).
* **!createbank <bank name>:** Create a new bank with a custom name.
* **!addmember <bank name> <username>:** Invite a user to join your bank.
* **!deposit <bank name> <amount>:** Deposit Pash Coins into your bank (limited based on contributions).
* **!withdraw <bank name> <amount>:** Withdraw Pash Coins from your bank (limited based on contributions).
* **!requestloan <bank name> <amount> <purpose> <repayment plan>:** Request a loan from your bank owner.
* **!repayloan <bank name> <amount>:** Repay a loan to your bank.
* **!leaderboard users:** View the leaderboard of richest users.
* **!leaderboard banks:** View the leaderboard of richest banks.
* **!flip <amount> <heads/tails>:** Bet Pash Coins on a coin flip (double win, lose bet amount).
* **!help:** Get help with available commands.

**Additional notes:**

* For most commands, replace `<bank name>` with the actual name of your bank and `<username>` with the username of the user you want to add/invite.
* Use the correct amount format (e.g., 10, 25) for commands involving money.
* Remember cooldowns and limitations for certain actions.

**For detailed information about a specific command, enter '!help <command name>'.**

"""

    # Send the help message to the user's DM
    await message.author.send(help_message)

# Example usage for testing
# send_help(message, bot)
