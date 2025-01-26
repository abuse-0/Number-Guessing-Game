greeting = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 3-10 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
"""
print(greeting)

while True:
    try:
        number_of_choice = int(input("Enter your choice: "))
        if number_of_choice == 1 or number_of_choice == 2 or number_of_choice == 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if number_of_choice == 1:
    level = "Easy"
elif number_of_choice == 2:
    level = "Medium"
elif number_of_choice == 3:
    level = "Hard"

print(f"""
   Great! You have selected the {level} dificulty level.
   Let's start the game!
""")

