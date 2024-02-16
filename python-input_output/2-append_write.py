#!/usr/bin/python3
"""Defines a file-writing function at the end of file"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
