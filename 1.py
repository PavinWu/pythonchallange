"""
Solution to python challange 1
"""
#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "http://www.pythonchallenge.com/pc/def/map.html"
## No need to import maketrans anymore


###### ad-hoc method

def print_sp(str):
	print(str, end="")

for char in text:
	num_ch = ord(char)
	if(num_ch >= 97 and num_ch <= 120):
		print_sp(chr(num_ch+2))
	elif(num_ch > 120 and num_ch <= 122):
		print_sp(chr(num_ch-24))	#chr(y)-chr(a) == 24
	else:
		print_sp(char)
print()


###### use string.maketrans()

# transTable = maketrans("koe", "mqg")
# print (text.translate(transTable))

### Question: why not work in python3?
## https://lists.gt.net/python/python/1053035
## https://docs.python.org/3/whatsnew/3.1.html
# print (text.translate(text.maketrans("koe", "mqg")))
## New maketrans only translate individual characters.

# https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3


###### solution after applying to url
#ocr
