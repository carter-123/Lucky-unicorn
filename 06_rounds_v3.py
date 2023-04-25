"""Component 4 - game mechanics and looping v1
Convert v2 into a function
"""

import random

# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1 # keep rounds tallied
        number = random.randint(1, 100)

        # adjust balance
        # if the random number is between 1 and 5, user gets a unicorn (+4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # if number is between 6 and 36, user gets a donkey (-1 to balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # in all other cases the token is a horse or zebra (-.5 to balance)
        else:
            # if number is even, token is zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5

            # otherwise, token is a horse
            else:
                token = "horse"
                balance -= 0.5

        # output
        print(f"Round {rounds_played}. Token: {token}, Balance: {balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play"
                               "again or 'X' to exit").lower()
        print()
    return balance


# Main routine
starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${closing_balance:.2f}")
print("Goodbye!")