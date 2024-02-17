#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list = sys.argv[1:]

""" load the object JSON file """
loaded = load_from_json_file('add_item.json')

""" save the list python in text file JSON """
save_to_json_file(loaded + list, 'add_item.json')
