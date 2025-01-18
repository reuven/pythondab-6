#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

def menu(args):
  while True:
    inp = input(f"Select one of: {args}")

    if inp in args:
      print(f'You entered {inp}. Bye!')
      break

    else:
      print(f'{inp} not found.')

if __name__ == '__main__':
  print(f'{sys.argv=}')

  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--strings', nargs='+', help='Entered strings, e.g. a b c')
  args = parser.parse_args()
  menu(args.strings)
