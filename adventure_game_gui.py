import tkinter as tk
import time
import random

# Create the main game window
root = tk.Tk()
root.title("Adventure Game")

# Define global variables for the game state
weapon = []
messages = []
creature = random.choice(["goblin", "troll", "dragon", "pirate"])


# Function to update the message area in the GUI
def update_message(new_message):
    global messages
    messages.append(new_message)
    message_label.config(text="\n".join(messages))


# Function for handling the house scenario
def house():
    update_message("You approach the door of the house.")
    update_message(f"It is a {creature}!")
    update_message(f"The {creature} attacks you!")

    if "sword" in weapon:
        update_message(f"As the {creature} moves to attack, you unsheathe "
                       "your new sword. The Sword of Ogoroth shines brightly in your hand.")
        update_message(f"The {creature} runs away!")
        update_message("You have rid the town of the wicked creature. You are victorious!")
    else:
        update_message("You feel underprepared, holding only a dagger.")
        update_message(f"The {creature} overpowers you. You have been defeated.")

    play_again()


# Function for handling the cave scenario
def cave():
    update_message("You peer cautiously into the cave.")
    if "sword" in weapon:
        update_message("You've been here before and have the magical sword.")
    else:
        update_message("Your eye catches a glint of metal behind a rock.")
        update_message("You have found the magical Sword of Ogoroth!")
        weapon.append("sword")
    update_message("You walk back to the field.")
    display_field_buttons()


# Function to ask if the player wants to play again
def play_again():
    # Clear the previous buttons
    for widget in button_frame.winfo_children():
        widget.destroy()

    play_again_label = tk.Label(button_frame, text="Would you like to play again?")
    play_again_label.pack()

    yes_button = tk.Button(button_frame, text="Yes", command=play_game)
    yes_button.pack(side=tk.LEFT)

    no_button = tk.Button(button_frame, text="No", command=root.quit)
    no_button.pack(side=tk.RIGHT)


# Function to display the field buttons (knock on house or go to cave)
def display_field_buttons():
    for widget in button_frame.winfo_children():
        widget.destroy()

    # Buttons for player to choose actions
    house_button = tk.Button(button_frame, text="Knock on the door of the house", command=house)
    house_button.pack(side=tk.LEFT)

    cave_button = tk.Button(button_frame, text="Peer into the cave", command=cave)
    cave_button.pack(side=tk.RIGHT)


# Function to start the game
def play_game():
    global weapon, messages, creature
    weapon = []
    messages = []
    creature = random.choice(["goblin", "troll", "dragon", "pirate"])

    # Game introduction
    update_message("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    update_message("Rumor has it that a wicked creature is somewhere around here.")
    update_message("In front of you is a house. To your right is a dark cave.")
    update_message("In your hand you hold your trusty (but not very effective) dagger.")

    # Display the action buttons (house/cave)
    display_field_buttons()


# GUI Layout
message_frame = tk.Frame(root)
message_frame.pack(pady=20)

message_label = tk.Label(message_frame, text="", justify="left", font=("Arial", 14), wraplength=400)
message_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Start the game when the window loads
play_game()

# Start the tkinter main loop
root.mainloop()
