"""
SwiftDrop
A simple CLI WiFi file transfer tool.

Author: tPowdel
Version: 0.1.0
"""

APP_NAME = "SwiftDrop"
VERSION = "0.1.0"

def print_banner():
    """ Display the application banner."""
    print("=" * 50)
    print (f"{APP_NAME} v{VERSION}")
    print("CLI WiFi File Transfer")
    print("=" * 50)

def main():
    print_banner()

if __name__ == "__main__":
    main()