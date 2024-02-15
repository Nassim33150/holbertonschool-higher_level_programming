#!/usr/bin/python3
""" open and read a textfile """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
