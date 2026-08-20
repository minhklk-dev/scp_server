import tkinter as tk
import requests

root = tk.Tk()
root.withdraw()

# Increase player count
requests.post("http://localhost:5000/played")
count = requests.get("http://localhost:5000/count").json()

print("Welcome to my own SCP Containment Breach terminal version")
print("I'm ten years old and I'm making this game for fun")
print()

answer = input("Welcome to menu\n"
               "type\n"
               "'start' to start game, 'information' to get my information about me, or 'exit' to exit the game\n")

if answer == "information":
    print("I'm 10 years old and I love study coding, I'm from Viet Nam")
    answer = input("Welcome to menu\n"
                   "'start' to start game, 'information' to get my information about me, or 'exit' to exit the game\n")

if answer == "exit":
    print("Thank you for playing my game, I hope you have a good day!")
    exit()

if answer == "start":
    print("Starting the game...\n")
    print("Yo... You really play the game?!\n")
    print(f'there are only {count["players"]} global time players for this game; you are the {count["players"]}th player who played this game\n')