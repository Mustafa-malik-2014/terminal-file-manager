from data import *
import os
# run command:
# py main.py

comm = {}

def main_menu():
    option = input(f"Welcome to the Main Menu!\nplease select your option:\n{main_menu_data.data}\n> ")
    if option == "settings mode":
        settings()
    elif option == "view mode":
        view()
    elif option == "create mode":
        create()

def settings():
    print("you haven't set up your settings yet, please set them up first.")
    username_input = input("let's start with your account please fill the following:\nusername (rules : use only Letters,numbers and symbols) ")
    wants_tutorial = input("great! now would you like a tutorial on how to use the program? (y/n) ")
    if wants_tutorial == "y":
        tutorial()
    else:
        print("ok! you can always access the tutorial later on by typing tutorial in the main menu.")
        
    print(f"great! your username is set to {username_input} and your tutorial preference is set to {wants_tutorial}.\nnow you can change your settings anytime in the settings mode.\nto go back a step type 'back' in any mode!")
    
    command = ""
    show_file_extensions_val = False
    clear_previous_lines_val = False

    while command != "back":
        command = input(">settings: ")
        if command in settings_data.data:
            for i in settings_data.data:
                if i == settings_data.data[0] and command == i:
                    username_input = input("please enter your new username (rules : use only Letters,numbers and symbols) ")
                elif i == settings_data.data[1] and command == i:
                    ext_choice = input("would you like to see file extensions? (y/n) ")
                    show_file_extensions_val = (ext_choice == "y")
                elif i == settings_data.data[2] and command == i:
                    clear_choice = input("would you like to clear previous lines? (y/n) ")
                    clear_previous_lines_val = (clear_choice == "y")
    comm["show_file_extensions"] = show_file_extensions_val
    comm["clear_previous_lines"] = clear_previous_lines_val
    comm["username"] = username_input
    username_data.update(username_input, "username")
    main_menu()

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
            os.system("cls")
        main_menu()