import time
import os
import random

friends = {}
friends = set()

onl = ["(ᴗ˳ᴗ)zZ", "(^-^)!", "(-_-)"]

def load():
    for i in range(2):
        print(".")
        time.sleep(0.2)
        os.system("cls")
        print("..")
        time.sleep(0.2)
        os.system("cls")
        print("...")
        time.sleep(0.2)
        os.system("cls")
        print("..")
        time.sleep(0.2)
        os.system("cls")
        print(".")
        time.sleep(0.2)
        os.system("cls")
        print("..")
        time.sleep(0.2)
        os.system("cls")
        print("...")
        time.sleep(0.2)
        os.system("cls")
        print("..")
        time.sleep(0.2)
        os.system("cls")

def addfriend():
    os.system("cls")

    username = input("What is the username of the friend?                ")

    os.system("cls")
    time.sleep(0.5)
    load()

    time.sleep(0.25)
    os.system("cls")
    time.sleep(0.25)

    print(f"{username} has been added to your friendlist.                ")
    friends.add(username)

    time.sleep(2.5)
    os.system("cls")

def showlist():
    os.system("cls")
    amt = len(friends)
    if amt == 0:
        load()
        print("No friends added.")
        time.sleep(1)
        os.system("cls")
        return
    else:
        load()
        time.sleep(0.5)
        print(f"You have {str(amt)} friends.")
        for item in friends:
            onlcheck = random.choice(onl)
            print(f"- {item}: {onlcheck}")
            time.sleep(5)
            os.system(clear)

def remfriend():
    os.system("cls")
    amt = len(friends)
    if amt == 0:
        load()
        time.sleep(0.5)
        print("No friends added.")
        time.sleep(1)
        os.system("cls")
        return
    remofriend = input("Who do you want to remove from your friendlist?")
    if remofriend not in friends:
        load()
        time.sleep(0.5)
        print("Friend is not in your Friendlist.")
        time.sleep(1)
        os.system("cls")
        return

    else:
        load()
        time.sleep(0.5)
        friends.discard(remofriend)
        print(f"{remofriend} is removed from your friendlist.")
        time.sleep(1)
        os.system("cls")
