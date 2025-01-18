#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=argparse.FileType('r'))
args = parser.parse_args()

print(args.file.read())
