def obfuscate(code):
	idents = normalize_idents(calc_idents(code))
	lines = code.split("\n")
	new_code = ""
	code_segment = ""
	for line_number in range(len(lines)):
		if idents[line_number]:
			code_segment += line
		else:
			pass

def deident(code, depth = -1):
	lines = code.split("\n")
	new_code = "\n"
	new_lines = []
	for line_number in range(len(lines)):
		new_line = ""
		for character_number in range(len(characters)):
			if (character_number < depth or depth < 0) and lines[line_number][character_number] in " \t":
				continue
			else:
				new_line += lines[line_number][character_number]
		new_lines.append(new_line)
	return new_code.join(new_lines)


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
