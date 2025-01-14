"""
1. Function menu takes any number of string arguments, presented to the user

If the user chooses one of those as a string, it's returned from the function.
If not, the user is given another chance to enter a choice.

For example:
    import menu
    user_choice=menu.menu('a','b','c')

2. Modify such that running it from cmd line asks user to enter 'a','b', or 'c' and prints the result.

3. Modify s.t. running from cmd line uses "sys.argv" to get any cmd-line args as a list of strings.
Pass them to the menu function and ask user to choose from among them. Print the user's choice.

"""
import sys


def menu(*args):

    while True:
        print("Please enter one of the choices listed.")
        for menu_choice in args:
            print(menu_choice)

        choice=input('Enter your choice: ').strip()
        if choice in args:
            return choice
        print ("That wasn't listed.")

if __name__ == '__main__':
    menu_items=[]
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            menu_items.append(arg)
    else:
        menu_items = ('a','b','c')
    actual_choice=menu(*menu_items)
    print(f"You have chosen {actual_choice}")