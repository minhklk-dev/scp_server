import tkinter as tk
import requests

root = tk.Tk()
root.withdraw()

URL = "https://scp-server-hsdk.onrender.com"

print("Connecting to server...")

try:
    requests.post(f"{URL}/played", timeout=5)
    count = requests.get(f"{URL}/count", timeout=5).json()
except Exception as e:
    print("⚠️ Could not connect to server. Running offline mode.")
    count = {"players": 0}

print("Welcome to my own SCP Containment Breach terminal version")
print("I'm ten years old and I'm making this game for fun\n")

answer = input("Welcome to menu\n"
               "type\n"
               "'start' to start game, 'information' to get my information about me, or 'exit' to exit the game\n")

if answer == "information":
    print("I'm 10 years old and I love studying coding, I'm from Viet Nam")
    answer = input("Welcome to menu\n"
                   "'start' to start game, 'information' to get my information about me, or 'exit' to exit the game\n")

if answer == "exit":
    print("Thank you for playing my game, I hope you have a good day!")
    exit()

if answer == "start":
    print("Starting the game...\n")
    print("Yo... You really play the game?!\n")
    print(f"There are {count['players']} global players who played this game; you are the {count['players']}th player!\n")

