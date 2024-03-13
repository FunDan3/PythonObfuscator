def obfuscate(code):
	code = scan_for_string(code, "'")
	code = scan_for_string(code, '"')
	code = scan_for_string(code, "'''")
	code = scan_for_string(code, '"""')
	return code

def scan_for_string(code, quote): # really bad string parser tbh
	return_code = ""
	string_content = ""
	started = False
	for i in range(len(code)):
		quote_check = code[i:i+len(quote)] == quote
		if len(quote) == 1:
			if code[i:i+3] == quote*3 or code[i-1:i+2] == quote*3 or code[i-2:i+1] == quote*3 or code[i-3:i] == quote*3:
				quote_check = False
		if not started and not (code[i] == quote[0] and len(quote)!=1):
			return_code += code[i]
			print(code[i])
		if started and not (code[i] == quote[0] and len(quote)!=1):
			string_content += code[i]
		if quote_check:
			if started:
				return_code += on_string(string_content, quote)
			started = not started
	return return_code

def on_string(string_content, quote):
	return f"{quote}{string_content[::-1]}{quote}[::-1]" #just to test
