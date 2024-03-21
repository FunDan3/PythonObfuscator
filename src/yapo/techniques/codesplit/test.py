#! /usr/bin/python3
from main import obfuscate

code = """x = input("x = ")
if x-10:
	print("tetra")
else:
	print("betra")"""

print(obfuscate(code))
