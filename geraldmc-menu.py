#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def menu(*args):
  while True:
    choices = ' '.join(args)
    choice = choices + "\n"
    inp = input(f"Select one of: \n { choice }").strip()
    if inp in args:
      print(f'You entered {inp}. Bye!')
      return None
    else:
      print(f'{inp} not found.')