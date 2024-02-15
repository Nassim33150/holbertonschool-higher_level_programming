#!/usr/bin/python3
""" open and read a textfile """


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
