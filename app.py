#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    amity create_room <room_name>...
    amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_accomodation>]
    amity reallocate_person <person_name> <new_room_name>
    amity remove_person <person_identifier>
    amity load_people <filename>
    amity print_allocations [-o <filename>]
    amity print_unallocated [-o <filename>]
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)
    amity (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app.amity import my_amity
from app.person import person
from app.rooms import my_room
from app.database import amity_db
from termcolor import cprint, colored
from pyfiglet import figlet_format


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):

    cprint(figlet_format('AMITY', font='univers'), 'green', attrs=['bold'])

    def introduction():
        cprint("\n")
        cprint("ROOM ALLOCATION COMMANDS:".center(40), 'green')
        cprint("\n")
        cprint("1. create_room <room_name>...".center(40), 'green')
        cprint(
            "2. add_person <first_name> <last_name> (Fellow|Staff)"
            "[<wants_accomodation>]".center(40), 'green')
        cprint(
            "3. reallocate_person <person_name> <new_room_name>".center(
                40), 'green')
        cprint(
            "4. remove_person <person_name>".center(40), 'green')
        cprint("5. load_people <filename>".center(40), 'green')
        cprint("6. print_allocations [-o <filename>]".center(40), 'green')
        cprint("7. print_unallocated [-o <filename>]".center(40), 'green')
        cprint("8. print_room <room_name>".center(40), 'green')
        cprint("9. save_state [--db=sqlite_database]".center(40), 'green')
        cprint("10. load_state <sqlite_database>".center(40), 'green')
        cprint("\n")
        cprint("OTHER COMMANDS:".center(40), 'green')
        cprint("\n")
        cprint("1. -h, --help, help".center(40), 'green')
        cprint("2. quit".center(40), 'green')
        cprint("\n\n")

    intro = introduction()

    prompt = '(amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_name>..."""
        
        print(my_amity.create_room(args))

    @docopt_cmd
    def do_add_person(self, args):
        """Usage:
        add_person <first_name> <last_name> (Fellow|Staff) [<wants_accomodation>]"""
        print(person.add_person(args))

    @docopt_cmd
    def do_remove_person(self, args):
        """Usage:
        remove_person <person_name>"""

        print(person.remove_person(args))

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage:
        reallocate_person <person_name> <new_room_name>"""

        print(person.reallocate_person(args))

    @docopt_cmd
    def do_load_people(self, args):
        """Usage:
        load_people <filename>

                Sample Input Format:

                OLUWAFEMI SULE FELLOW Y
                DOMINIC WALTERS STAFF
                SIMON PATTERSON FELLOW Y
                MARI LAWRENCE FELLOW Y
                LEIGH RILEY STAFF
                TANA LOPEZ FELLOW Y
                KELLY McGUIRE STAFF N
        """
        print(person.load_people(args))

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage:
        print_allocations [-o <filename>]
        """
        print(my_room.print_allocations(args))

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage:
        print_unallocated [-o <filename>]"""
        print(my_room.print_unallocated(args))

    @docopt_cmd
    def do_print_room(self, args):
        """Usage:
        print_room <room_name>

        """
        print(my_room.print_room(args))

    @docopt_cmd
    def do_save_state(self, args):
        """Usage:
        save_state [--db=sqlite_database]"""
        print(amity_db.save_state(args))

    @docopt_cmd
    def do_load_state(self, args):
        """Usage: \
        load_state <sqlite_database>"""
        print(amity_db.load_state(args))

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print(amity_db.save_state({"--db": 'amity.db'}))
        print('Good Bye!')
        exit()


print(amity_db.load_state({"<sqlite_database>": 'amity.db'}))
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
