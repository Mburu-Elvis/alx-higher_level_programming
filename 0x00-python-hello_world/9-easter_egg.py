#!/usr/bin/python3
with open("zen.txt", "r") as zen:
	line = zen.read()
print(line, end="\r")
