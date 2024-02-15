#!/usr/bin/python3
""" open and read a textfile """


def read_file(filename=""):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
    file.close()
