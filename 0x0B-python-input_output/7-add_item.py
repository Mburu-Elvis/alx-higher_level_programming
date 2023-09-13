#!/usr/bin/python3
"""Script that adds all arguments to a Python list."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
my_file = "add_item.json"
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, my_file)
load_from_json_file(my_file)
