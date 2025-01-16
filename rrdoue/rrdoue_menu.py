#! /usr/bin/env python3
"""The rrdoue_menu module, with one function, when called with any number of arguments, asks a user to choose from the list of arguments and returns the user's choice. For example, "rrdoue_menu.menu('1', '2', '3', '4', '5')".
When run from the command line, execute the script with any number of choices (not quoted) separated by spaces.  For example, "python3 rrdoue_menu.py a b c".  However, if executed from the command line without any parameters, the script executes a standard menu including a, b, and c.
Brief command-line help is available by calling the script with -h or --help."""

import sys


def menu(*args):
    """
    :param args: Any number of string arguments in the form of a comma-separated single-quoted list.
    :return: The user's choice from the list of arguments.
    """

    options = '/'.join(args)  # Reuven used this in his solution

    while True:

        user_response: str = input(f'Please enter a choice, one of {options}: ')

        if user_response in args:
            return user_response

        print(f'"{user_response}" is not valid, please try again.')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Using default choices a, b, and c')
        user_choice = menu('a', 'b', 'c')
        print(f'You chose `{user_choice}`.')
    elif (len(sys.argv) == 2
          and sys.argv[1] == '-h'
          or sys.argv[1] == '--help'):
        print('Execute the script from the command line with any number of choices (not quoted) separated by spaces.  '
              'For example, "python3 rrdoue_menu.py a b c"')
        exit()
    else:
        user_choice = menu(*sys.argv[1:])
        print(f'You chose `{user_choice}`.')
