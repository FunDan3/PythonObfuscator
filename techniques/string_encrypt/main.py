import random

def encrypt_function(data, password):
	new_data = ""
	for i in range(len(data)):
		addition = password.split(";")[i]
		new_data += str(ord(data[i])+int(addition)) + (";" if not i == len(data)-1 else "")
	return new_data
decrypt_function = f"''.join([chr(int(i)-int(j)) for i, j in zip(%s.split(';'), %s.split(';'))])"

def obfuscate(code):
	code = scan_for_string(code, "'''")
	code = scan_for_string(code, '"""')
	code = scan_for_string(code, '"')
	code = scan_for_string(code, "'")
	return code

def scan_for_string(code, quote): # really bad string parser tbh
	return_code = ""
	string_content = ""
	started = False
	for i in range(len(code)):
		if len(quote) == 3:
			quote_check = code[i:i+len(quote)] == quote
			in_tripple_quote = code[i] == quote[0] and (code[i-1] == quote[0] or code[i+1] == quote[0])
			if not started and not in_tripple_quote:
				return_code += code[i]
			if started and not in_tripple_quote:
				string_content += code[i]
			if quote_check:
				if started:
					return_code += on_string(string_content, quote)
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
					return_code += on_string(string_content, quote)
				started = not started
	return return_code

def on_string(string_content, quote):
	password = ";".join([str(random.randint(-99, 99)) for _ in range(len(string_content))])
	return decrypt_function % ((quote + encrypt_function(string_content, password) + quote), '"' + password + '"')
