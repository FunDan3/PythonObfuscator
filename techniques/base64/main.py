import base64
def obfuscate(code):
	code = base64.b64encode(code.encode("utf-8"))
	code = f"exec(__import__('base64').b64decode({code}).decode('utf-8'))"
	return code
