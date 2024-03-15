import random

def encrypt_function(data, password):
	new_data = ""
	for i in range(len(data)):
		addition = password[i]
		new_data += chr(ord(data[i])+ord(addition))
	return new_data
decrypt_function = f"''.join([chr(ord(i)-ord(j)) for i, j in zip(%s, %s)])"

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
	special_string = False
	byte_string = False
	for i in range(len(code)):
		if len(quote) == 3:
			quote_check = code[i:i+len(quote)] == quote
			in_tripple_quote = code[i] == quote[0] and (
				(code[i-1] == quote[0] and code[i-2] == quote[0]) or
				(code[i+1] == quote[0] and code[i+2] == quote[0]) or
				(code[i-1] == quote[0] and code[i+1] == quote[0]))
			if not started and not in_tripple_quote:
				return_code += code[i]
			if started and not in_tripple_quote:
				string_content += code[i]
			if quote_check:
				if started:
					if not special_string:
						return_code += on_string(string_content, quote, byte_string)
					else:
						return_code += quote + string_content + quote
					string_content = ""
				else:
					special_string = code[i-1] == "f" # f-string
					byte_string = code[i-1] == "b" # b-string
					if byte_string:
						return_code = return_code[:len(return_code)-1]
				started = not started
		if len(quote) == 1:
			quote_check = code[i] == quote and not (code[i-1] == quote or code[i+1] == quote)
			in_tripple_quote = code[i] == quote[0] and (code[i-1] == quote[0] or code[i+1] == quote[0])
			if not started and not (code[i] == quote and not in_tripple_quote):
				return_code += code[i]
			if started and not (code[i] == quote and not in_tripple_quote):
				string_content += code[i]
			if quote_check:
				if started:
					if not special_string:
						return_code += on_string(string_content, quote, byte_string)
					else:
						return_code += quote + string_content + quote
					string_content = ""
				else:
					special_string = code[i-1] == "f" # f-string
					byte_string = code[i-1] == "b" # b-string
					if byte_string:
						return_code = return_code[:len(return_code)-1]

				started = not started
	return return_code

def on_string(string_content, quote, byte_string):
	type_processor = "%s"
	if byte_string:
		string_content = f"b{quote}{string_content}{quote}"
		type_processor = "eval(%s)"
	password = ""
	banned = ["\n", "\\", "'"]
	for character in string_content:
		addition = random.randint(ord(character), ord(character)+100)
		while chr(addition) in banned or chr(ord(character)+addition) in banned:
			addition += 1
		password += chr(addition)
	return type_processor % decrypt_function % (("'" + encrypt_function(string_content, password) + "'"), "'" + password + "'")
