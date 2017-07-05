import sys, random
# "lis", {"a"->3, "b"->10}

name_distribution = dict()
N = 4
debug = False
names = []

while True:
	line = sys.stdin.readline()
	if not line:
		break

	line = line.strip()
	names.append(line)
	line = ' ' + line + ' '

	for i in range(1, len(line)):
		sub = line[max(0,i-N):i]
		if sub not in name_distribution:
			name_distribution[sub] = dict()
		d = name_distribution[sub]

		next_char = line[i]
		if next_char not in d:
			d[next_char] = 1
		else:
			d[next_char] = d[next_char] + 1

if debug:
	print name_distribution.keys()
	print len(name_distribution)
	print name_distribution[' ']
	print len(name_distribution[' '])

def get_next_most_probable_char(prefix):
	dist = name_distribution[prefix]
	total_occurances = sum(dist.values())
	current_prob = 0.0
	probarray = []
	for k in dist.keys():
		current_prob += float(dist[k])/float(total_occurances)
		probarray.append((k, current_prob))

	if debug:
		print probarray

	r = random.random()
	for t in probarray:
		if r < t[1]:
			return t[0]
	return probarray[-1][0]

def get_random_name():
	c = get_next_most_probable_char(' ')
	name = c
	while True:
		prefix = ' ' + name
		# " S"
		tail = N
		if len(prefix) < tail:
			tail = len(prefix)
		if debug:
			print prefix[-tail:]
		c = get_next_most_probable_char(prefix[-tail:])
		if c == ' ':
			break
		name += c
		if debug:
			print c
	return name

i = 0
while i < 10:
	name = get_random_name()
	if name not in names:
		print name
		i += 1