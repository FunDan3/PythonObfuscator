import base64
def obfuscate(code, decoder_function = None):
	if not decoder_function:
		decoder_function = "__import__('base64').b64decode(%s).decode('utf-8')"
	code = decoder_function % base64.b64encode(code.encode('utf-8'))
	code = f"exec({code})"
	return code
