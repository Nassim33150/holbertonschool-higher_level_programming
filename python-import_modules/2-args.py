#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

if num_args == 0:
    print(f"{0} {'arguments'}{'.'}")
elif num_args == 1:
    print(f"{1} {'argument'}{':'}")
    print(end="")
    print(f"{1}{':'} {argv[1]}")
else:
    print(f"{num_args} {'arguments'}{':'}")
    print(end="")
    for i, arg in enumerate(argv[1:], start=1):
        print(f"{i}: {arg}")
