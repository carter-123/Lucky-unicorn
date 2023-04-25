"""Component 3 (random tokens) v4
Calculate percentages to ensure odds favour the house
5% unicorns, 30% donkeys, and 65% horses/zebras"""

import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 100 tokens
for item in range(100):
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
    print(f"Token: {token}, Balance: ${balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
