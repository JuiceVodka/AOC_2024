import numpy as np
import copy

file = open("d6.txt", "r")
lines = np.array([list(line)[:-1] for line in file.readlines()])

#print(lines)

#part 1

sight_lines_up = []
sight_lines_down = []
sight_lines_left = []
sight_lines_right = []

visited_locations = []

def path_obstructed(guard_pos, heading, lines):
	if heading == "left":
		path = lines[guard_pos[0], :guard_pos[1]][::-1]
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[guard_pos[0], :guard_pos[1]+1] = "X"

			sight_line = (tuple(guard_pos), (guard_pos[0], 0))
			locations_on_path = [((guard_pos[0], column), "left") for column in range(guard_pos[1], 0, -1)]

			visited_locations.extend(locations_on_path)
			sight_lines_left.append(sight_line)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0], guard_pos[1]-first_x:guard_pos[1]+1] = "X"
			new_pos = [guard_pos[0], guard_pos[1]-first_x]
			lines[new_pos[0], new_pos[1]] = "^"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_left.append(sight_line)

			locations_on_path = [((guard_pos[0], column), "left") for column in range(guard_pos[1], new_pos[1], -1)]
			visited_locations.extend(locations_on_path)

	elif heading == "down":
		path = lines[guard_pos[0]+1:, guard_pos[1]]
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[guard_pos[0]:, guard_pos[1]] = "X"

			sight_line = (tuple(guard_pos), (lines.shape[0], guard_pos[1]))
			sight_lines_down.append(sight_line)

			locations_on_path = [((row, guard_pos[1]), "down") for row in range(guard_pos[0], lines.shape[0])]
			visited_locations.extend(locations_on_path)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0]:guard_pos[0]+first_x, guard_pos[1]] = "X"
			new_pos = [guard_pos[0]+first_x, guard_pos[1]]
			lines[new_pos[0], new_pos[1]] = "<"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_down.append(sight_line)

			locations_on_path = [((row, guard_pos[1]), "down") for row in range(guard_pos[0], new_pos[0])]
			visited_locations.extend(locations_on_path)

	elif heading == "right":
		path = lines[guard_pos[0], guard_pos[1]+1:]
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[guard_pos[0], guard_pos[1]:] = "X"

			sight_line = (tuple(guard_pos), (guard_pos[0], lines.shape[1]))
			sight_lines_right.append(sight_line)

			locations_on_path = [((guard_pos[0], column), "right") for column in range(guard_pos[1], lines.shape[1])]
			visited_locations.extend(locations_on_path)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0], guard_pos[1]:guard_pos[1]+first_x] = "X"
			new_pos = [guard_pos[0], guard_pos[1]+first_x]
			lines[new_pos[0], new_pos[1]] = "v"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_right.append(sight_line)

			locations_on_path = [((guard_pos[0], column), "right") for column in range(guard_pos[1], new_pos[1])]
			visited_locations.extend(locations_on_path)

	elif heading == "up":
		path = lines[:guard_pos[0], guard_pos[1]][::-1]
		
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[:guard_pos[0]+1, guard_pos[1]] = "X"

			sight_line = (tuple(guard_pos), (0, guard_pos[1]))
			sight_lines_up.append(sight_line)

			locations_on_path = [((row, guard_pos[1]), "up") for row in range(guard_pos[0], 0, -1)]
			visited_locations.extend(locations_on_path)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0]-first_x:guard_pos[0]+1, guard_pos[1]] = "X"
			new_pos = [guard_pos[0]-first_x, guard_pos[1]]
			lines[new_pos[0], new_pos[1]] = ">"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_up.append(sight_line)

			locations_on_path = [((row, guard_pos[1]), "up") for row in range(guard_pos[0], new_pos[0], -1)]
			visited_locations.extend(locations_on_path)

	return new_pos, heading_dict[lines[new_pos[0], new_pos[1]]]

lines_copy = copy.deepcopy(lines)


guard_pos = [np.argwhere(lines == char) for char in list("><^v") if len(np.argwhere(lines==char))][0][0]

starting_pos = guard_pos.copy()

heading_dict = {
	">": "right",
	"<": "left",
	"^": "up",
	"v": "down"
}

heading = heading_dict[lines[guard_pos[0], guard_pos[1]]]
starting_heading = heading

while guard_pos is not None:
	guard_pos, heading = path_obstructed(guard_pos, heading, lines)


num_visited = len(np.argwhere(lines=="X"))
print(num_visited)

#part 2


visited_locations_iter = visited_locations.copy()
visited_locations.clear()

blockades = 0
blockades_list = []

for i, location in enumerate(visited_locations_iter):
	if i == 0: continue

	lines_with_blockade = copy.deepcopy(lines_copy)
	lines_with_blockade[location[0]] = "#"
	loop_pos = visited_locations_iter[0][0]
	loop_heading = visited_locations_iter[0][1]
	visited_locations = []

	while loop_pos is not None:
		loop_pos, loop_heading = path_obstructed(loop_pos, loop_heading, lines_with_blockade)
		if len(visited_locations) > 1 and visited_locations[-1] in visited_locations[:-1]:
			blockades += 1
			blockades_list.append(location[0])
			break


deduplicated = list(dict.fromkeys(blockades_list))
print(len(deduplicated))
