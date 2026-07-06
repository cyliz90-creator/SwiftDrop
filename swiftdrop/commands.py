import os

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

    print(f"Unknown command: {command}")
    print("Type 'help' for available commands.")
    return True

