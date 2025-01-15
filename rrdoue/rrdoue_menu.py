#! /usr/bin/env python3
"""The rrdoue_menu module, with one function, when called with any number of arguments, asks a user to choose from a list of the arguments and returns the user's choice. For example, rrdoue_menu.menu('1', '2', '3', '4', '5')
When run from the command line, execute the script with any number of choices (not quoted) separated by spaces.  For example, python3 <script_name>.py a b c"""


from sys import argv

def menu(*args):
    """
    :param args: Any number of arguments in the form of a comma-separated single-quoted list.
    :return: The user's choice from the list of arguments.
    """

    debug = False

    while True:

        user_response: str = input(f'Please enter your choice, one of {args}: ')

        if user_response in args:
            if debug:
                print(f'User choice is {user_response}')
            return user_response

        print(f'"{user_response}" is not valid, please try again.')


if __name__ == "__main__":
    if argv[1] == '-h' or argv[1] == '--help':
        print('Execute the script from the command line with any number of choices (not quoted) separated by spaces.  '
              'For example, python3 <script_name>.py a b c')
    else:
        print(f"'{menu(*argv[1:])}'")
