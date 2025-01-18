#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def menu(*args):
  while True:
    choice = ' '.join(args) + "\n"
    inp = input(f"Select one of: \n { choice }").strip()
    if inp in args:
      print(f'You entered {inp}. Bye!')
      return None
    else:
      print(f'{inp} not found.')

if __name__ == '__main__':
  menu('a','b','c')