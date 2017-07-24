"""
Solution to challange 2:
"""

#srcFile = open("2_ocr.html", "r")
# https://stackoverflow.com/questions/24755022/why-html2text-module-throws-unicodedecodeerror
# https://stackoverflow.com/questions/28610508/how-to-get-raw-html-text-of-a-given-url-using-python
# https://stackoverflow.com/questions/37042152/python-3-5-1-urllib-has-no-attribute-request
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = urllib.request.urlopen(url)

flag = False

for line in html:
	# print (line)
	if (line[:2] == "%%"):
		flag = True
	
	if (flag):
		for char in line:
			if (( char >='A' and char <= 'Z') or (char >= 'a' and char <= 'z') 
					or (ordCh in [' ', '\t', '\n'])):
				print (char, end="")

srcFile.close()
