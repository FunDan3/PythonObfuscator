#! /usr/bin/python3
import main

code = """
print('te#st')
'''emt
comment test
'''
print('''test
DIE''') #comment
"""

print(main.obfuscate(code))
