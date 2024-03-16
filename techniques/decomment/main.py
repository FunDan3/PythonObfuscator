def obfuscate(code):
	code = singleline(code)
	#code = scan_for_string(code, "'''")
	#code = scan_for_string(code, '"""')
	return code

def singleline(code): #got to figure out a way how to decomment multine strings. Probably will look for characters like =; ( before it. Will need to remove whitespace first...
	quotes = ["'", '"']
	return_code = ""
	started_quote = ""
	string_started = False
	comment_started = False
	for character in code:
		if character == started_quote and string_started:
			string_started = False
		if character in quotes and not string_started:
			string_started = True
			started_quote = character
		if character == "#" and not string_started:
			comment_started = True
		if character == "\n" and comment_started:
			comment_started = False
		if not comment_started:
			return_code += character
	return return_code


def multiline(code, quote): #BROKEN YET
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
					if byte_string:
						return_code = return_code[:len(return_code)-1]
				started = not started
	return return_code
