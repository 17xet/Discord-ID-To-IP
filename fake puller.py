import os
import random
import time
import webbrowser
from pystyle import Colors, Colorate, Center, Write


os.system('title ghost')

def logo():
    ascii_logo = """
                   ██╗██████╗     ██████╗ ██╗   ██╗██╗     ██╗     ███████╗██████╗ 
                   ██║██╔══██╗    ██╔══██╗██║   ██║██║     ██║     ██╔════╝██╔══██╗
                   ██║██████╔╝    ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
                   ██║██╔═══╝     ██╔═══╝ ██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
                   ██║██║         ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
                   ╚═╝╚═╝         ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                             
                 	      Made with great intent to destroy your hopes and dreams
"""
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(ascii_logo)))

def generate_fake_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        print()
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("[1] Discord to IP")))
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("[2] Exit")))
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter("[3] Support Me!")))
        print()

        choice = input("Choice: ").strip()
        if choice == "1":
            discord_to_ip()
        elif choice == "2":
            exit_sequence()
            break
        elif choice == "3":
            webbrowser.open("https://discord.gg/hKNW6wvyg3")
        else:
            print("Invalid input.")
            time.sleep(1)

def discord_to_ip():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        username = input("\nEnter Discord Username: ").strip()
        fake_ip = generate_fake_ip()
        print(f"\nIP address for {username}: {fake_ip}")
        again = input("\nAny more? (Y/N): ").strip().lower()
        if again != "y":
            break

def exit_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    for line in [
        "                   __         __",
        "                    $           $",
        "                          *",
        "                  /----------------\\",
        "                   Made By 17xet"
    ]:
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(line)))
        time.sleep(1)

if __name__ == "__main__":
    main_menu()
