# ASk the user if they have played before
show_instructions = input("Have you played this game before? :")

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("program continues")

# If they say no, output 'Display Instructions'
elif show_instructions == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")