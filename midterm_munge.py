import sys
import re
import random


lines = list()

for line in sys.stdin:
	line = line.strip()
	lines.append(line)
while len(lines) > 0:
		print " ".join(random.sample(lines, len(lines))) #mixes up the lines (but not the words in the lines)
		break

