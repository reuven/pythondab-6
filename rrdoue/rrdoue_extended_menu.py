"""This module provides an interactive menu function.  The function builds a numbered menu from the argument list,
asking the user to enter a number instead of the choice's text.  This enables a user to enter a short (usually
one-character) value in the event of choices with larger amounts of text.

Functions: - menu(*args): Repeatedly prompts the user to select an option from a list of string arguments. Returns
the selected option when a valid input is provided. """


def menu(*args):  # accept any number of arguments
    """Repeatedly prompts the user to select an option from a list of string arguments presented to the user.

    :param args: Arbitrary string arguments representing the menu options.
    :returns: The user's choice from the list of arguments.
    """

    debug = False

    key_lookup = {}

    if debug:
        print(f'(in debug) Indexes and Values')

    for idx, argument in enumerate(args, start=1):
        key_lookup[str(idx)] = argument
        if debug:
            print(f'{idx}: {argument}')

    if debug:
        print(f'(in debug) Building ui presentation based on dictionary: \n{key_lookup}\n')

    print(f'Choices:\n')
    for key, value in key_lookup.items():
        print(f'({key})  {value}')

    while True:

        user_response: str = input(f'\nPlease enter one of the numbers (without parentheses) as your choice: ').strip()

        if user_response in key_lookup.keys():
            return key_lookup[user_response]
        else:
            print(f'\n{user_response} is not a valid choice, please try again.')
            continue
