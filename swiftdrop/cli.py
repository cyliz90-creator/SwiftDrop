from swiftdrop.commands import execute

def run_cli():
    running = True

    while running:
        command = input("swiftdrop> ")
        running = execute(command)