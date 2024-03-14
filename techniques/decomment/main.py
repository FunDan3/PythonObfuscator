import random

def obfuscate(code): #got to figure out a way how to decomment multine strings. Probably will look for characters like =; ( before it. Will need to remove whitespace first...
	quotes = ["'", '"']
	return_code = ""
	started_quote = ""
	string_started = False
	comment_started = False
	for character in code:
		if character in quotes and not string_started:
			string_started = True
			started_quote = character
		if character == started_quote and string_started:
			string_started = False
		if character == "#" and not string_started:
			comment_started = True
		if character == "\n" and comment_started:
			comment_started = False
		if not comment_started:
			return_code += character
	return return_code
