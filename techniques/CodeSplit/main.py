def obfuscate(code, chunk_size = 8):
	chunks = [code[i:i+chunk_size] for i in range(0, len(code), chunk_size)]
	code = ""
	for i in range(len(chunks)):
		nl = "\n"
		snl = "\\n"
		code += f"'{process_quotes(chunks[i]).replace(nl, snl)}'"
		if i!=len(chunks)-1:
			code += "+"
	code = f"exec({code})"
	return code

def process_quotes(code): #has issues with \' but I have no idea how to fix it really
	code = code.replace("'", "\\'").replace('"', '\\"')
	return code
