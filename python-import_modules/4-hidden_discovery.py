#!/usr/bin/python3
import sys

module_path = '/tmp/hidden_4.pyc'

with open(module_path, 'rb') as file:
    code = marshal.load(file)

names = [name for name in code.co_names if not name.startswith('__')]

names.sort()

for name in names:
    print(name)
