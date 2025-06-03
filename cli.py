import argparse

parser = argparse.ArgumentParser(description="beckn-onix CLI Tool")
parser.add_argument('command', help='Command to run (init, help)')

args = parser.parse_args()

if args.command == 'init':
    print("Initializing a new Onix config...")
elif args.command == 'help':
    print("Available commands: init, help")
else:
    print("Unknown command. Use 'help' for options.")
