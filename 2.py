"""
Solution to challange 2:
"""
## Attempting to have the key,value automatically sorted by using Maxheap
# class KV():
	# def __init__(self, key, val):
		# self.key = key;
		# self.val = val;
		
# class Maxheap():
	# def __init__(self, key, val):
		# self.head = KV
		# self.head.key = key
		# self.head.val = val
		
		# self.left = None
		# self.right = None
	
	# def traverseDown(self):
		# prevHead = self.head
		
		
		# return prevHead
		
	# def getMax(self):
		# if(self.head is None):
			# return None
		# else:
			 
		
	# def insert(self, key, val):

# ... just use built-in solution


######
#srcFile = open("2_ocr.html", "r")
# https://stackoverflow.com/questions/24755022/why-html2text-module-throws-unicodedecodeerror
# https://stackoverflow.com/questions/28610508/how-to-get-raw-html-text-of-a-given-url-using-python
# https://stackoverflow.com/questions/37042152/python-3-5-1-urllib-has-no-attribute-request
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = urllib.request.urlopen(url)

flag = False
line_count = 0
dict = {}

for line in html:
	#print (line)
	if (line_count > 37):	# skip non-mess parts (by inspection)
		for ordCh in line:
			if ordCh not in dict:
				dict[ordCh] = [1, line_count]	# #occurance, the line which it occurred
			else:
				dict[ordCh][0] += 1				# update freq
				dict[ordCh][1] = line_count		# update line
	line_count += 1

keyList = []
for key, val in dict.items():
	if val[0] == 1:		# know that "rare" means having exactly one occurance (by inspection)
		keyList.append([val[1],chr(key)])
keyList.sort()	# sort by first element
print(keyList)

## Solution: rare characters are
## 	a, l, -, q, t, u, i, y, >
## sorted: equality


