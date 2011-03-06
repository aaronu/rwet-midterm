import sys
import re

lines = list()
for line in sys.stdin:
	line = line.strip()
	lines.append(line)

guinness = [r'^[Gg].+[Gg]$', r'^[Uu].+[Uu]$', r'^[Ii].+[Ii]$', r'^[Nn].+[Nn]$', r'^[Nn].+[Nn]$', r'^[Ee].+[Ee]$', r'^[Ss].+[Ss]$', r'^[Ss].+[Ss]$']

for pattern in guinness:
	for line in lines:
		if re.search(pattern, line):
			print line
			break # will exit the inner-most for loop

	