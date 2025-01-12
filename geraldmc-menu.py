#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

def menu(*args):
  while True:
    for arg in args:
     inp = input(f"Select one of: {arg}")
    if inp in arg:
      print(f'You entered {inp}. Bye!')
      return None
    else:
      print(f'{inp} not found.')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--strings', nargs='+', help='Entered strings, e.g. a, b, c')
  args = parser.parse_args()
  menu(args.strings)