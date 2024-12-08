import numpy as np

file = open("d8.txt", "r")


lines = np.array([list(line)[:-1] for line in file.readlines()])
print(lines)

antenae = {}

for i in range(lines.shape[0]):
	for j in range(lines.shape[1]):
		if lines[i, j] != ".":
			if antenae.get(lines[i, j]) is None:
				antenae[lines[i, j]] = []
			antenae[lines[i, j]].append((i, j))

#part 1
antinodes = []

for key in antenae:
	locations = antenae[key]
	for i, location1 in enumerate(locations):
		for j in range(i):
			location2 = locations[j]
			from_first_to_second = (location2[0]-location1[0], location2[1]-location1[1])
			antinode1 = (location1[0] - from_first_to_second[0], location1[1] - from_first_to_second[1]) #subrtract
			antinode2 = (location2[0] + from_first_to_second[0], location2[1] + from_first_to_second[1]) #add
			if antinode1 not in antinodes and antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < lines.shape[0] and antinode1[1] < lines.shape[1]:
				antinodes.append(antinode1)
			if antinode2 not in antinodes and antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < lines.shape[0] and antinode2[1] < lines.shape[1]:
				antinodes.append(antinode2)

print(len(antinodes))

#part 2

antinodes = []
for key in antenae:
	locations = antenae[key]
	for i, location1 in enumerate(locations):
		for j in range(i):
			location2 = locations[j]
			vec = (location2[0]-location1[0], location2[1]-location1[1])
			for div in range(min(vec), 1, -1):
				if vec[1] % div == 0 and vec[0] % div == 0:
					vec = (vec1[0]//div, vec1[1]//div)

			curr_loc_pos = location1
			curr_loc_neg = location1
			while True:
				pos_inbounds = curr_loc_pos[0] >= 0 and curr_loc_pos[1] >= 0 and curr_loc_pos[0] < lines.shape[0] and curr_loc_pos[1] < lines.shape[1]
				neg_inbounds = curr_loc_neg[0] >= 0 and curr_loc_neg[1] >= 0 and curr_loc_neg[0] < lines.shape[0] and curr_loc_neg[1] < lines.shape[1]

				if curr_loc_pos not in antinodes and pos_inbounds:
					antinodes.append(curr_loc_pos)
				if curr_loc_neg not in antinodes and neg_inbounds:
					antinodes.append(curr_loc_neg)

				if pos_inbounds:
					curr_loc_pos = (curr_loc_pos[0] + vec[0], curr_loc_pos[1] + vec[1])

				if neg_inbounds:
					curr_loc_neg = (curr_loc_neg[0] - vec[0], curr_loc_neg[1] - vec[1])

				if not pos_inbounds and not neg_inbounds:
					break

print(len(antinodes))



