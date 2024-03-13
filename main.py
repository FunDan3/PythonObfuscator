#! /usr/bin/python3
import techniques
import tqdm

code = "print('test')"
code = techniques.base64(code)
print(code)
