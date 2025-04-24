import pet
import time
"""
- This is a simple pet simulator program that allows users to create a pet and interact with it.
- The user can feed the pet, play with it, teach it tricks, and check its status.
- The program uses a class to represent the pet and its attributes, and it provides a simple text-based interface for user interaction.
- The program is designed to be easy to use and understand, making it suitable for beginners in programming.
- The program is written in Python and uses basic programming concepts such as classes, methods, and user input.
- The program is designed to be run in a terminal or command prompt, and it provides clear instructions for the user to follow.
"""

def loading(action, petName=""):
    """Simulate loading time for pet actions."""
    if action == "teach":
        print(f"Teaching {petName} the new trick", end="")
    else:
        print(f"{petName} is {action}ing", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("")

# Main program starts here
print("==============================================")
print("Welcome to the Pet Simulator!")
print("You can create a pet and interact with it.")
print("Let's get started!")
name = input("Please enter the name of your pet: ")

userPet = pet.Pet(name)
print("==============================================")
print(f"🐶 Congratulations! You have created a pet named {userPet.name}.")
time.sleep(2)
print("Now, let's see what you can do with your pet.")
time.sleep(3)

while True:
    print("\n==============================================")
    print("Available options:")
    print("1. 🍖 Feed your pet")
    print("2. ⚽ Play with your pet")
    print("3. ✍️  Teach your pet a trick")
    print("4. 📃 Check your pet's status")
    print("5. 😴 Allow your pet to sleep")
    print("6. 📃 Display all tricks your pet knows")
    print("7. Exit")
    print("==============================================")
    try:
        userChoice = int(input("Please choose an option (1-7): "))
        if userChoice < 1 or userChoice > 7:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        time.sleep(2)  # Adding a delay for better readability
        continue

    # Processing user choice
    if userChoice == 1:
        loading("feed", userPet.name)
        userPet.eat()
        userPet.get_status()
    elif userChoice == 2:
        loading("play", userPet.name)
        userPet.play()
        userPet.get_status()
    elif userChoice == 3:
        trick = input("🎃 Please enter the trick you want to teach your pet: ")
        loading("teach", userPet.name)
        if trick == "":
            print("You didn't enter a trick. Please try again.")
            time.sleep(2)
            continue
        elif len(trick) > 20:
            print("Trick name is too long. Please keep it under 20 characters.")
            time.sleep(2)
            continue
        elif len(trick) < 3:
            print("Trick name is too short. Please provide a name with at least 3 characters.")
            time.sleep(2)
            continue
        elif not trick.isalpha():
            print("Trick name should only contain letters.")
            time.sleep(2)
            continue
        userPet.train(trick)
        userPet.get_status()
    elif userChoice == 4:
        userPet.get_status()
    elif userChoice == 5:
        loading("sleep", userPet.name)
        userPet.sleep()
        userPet.get_status()
    elif userChoice == 6:
        userPet.show_tricks()
        time.sleep(2)
    elif userChoice == 7:
        confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Thank you for using the Pet Simulator!")
            break
        else:
            print("Returning to the menu...")
            time.sleep(2)
    else:
        print("Try again.")
        time.sleep(2)

# Simulate closing the simulator
print("Closing the Pet simulator", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)
print("\nGoodbye!")
