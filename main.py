#! /usr/bin/python3
import obfuscator
import tqdm

code = """
print('''test
for newlines
and "" \"\" ''')
"""
code = obfuscator.obfuscate(code)
print(code)
