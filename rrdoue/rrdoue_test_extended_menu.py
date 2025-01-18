import rrdoue_extended_menu

print(f'\n* Meta announced this week that it was making what change to its popular social media apps, Facebook, '
      f'Instagram and Threads?\n')

user_choice = rrdoue_extended_menu.menu('Every post will need to be approved by a Meta employee.', 'Fact-checkers '
                                        'will no longer police content.', 'Teenagers will no longer be able to make '
                                        'accounts.', 'The apps will no longer allow political posts.', 'Users will '
                                        'need to pay $10 a month for access.')

print(f'\nYou chose \'{user_choice}\'.\n')

print(f'* Note:  With respect to the New York Times, the question was taken from one of their weekly news quiz '
      f'articles.\n')
