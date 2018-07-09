import re

#1877-03-03,England,Scotland,1,3,Friendly,London,England,FALSE
pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')

f = open('../../files/results.csv', 'r')

total_matches = 0

for line in f:
	res = re.match(pattern, line)
	if(res):
		date = res.group(1)
		local = res.group(2)
		visitor = res.group(3)
		local_score = int(res.group(4))
		visitor_score = int(res.group(5))
		goals_number = local_score + visitor_score
		if (goals_number >= 15):
			print('*Goals: {} Match => [{}] {}({}) - {}({})'.format(goals_number, date, local, local_score,
											 visitor, visitor_score))
			total_matches+=1
			#break

print(total_matches)

f.close()