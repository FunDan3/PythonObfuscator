#! /usr/bin/python3
import techniques
import tqdm

code = """
print('''test
for newlines''')
"""
code = techniques.CodeSplit(code)
print(code)
