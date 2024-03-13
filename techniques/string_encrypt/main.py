import random
trash = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~ "
def obfuscate(code, encrypt_function = None, decrypt_function = None):
	trash_size = random.randint(16, 32)
	if not encrypt_function:
		encrypt_function = default_encrypt(trash_size) #not actual encryption but IDC
	if not decrypt_function:
		decrypt_function = f"%s[::-{trash_size}]"
	code = scan_for_string(code, "'''", encrypt_function, decrypt_function)
	code = scan_for_string(code, '"""', encrypt_function, decrypt_function)
	code = scan_for_string(code, "'", encrypt_function, decrypt_function)
	code = scan_for_string(code, '"', encrypt_function, decrypt_function)
	return code

def scan_for_string(code, quote, encrypt_function, decrypt_function): # really bad string parser tbh
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
					return_code += on_string(string_content, quote, encrypt_function, decrypt_function)
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
					return_code += on_string(string_content, quote, encrypt_function, decrypt_function)
				started = not started
	return return_code

def on_string(string_content, quote, encrypt_function, decrypt_function):
	return decrypt_function % (quote + encrypt_function(string_content) + quote)

def default_encrypt(size):
	def encrypt(data):
		new_data = ""
		for chr in data:
			new_data += chr
			for _ in range(size-1):
				new_data += random.choice(trash)
		return new_data[::-1]
	return encrypt
