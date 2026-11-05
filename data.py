# run command:
# py data.py
class data:
    def __init__(self,variable_name,data):
        self.variable_name = variable_name
        self.data = data
    def update(self,new_data,variable_name):
        self.data = new_data
        self.variable_name = variable_name


main_menu_data= ["settings mode",
           "view mode",
           "create mode"]
settings_data=["change username",
          "show file extensions",
          "clear previous lines"]
main_menu_data = data("main_menu",main_menu_data[:])
settings_data = data("settings",settings_data[:])
username_data = data("username",None)
