#!/usr/bin/python3
"""Defines a file-writing function."""


def read_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)