import os

techniques_folder = os.path.dirname(os.path.realpath(__file__))
for name in os.listdir(techniques_folder): #list all techniques names
	path = f"{techniques_folder}/{name}"
	if os.path.isdir(path) and not name.startswith("_"):
		exec(f"from .{name} import obfuscate as {name}", globals(), locals())

del os
del name
del path
del techniques_folder
