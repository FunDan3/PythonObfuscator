def obfuscate(code):
	code = singleline(code)
	code = multiline(code, "'''")
	code = multiline(code, '"""')
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
	string_start = 0
	started = False
	for i in range(len(code)):
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
				comment = True
				for j in range(string_start):
					character = code[string_start-j-1]
					if character in " \t\n":
						continue

					if character in "[,=(":
						comment = False
						break
					else:
						comment = True
						break
				if not comment:
					return_code += quote + string_content + quote
			else:
				string_content = ""
				string_start = i
			started = not started
	return return_code
