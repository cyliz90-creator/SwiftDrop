"""
SwiftDrop
A simple CLI WiFi file transfer tool.

Author: tPowdel
"""

from swiftdrop.banner import print_banner
from swiftdrop.cli import run_cli

def main():
    print_banner()
    run_cli()

if __name__ == "__main__":
    main()