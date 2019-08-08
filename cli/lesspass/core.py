import getpass
import platform
import sys
import traceback
import signal

from lesspass.version import __version__
from lesspass.cli import parse_args
from lesspass.profile import create_profile
from lesspass.password import generate_password
from lesspass.clipboard import copy, get_system_copy_command

signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))


def main(args=sys.argv[1:]):
    args = parse_args(args)
    if args.clipboard and not get_system_copy_command():
        print(
            "ERROR To use the option -c (--copy) you need pbcopy "
            + "on OSX, xsel or xclip on Linux, and clip on Windows"
        )
        sys.exit(3)

    if args.prompt_all:
        args.site = getpass.getpass("Site: ")
        args.login = getpass.getpass("Login: ")
        
        counter = getpass.getpass("Counter: ")
        if counter.isdigit():
            args.counter = int(counter)
        else:
            print("ERROR argument COUNTER must be an integer.")
            sys.exit(4)
            
        length = getpass.getpass("Length [5-35]: ")
        try:
            length = int(length)
            if length >= 5 and length <= 35:
                args.length = length
            else:
                raise
        except:
            print("ERROR argument LENGTH must be an integer in range [5-35].")
            sys.exit(4)
            
        args.nl = True if getpass.getpass("Lowercase (Y/n): ") == 'n' else False
        args.nu = True if getpass.getpass("Uppercase (Y/n): ") == 'n' else False
        args.nd = True if getpass.getpass("Digits (Y/n): ") == 'n' else False
        args.ns = True if getpass.getpass("Symbols (Y/n): ") == 'n' else False
        
    elif args.prompt:
        args.site = getpass.getpass("Site: ")
        args.login = getpass.getpass("Login: ")
    if not args.site:
        print("ERROR argument SITE is required but was not provided.")
        sys.exit(4)

    if not args.master_password:
        args.master_password = getpass.getpass("Master Password: ")
    if not args.master_password:
        print("ERROR argument MASTER_PASSWORD is required but was not provided")
        sys.exit(5)

    profile, master_password = create_profile(args)
    generated_password = generate_password(profile, master_password)

    if args.clipboard:
        try:
            copy(generated_password)
            print("Copied to clipboard")
        except Exception as e:
            print("Copy failed, we are sorry")
            print("Can you send us an email at contact@lesspass.com\n")
            print("-" * 80)
            print("Object: [LessPass][cli] Copy issue on %s" % platform.system())
            print("Hello,")
            print("I got an issue with LessPass cli software.\n")
            traceback.print_exc()
            print("-" * 80)
    else:
        print(generated_password)


if __name__ == "__main__":
    main()
