import numpy as np

file = open("d12.txt", "r")

lines = np.array([list(line[:-1]) for line in file.readlines()])

covered = np.zeros(lines.shape)
lines = np.pad(lines, 1)
covered = np.pad(covered, 1)


area_circumference_list = []

def plot_group(coords, group_id):
	if lines[coords] != group_id or covered[coords] == 1:
		return 0, 0

	covered[coords] = 1

	top_neighbor = lines[coords[0]-1, coords[1]]
	bot_neighbor = lines[coords[0]+1, coords[1]]
	left_neighbor = lines[coords[0], coords[1]-1]
	right_neighbor = lines[coords[0], coords[1]+1]
	neighbors = [top_neighbor, bot_neighbor, left_neighbor, right_neighbor]
	circumference = sum([0 if neighbor == group_id else 1 for neighbor in neighbors])

	a1, c1 = plot_group((coords[0]-1, coords[1]), group_id)
	a2, c2 = plot_group((coords[0]+1, coords[1]), group_id)
	a3, c3 = plot_group((coords[0], coords[1]-1), group_id)
	a4, c4 = plot_group((coords[0], coords[1]+1), group_id)

	total_area = a1 + a2 + a3 + a4 + 1
	total_circumference = c1 + c2 + c3 + c4 + circumference

	return total_area, total_circumference


for i in range(1, lines.shape[0]-1):
	for j in range(1, lines.shape[1]-1):
		if covered[i, j] == 0:
			area, circumference = plot_group((i, j), lines[i, j])
			area_circumference_list.append((area, circumference))
		else:
			continue

price = 0
for pair in area_circumference_list:
	price += pair[0] * pair[1]

print(price)

#part 2
covered = np.zeros(lines.shape)


edge_vectors = []
area_circumference_list = []

def plot_group2(coords, group_id):
	if lines[coords] != group_id or covered[coords] == 1:
		return 0, 0

	covered[coords] = 1
	

	top_neighbor = lines[coords[0]-1, coords[1]]
	bot_neighbor = lines[coords[0]+1, coords[1]]
	left_neighbor = lines[coords[0], coords[1]-1]
	right_neighbor = lines[coords[0], coords[1]+1]
	neighbors = [top_neighbor, bot_neighbor, left_neighbor, right_neighbor]
	circumference = sum([0 if neighbor == group_id else 1 for neighbor in neighbors])

	if top_neighbor != group_id:
		edge_vector = ((coords[0], coords[1]), (coords[0], coords[1]+1))
		edge_vectors.append(edge_vector)
	if bot_neighbor != group_id:
		edge_vector = ((coords[0]+1, coords[1]+1), (coords[0]+1, coords[1]))
		edge_vectors.append(edge_vector)
	if left_neighbor != group_id:
		edge_vector = ((coords[0]+1, coords[1]), (coords[0], coords[1]))
		edge_vectors.append(edge_vector)
	if right_neighbor != group_id:
		edge_vector = ((coords[0], coords[1]+1), (coords[0]+1, coords[1]+1))
		edge_vectors.append(edge_vector)


	a1, c1 = plot_group2((coords[0]-1, coords[1]), group_id)
	a2, c2 = plot_group2((coords[0]+1, coords[1]), group_id)
	a3, c3 = plot_group2((coords[0], coords[1]-1), group_id)
	a4, c4 = plot_group2((coords[0], coords[1]+1), group_id)

	total_area = a1 + a2 + a3 + a4 + 1
	total_circumference = c1 + c2 + c3 + c4 + circumference

	return total_area, total_circumference


def count_sides(vectors, group):
	starting_vector = vectors[0]
	vectors2 = vectors.copy()
	visited_vectors = [vectors[0]]
	total_sides = 1
	current_vector = vectors[0]
	vectors2.remove(current_vector)

	while len(vectors2) != 0:
		found_next = False
		for vector in vectors2:
			if vector[0] == current_vector[1]:
				y_diff_prev = current_vector[0][0] - current_vector[1][0]
				x_diff_prev = current_vector[0][1] - current_vector[1][1]

				y_diff_curr = vector[0][0] - vector[1][0]
				x_diff_curr = vector[0][1] - vector[1][1]

				if x_diff_prev != x_diff_curr and y_diff_prev != y_diff_curr:
					total_sides += 1

					y_dif_start = starting_vector[0][0] - starting_vector[1][0]
					x_diff_start = starting_vector[0][1] - starting_vector[1][1]
					if x_diff_curr == x_diff_start and y_diff_curr == y_dif_start and (starting_vector[1][0] == vector[1][0] or starting_vector[1][1] == vector[1][1]):
						if (y_diff_curr != 0 and (starting_vector[0][1] == vector[1][1])) or (x_diff_curr != 0 and (starting_vector[0][0] == vector[1][0])) and len(vectors2) == 1:
							total_sides -= 1
				current_vector = vector
				vectors2.remove(current_vector)
				found_next = True
				break

		if not found_next:
			total_sides += 1
			starting_vector = vectors2[0]
			current_vector = vectors2[0]
			vectors2.remove(current_vector)

	return total_sides


for i in range(1, lines.shape[0]-1):
	for j in range(1, lines.shape[1]-1):
		if covered[i, j] == 0:
			edge_vectors = []
			area, circumference = plot_group2((i, j), lines[i, j])
			acutual_circum = count_sides(edge_vectors, lines[i, j])
			area_circumference_list.append((area, acutual_circum))

		else:
			continue


price = 0
for pair in area_circumference_list:
	price += pair[0] * pair[1]

print(price)