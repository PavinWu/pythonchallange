"""
Solution to python challange 1

Should be used with python 3
"""

def print_sp(str):
	print(str, end="")

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for char in text:
	num_ch = ord(char)
	if(num_ch >= 97 and num_ch <= 120):
		print_sp(chr(num_ch+2))
	elif(num_ch > 120 and num_ch <= 122):
		print_sp(chr(num_ch-24))	#chr(y)-chr(a) == 24
	else:
		print_sp(char)
print()

# use string.maketrans()

		
