from data import *
import os
# run command:
# py main.py

comm = {"show_file_extensions": False,
    "clear_previous_lines": False,
    "username": None,
    "wants_tutorial": "n/a"}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    option = input(f"Welcome to the Main Menu!\nplease select your option:\n{main_menu_data.data}\n> ")
    if option == "settings mode":
        settings()
    elif option == "view mode":
        view()
    elif option == "create mode":
        create()

def settings():
    if comm.get("clear_previous_lines"):
        clear_screen()
    if username_data.data is None:
        print("you haven't set up your settings yet, please set them up first.")
        username_input = input("let's start with your account please fill the following:\nusername (rules : use only Letters,numbers and symbols) ")
        wants_tutorial = input("great! now would you like a tutorial on how to use the program? (y/n) ")
        comm["username"] = username_input
        username_data.update(username_input,"username")
        comm["wants_tutorial"] = wants_tutorial
        if wants_tutorial == "y":
            tutorial()
        else:
            print("ok! you can always access the tutorial later on by typing tutorial in the main menu.")
        
    print(f"great! your username is set to {comm['username']} and your tutorial preference is set to {comm['wants_tutorial']}.\nnow you can change your settings anytime in the settings mode.\nto go back a step type 'back' in any mode!")
    
    command = ""
    show_file_extensions_val = False
    clear_previous_lines_val = False

    while command != "back":
        command = input(">settings: ")
        if command in settings_data.data:
            for i in settings_data.data:
                if i == settings_data.data[0] and command == i:
                    username_input = input("please enter your new username (rules : use only Letters,numbers and symbols) ")
                    comm["username"] = username_input
                elif i == settings_data.data[1] and command == i:
                    ext_choice = input("would you like to see file extensions? (y/n) ")
                    show_file_extensions_val = (ext_choice == "y")
                    comm["show_file_extensions"] = show_file_extensions_val
                elif i == settings_data.data[2] and command == i:
                    clear_choice = input("would you like to clear previous lines? (y/n) ")
                    clear_previous_lines_val = (clear_choice == "y")
                    comm["clear_previous_lines"] = clear_previous_lines_val
                if comm.get("clear_previous_lines"):
                    clear_screen()


def tutorial():
    pass

def view():
    pass

def create():
    pass

if __name__ == "__main__":
    while True:
        # main logic goes here.
        if comm.get("clear_previous_lines", False):
            clear_screen()
        main_menu()
