import random
import time

while True:
    start_time = time.time()
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

    randomly_number = random.randrange(1, 101)

    record = {"Easy": None, "Medium": None, "Hard": None}

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
        number_of_chances = 10
    elif number_of_choice == 2:
        level = "Medium"
        number_of_chances = 5
    elif number_of_choice == 3:
        level = "Hard"
        number_of_chances = 3

    print(f"""
    Great! You have selected the {level} difficulty level.
    Let's start the game!
    """)

    attempts_count = 0
    while number_of_chances != 0:
        try:
            player_input = int(input("Input your number: "))
            number_of_chances -= 1
            attempts_count += 1
            if player_input == randomly_number:
                print(f"\n\n\nYou won in {attempts_count} attempts!")
                break
            elif player_input != randomly_number:
                if player_input > randomly_number:
                    print("Your number higher than randomly number")
                elif player_input < randomly_number:
                    print("Your number less than randomly number")

            if number_of_chances == 0:
                print("\n\n\nYou lose(")
        except:
            print("Input correct number please.")

    elapsed_time = time.time() - start_time
    print(f"Duration game: {round(elapsed_time, 1)} sec")
    
    if number_of_chances != 0:
        if record.get(level) == None or record.get(level) > elapsed_time:
            record[level] = elapsed_time

    print("Record:")
    for level in record:
        print(f"{level}: {record[level]}")

    continue_question = input("Do you want to play it again? Input yes or no: ")
    if continue_question == "no" or continue_question == "n":
        break
