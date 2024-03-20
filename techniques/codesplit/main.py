def obfuscate(code):
	idents = normalize_idents(calc_idents(code))

def normalize_idents(idents):
        minimal_ident = min([ident if ident else 2**32 for ident in idents]) #get minimal element except the '0'
        normalized_idents = [int(ident / minimal_ident) for ident in idents]
        return normalized_idents

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
