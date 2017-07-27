import urllib.request, urllib.error
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothingNum = '63579'

error = False
while (not error):
	newurl = url + nothingNum
	try:
		html = urllib.request.urlopen(newurl)
		text = html.read().decode('utf-8')
		#matchObj = re.match(r'[^0-9]*([0-9]*[^0-9]*)*([0-9]+)', text)	# text,(number,text)*(number)	# last number won't be in first group
			##have not tested
		matchObj = re.match(r'[^0-9]*([0-9]+)', text)
		nothingNum = matchObj.group(1)
		print(nothingNum)
		
	except (urllib.error.URLError, AttributeError) as e:
		print(e)
		error = True
	
## https://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string

# 8022 -> ... -> 82683 -> 63579 -> 66831
# peak.html