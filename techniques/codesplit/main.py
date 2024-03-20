def obfuscate(code):
	idents = calc_idents(code)

def calc_idents(code):
	lines = code.split("\n")
	idents = []
	for line in lines:
		ident_level = 0
		for character in line:
			if character in " \t":
				ident_level += 1
			else:
				break
		idents.append(ident_level)
	return idents
