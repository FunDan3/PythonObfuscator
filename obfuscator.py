import base64
import techniques

def obfuscate(code):
	code = techniques.base64(code, decoder_function = "b64d(%s)")
	code = """b64 = __import__('base64')
b64d = lambda c: b64.b64decode(c).decode('utf-8')
""" + code
	return code
