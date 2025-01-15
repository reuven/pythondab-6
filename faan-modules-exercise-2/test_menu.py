"""
This script demonstrates the usage of the `menu()` function from the `menu_faan` module.

The `menu()` function is called with the arguments 'a', 'b', and 'c', representing
the menu options. The user's choice is captured and printed to the console.
"""

import menu_faan

user_choice = menu_faan.menu('a', 'b', 'c')
print(f"User selected: {user_choice}")