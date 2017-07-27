"""
Solution to challange 3:
"""
import pdb
import urllib.request

def isCap (ordCh):
	if (ordCh >= ord('A') and ordCh <= ord('Z')):
		return True
	else:
		return False

def isSmall (ordCh):
	if (ordCh >= ord('a') and ordCh <= ord('z')):
		return True
	else:
		return False

url = "http://www.pythonchallenge.com/pc/def/equality.html"
html = urllib.request.urlopen(url)

flag = False
line_count = 1
dict = {}
chrSeq = [None]*8
prev_ordCh = 0

seq_count = 0
for line in html:
	line = line.strip()
	if (line_count > 21):	# skip non-mess parts (by inspection)
		# if (line_count == 138):
			# pdb.set_trace()
		for ordCh in line:
			if (((seq_count == 3 or seq_count == 7) and isCap(ordCh)) or 
					(seq_count == 0 and isCap(prev_ordCh)) or
					((seq_count != 3 and seq_count != 7) and isSmall(ordCh))):
				chrSeq = [None]*8
				seq_count = 0
				prev_ordCh = ordCh
			else:
				chrSeq[seq_count] = ordCh
				seq_count += 1
			if (seq_count == 8):
				#print([chr(chrItem) for chrItem in chrSeq], end="\t")
				#print(line_count)
				print(chr(chrSeq[3]),end="")
				chrSeq[0:4] = chrSeq[4:8]
				seq_count = 4
	
	line_count += 1
print()

# Solution: linkedlist
