#! /usr/bin/python3
import obfuscator

code = """
print('''test
for newlines
and "" \"\" ''') #test
"""
code = obfuscator.obfuscate(code)
with open("test_result.py", "w") as f:
	f.write("#!/usr/bin/python3\n")
	f.write(code)
