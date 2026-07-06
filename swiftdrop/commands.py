import os
from swiftdrop.filesystem import FileSystem
fs = FileSystem()

def execute (command: str) -> bool:
    command = command.strip().lower()

    if command == "":
        return True

    if command == "help":
        print()
        print("Available commands:")
        print("  help  Show this help")
        print("  version Show Program Version")
        print("  clear  Clear the screen")
        print("  exit Quit SwiftDrop")
        print("  pwd Show the current working directory")
        print("  ls Show the list of filesystems")
        print("  cd <folder> Change the current working directory")
        print()

        return True

    if command == "version":
        print("SwiftDrop version 0.2.0")
        return True

    if command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        return True

    if command == "exit":
        return False

    if command == "pwd":
        print(fs.pwd())
        return True

    if command == "ls":
        for item in fs.ls():
            if item.is_dir():
                print("[DIR]", item.name)
            else:
                print("      ", item.name)

        return True

    if command.startswith("cd "):
        folder = command[3:].strip()
        if fs.cd(folder):
            print("Directory changed.")
        else:
            print("Directory not found.")

        return True

    print(f"Unknown command: {command}")
    print("Type 'help' for available commands.")
    return True

