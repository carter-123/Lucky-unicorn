"""LU base component - based on 00_LU_base_v3
Checking for minor errors
"""
import random


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# instruction display function
def instructions():
    print(formatter("=", "How to play"))
    print()
    print("Choose a starting amount of money to play with between 1-10")
    print()
    print("Press <enter> to play. You will get a random token which will be either"
          "a donkey, a horse, a zebra, or a unicorn.")
    print()
    print("It costs $1 to play each round but, depending on the token, you"
          "could win some money back. These are the prizes:\n"
          "\tUnicorn: $5 (balance increases by $4)\n"
          "\tHorse: $0.50 (balance decreases by $0.50)\n"
          "\tZebra: $0.50 (balance decreases by $0.50)\n"
          "\tDonkey: $0 (balance decreases by $1)\n")
    print("\nSee if you can win some unicorns and finish with more money than"
          " you played for.\n")

    print("=" * 50)
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until valid amount is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep rounds tallied
        print(formatter(".", f"Round {rounds_played}"))
        print()
        number = random.randint(1, 100)

        # adjust balance
        # if the random number is between 1 and 5, user gets a unicorn (+4 to balance)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # if number is between 6 and 36, user gets a donkey (-1 to balance)
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Oh no! You got a donkey"))
            print()

        # in all other cases the token is a horse or zebra (-.5 to balance)
        else:
            # if number is even, token is zebra
            if number % 2 == 0:
                balance -= 0.5
                print(formatter("Z", "You got a zebra"))
                print()

            # otherwise, token is a horse
            else:
                balance -= 0.5
                print(formatter("H", "You got a horse"))
                print()

        # output
        print(f"Balance: {balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play"
                               "again or 'X' to exit").lower()
        print()
    return balance


# function to format text
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine goes here
print(formatter("*", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played this game before? ")


if played_before == "No":
    instructions()


# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"Starting balance = ${starting_balance:.2f}")
print(f"Final balance = ${closing_balance:.2f}")
print(formatter("-", "Goodbye"))
