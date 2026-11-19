import shelve
# run command:
# py data.py
with shelve.open("database") as db:
    db["main_menu"] = ["settings mode",
                        "view mode",
                        "create mode"]
    db["settings"] = {"username": None,
                      "show file extensions": None,
                      "clear previous lines": None}
