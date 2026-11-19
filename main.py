import data
import shelve
import os
# run command:
# py main.py
comm = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    with shelve.open('database') as db:
        if 'main_menu' not in comm:
            comm.append(db.get('main_menu', []))
        if 'username' not in comm:
            comm.append(db.get('settings', {}).get('username'))

    option = input(f"Welcome to the Main Menu!\nplease select your option:\n{comm[0]}\n> ")
    if option == "settings mode":
        settings()
    elif option == "view mode":
        view()
    elif option == "create mode":
        create()

def settings():
    if comm[1] is None:
        print("you haven't set up your settings yet, please set them up first.")
        username_input = input("let's start with your account please fill the following:\nusername (rules : use only Letters,numbers and symbols) ")
        wants_tutorial = input("great! now would you like a tutorial on how to use the program? (y/n) ")
        comm[1] = username_input
        with shelve.open('database') as db: db['settings']["username"] = username_input
        if wants_tutorial == "y":
            tutorial()
        else:
            print("ok! you can always access the tutorial later on by typing tutorial in the main menu.")
        
    print(f"great! your username is set to {comm[1]}\nnow you can change your settings anytime in the settings mode.\nto go back a step type 'back' in any mode!")
    command = ""
    show_file_extensions_val = False
    clear_previous_lines_val = False
    with shelve.open('database') as db:settings = db.get('settings', {})
    while command != "back":
        command = input(">settings: ")
        if command in settings:
            for i in settings:
                if i == 'username' and command == i:
                    username_input = input("please enter your new username (rules : use only Letters,numbers and symbols) ")
                    comm[1] = username_input
                    with shelve.open('database') as db: db['settings']["username"] = username_input
                elif i == "show file extensions" and command == i:
                    ext_choice = input("would you like to see file extensions? (y/n) ")
                    show_file_extensions_val = (ext_choice == "y")
                    comm.append(show_file_extensions_val)
                    with shelve.open('database') as db: db['settings']["show file extensions"] = show_file_extensions_val
                elif i == "clear previous lines" and command == i:
                    clear_choice = input("would you like to clear previous lines? (y/n) ")
                    clear_previous_lines_val = (clear_choice == "y")
                    comm.append(clear_previous_lines_val)
                    with shelve.open('database') as db: db['settings']["clear previous lines"] = clear_previous_lines_val
                if settings["clear previous lines"]:
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
        with shelve.open('database') as db: settings = db.get('settings', {})
        if settings["clear previous lines"]:
            clear_screen()
        main_menu()
