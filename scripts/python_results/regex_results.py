import re

#1877-03-03,England,Scotland,1,3,Friendly,London,England,FALSE
pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.*),Friendly,.*$')

f = open('../../files/results.csv', 'r')

for line in f:
	res = re.match(pattern, line)
	if(res):
		print('* {}'.format(res.group(2)))

f.close()