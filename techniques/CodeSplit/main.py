def obfuscate(code, chunk_size = 8):
	chunks = [code[i:i+chunk_size] for i in range(0, len(code), chunk_size)]
	code = ""
	for i in range(len(chunks)):
		code += f'"{chunks[i]}"'
		if i!=len(chunks)-1:
			code += "+"
	code = f"exec({code})"
	return code
