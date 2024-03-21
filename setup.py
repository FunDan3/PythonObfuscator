import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name = "YAPythonObfuscator",
	version = "0.0.4",
	author = "Fun_Dan3",
	author_email = "dfr34560@gmail.com",
	description = "Yet another python obfuscator",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/FunDan3/PythonObfuscator/",
	project_urls = {
		"Bug Tracker": "https://github.com/FunDan3/PythonObfuscator/issues"
	},
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	packages = setuptools.find_packages(where = "src"),
	package_dir = {"": "src"},
	python_requires = ">=3.8",
)
