#! /usr/bin/python3
import obfuscator

with open("test_source.py", "r") as f:
	code = f.read()
code = obfuscator.obfuscate(code)
with open("test_result.py", "w") as f:
	f.write("#!/usr/bin/python3\n")
	f.write(code)
