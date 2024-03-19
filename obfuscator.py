import base64
import techniques

def obfuscate(code):
	print("Decommenting...")
	code = techniques.decomment(code)
	print("Encrypting strings for main code...")
	code = techniques.string_encrypt(code)
	print("Base64 encoding main code...")
	code = techniques.base64(code, decoder_function = "b64d(%s)")
	print("Encrypting strings for encoded code...")
	code = """b64 = __import__('base64')
b64d = lambda c: b64.b64decode(c).decode('utf-8')
""" + code
	code = techniques.string_encrypt(code)
	return code
