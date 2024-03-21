from . import techniques

def obfuscate(code):
	code = techniques.decomment(code)
	code = techniques.string_encrypt(code)
	code = techniques.base64(code, decoder_function = "b64d(%s)")
	code = """b64 = __import__('base64')
b64d = lambda c: b64.b64decode(c).decode('utf-8')
""" + code
	code = techniques.string_encrypt(code)
	return code
