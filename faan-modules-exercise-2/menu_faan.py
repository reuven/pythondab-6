# (1) Write a module, "menu.py", in which you define a single function,  "menu". This function should take any number of string arguments,  which are then presented to the user.
#
# If the user chooses one of the arguments (as a string), then that  string is returned from the function.  If not, then the user is  given another chance to enter a choice.
#
# For example:
#
#         import menu
#         user_choice = menu.menu('a', 'b', 'c')
#
# (2) Modify your module, such that running it from the command line asks the user to enter 'a', 'b', or 'c' and then prints the result.
#
# (3) Now modify your module further, such that running it from the command line uses "sys.argv" to get any command-line
# arguments as a list of strings.  Pass those strings to the "menu" function, and ask the user to choose from among them.
# Print the user's choice.

"""
This module provides an interactive menu function.

Functions:
- menu(*args): Repeatedly prompts the user to select an option from a list of string arguments. Returns the selected option when valid input is provided.

If run as a script, this module will do nothing.
"""

def menu(*args):
    """
    Repeatedly prompts the user to choose from a list of provided arguments.

    Args:
        *args: Arbitrary string arguments representing the menu options.

    Returns:
        str: The selected option that matches one of the provided arguments.
    """
    while True:
        user_selection = input(f"Select one of: {args} : ").strip()
        if user_selection in args:
            return user_selection
        else:
            print(f'{user_selection} not found.')
            continue


if __name__ == '__main__':
    pass

