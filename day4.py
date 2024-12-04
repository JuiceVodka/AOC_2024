file = open("d4.txt", "r")
lines = [list(line[:-1]) if "\n" == line[-1] else list(line) for line in file.readlines()]

import numpy as np
lines = np.array(lines)

#part 1


diags = [lines[::-1,:].diagonal(i) for i in range(-lines.shape[0]+1,lines.shape[1])]
diags.extend(lines.diagonal(i) for i in range(lines.shape[1]-1,-lines.shape[0],-1))


lines_combined = ["".join(lines[i, :]) for i in range(lines.shape[0])]
columns_combined = ["".join(lines[:, i]) for i in range(lines.shape[1])]
diags_combined = ["".join(n.tolist()) for n in diags]


import re

total_matches = 0
for row in lines_combined:
	row_matches = re.findall(r"XMAS", row)
	row_matches_2 = re.findall(r"XMAS", row[::-1])
	total_matches += len(row_matches) + len(row_matches_2)

for column in columns_combined:
	column_matches = re.findall(r"XMAS", column)
	column_matches_2 = re.findall(r"XMAS", column[::-1])
	total_matches += len(column_matches) + len(column_matches_2)

for diag in diags_combined:
	diag_matches = re.findall(r"XMAS", diag)
	diag_matches_2 = re.findall(r"XMAS", diag[::-1])
	total_matches += len(diag_matches) + len(diag_matches_2)

print(total_matches)


#part 2

total_matches = 0

for i in range(1, lines.shape[0]-1):
	for j in range(1, lines.shape[1]-1):
		if lines[i, j] == "A":
			block = lines[i-1:i+2, j-1: j+2]
			diag1 = "".join([block[i, i] for i in range(3)])
			diag2 = "".join([block[i, 2-i] for i in range(3)])
			if ("MAS" == diag1 or "MAS" == diag1[::-1]) and ("MAS" == diag2 or "MAS" == diag2[::-1]):
				total_matches+= 1

print(total_matches)
