#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""


from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    liste = load_from_json_file(file)
except Exception:
    liste = []

""" autre methode : liste.extend(iter(argv[1:]))"""
for arg in argv[1:]:
    liste.append(arg)

save_to_json_file(liste, file)
