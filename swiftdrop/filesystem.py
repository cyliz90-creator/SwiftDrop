from pathlib import Path

class FileSystem:
    def __init__(self):
        self.current = Path.home()

    def pwd(self):
        return str(self.current)

    def ls(self):

        try:
            return sorted(self.current.iterdir())

        except Exception:
            return []

    def cd(self, folder):
        new_path = self.current / folder

        if new_path.exists() and new_path.is_dir():
            self.current = new_path
            return True

        return False
