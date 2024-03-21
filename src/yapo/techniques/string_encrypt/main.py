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
				(i in range(1, len(code)-2) and code[i-1] == quote[0] and code[i-2] == quote[0]) or
				(i in range(1, len(code)-2) and code[i+1] == quote[0] and code[i+2] == quote[0]) or
				(i in range(1, len(code)-1) and code[i-1] == quote[0] and code[i+1] == quote[0]))
			if not started and not in_tripple_quote:
				return_code += code[i]
			if started and not in_tripple_quote:
				string_content += code[i]
			if quote_check:
				if started:
					return_code += on_string(string_content, quote, byte_string, special_string)
					string_content = ""
				else:
					special_string = code[i-1] == "f" # f-string
					byte_string = code[i-1] == "b" # b-string
					if byte_string:
						return_code = return_code[:len(return_code)-1]
				started = not started
		if len(quote) == 1:
			quote_check = code[i] == quote
			in_tripple_quote = False
			if i in range(1, len(code)-2):
				quote_check = quote_check and not (code[i-1] == quote or code[i+1] == quote)
				in_tripple_quote = code[i] == quote[0] and (code[i-1] == quote[0] or code[i+1] == quote[0])
			if not started and not (code[i] == quote and not in_tripple_quote):
				return_code += code[i]
			if started and not (code[i] == quote and not in_tripple_quote):
				string_content += code[i]
			if quote_check:
				if started:
					return_code += on_string(string_content, quote, byte_string, special_string)
					string_content = ""
				else:
					special_string = code[i-1] == "f" # f-string
					byte_string = code[i-1] == "b" # b-string
					if byte_string:
						return_code = return_code[:len(return_code)-1]

				started = not started
	return return_code
def on_string(string_content, quote, byte_string, f_string):
	banned = ["\n", "\\"]

	if f_string:
		arguments = []
		argument_started = False
		argument = ""
		new_string_content = ""
		for character in string_content:
			if character == "}":
				arguments.append(argument)
				argument = ""
				argument_started = False
			if character == "{":
				argument_started = True
			if argument_started and character != "{":
				argument += character
			if not argument_started or character == "{":
				new_string_content += character

		new_string_content = new_string_content.replace("{}", "%s")
		real_arguments = "("
		for i in range(len(arguments)):
			obfuscated_argument = obfuscate(f"'{arguments[i]}'")
			real_arguments += f"eval({obfuscated_argument})"
			if i != len(arguments)-1:
				real_arguments += ","
		real_arguments += ")"

		password = ""
		banned = ["\n", "\\", "'"]
		for character in new_string_content:
			addition = random.randint(ord(character), ord(character)+100)
			while True:
				try:
					eval(f"'{chr(addition)}'")
					eval(f"'{chr(ord(character)+addition)}'")
				except Exception:
					addition += random.randint(-1, 1)
					continue
				try:
					is_string = eval(f"{chr(addition)}IS_STRING_CHARACTER{chr(addition)}")=="IS_STRING_CHARACTER"
					if is_string:
						addition += random.randint(-1, 1)
						continue
				except Exception:
					pass
				if not (chr(addition).isprintable() and chr(ord(character) + addition).isprintable()):
					addition += random.randint(-1, 1)
					continue
				if chr(addition) in banned or chr(ord(character)+addition) in banned:
					addition += random.randint(-1, 1)
					continue
				break
			password += chr(addition)
		encrypted_string_content = decrypt_function % ("'"+encrypt_function(new_string_content, password)+"'", "'" + password + "'")
		return f"{encrypted_string_content} % {real_arguments}"
	else:
		type_processor = "%s"
		if byte_string:
			string_content = f"b{quote}{string_content}{quote}"
			type_processor = "eval(%s)"
		password = ""
		for character in string_content:
			addition = random.randint(ord(character), ord(character)+100)
			while True:
				try:
					eval(f"'{chr(addition)}'")
					eval(f"'{chr(ord(character)+addition)}'")
				except Exception:
					addition += random.randint(-1, 1)
					continue
				try:
					is_string = eval(f"{chr(addition)}IS_STRING_CHARACTER{chr(addition)}")=="IS_STRING_CHARACTER"
					if is_string:
						addition += random.randint(-1, 1)
						continue
				except Exception:
					pass
				if not (chr(addition).isprintable() and chr(ord(character) + addition).isprintable()):
					addition += random.randint(-1, 1)
					continue
				if chr(addition) in banned or chr(ord(character)+addition) in banned:
					addition += random.randint(-1, 1)
					continue
				break
			password += chr(addition)

		return type_processor % decrypt_function % (("'" + encrypt_function(string_content, password) + "'"), "'" + password + "'")
