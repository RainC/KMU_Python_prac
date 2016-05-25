import re
import operator

f = open("voca.txt","r")
data = f.read().split()

count = 0
voca = {}
for lists in data:
	aa = re.match("[a-z]*$", lists)
	if (aa):
		if not(lists in voca):
			voca[lists] = 0

		plus_count = voca[lists] + 1
		voca[lists] = plus_count

sorted_x = sorted(voca.items(), key=operator.itemgetter(1), reverse= True)
print(sorted_x)
