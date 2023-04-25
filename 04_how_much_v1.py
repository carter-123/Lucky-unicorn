"""Component 2 (How much) v1
Ask user how much they want to play with and check that input is valid. If valid,
this amount becomes the players balance"""


user_balance = int(input("How much do you want to play with (must be an "
                         "integer between 1 and 10) $"))

# Keep asking until a valid amount is entered
while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number between 1 and 10")
    # ask for the input
    user_balance = int(input("How much do you want to play with $"))

print(f"You are playing with ${user_balance}")