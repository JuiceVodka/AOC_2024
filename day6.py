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

def path_obstructed(guard_pos, heading):
	if heading == "left":
		path = lines[guard_pos[0], :guard_pos[1]][::-1]
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[guard_pos[0], :guard_pos[1]+1] = "X"

			sight_line = (tuple(guard_pos), (guard_pos[0], 0))
			sight_lines_left.append(sight_line)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0], guard_pos[1]-first_x:guard_pos[1]+1] = "X"
			new_pos = [guard_pos[0], guard_pos[1]-first_x]
			lines[new_pos[0], new_pos[1]] = "^"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_left.append(sight_line)

	elif heading == "down":
		path = lines[guard_pos[0]+1:, guard_pos[1]]
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[guard_pos[0]:, guard_pos[1]] = "X"

			sight_line = (tuple(guard_pos), (lines.shape[0], guard_pos[1]))
			sight_lines_down.append(sight_line)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0]:guard_pos[0]+first_x, guard_pos[1]] = "X"
			new_pos = [guard_pos[0]+first_x, guard_pos[1]]
			lines[new_pos[0], new_pos[1]] = "<"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_down.append(sight_line)

	elif heading == "right":
		path = lines[guard_pos[0], guard_pos[1]+1:]
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[guard_pos[0], guard_pos[1]:] = "X"

			sight_line = (tuple(guard_pos), (guard_pos[0], lines.shape[1]))
			sight_lines_right.append(sight_line)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0], guard_pos[1]:guard_pos[1]+first_x] = "X"
			new_pos = [guard_pos[0], guard_pos[1]+first_x]
			lines[new_pos[0], new_pos[1]] = "v"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_right.append(sight_line)

	elif heading == "up":
		path = lines[:guard_pos[0], guard_pos[1]][::-1]
		
		first_x = np.argwhere(path == "#")
		if len(first_x) == 0:
			lines[:guard_pos[0]+1, guard_pos[1]] = "X"

			sight_line = (tuple(guard_pos), (0, guard_pos[1]))
			sight_lines_up.append(sight_line)
			return None, None
		else:
			first_x = first_x[0][0]
			lines[guard_pos[0]-first_x:guard_pos[0]+1, guard_pos[1]] = "X"
			new_pos = [guard_pos[0]-first_x, guard_pos[1]]
			lines[new_pos[0], new_pos[1]] = ">"

			sight_line = (tuple(guard_pos), tuple(new_pos))
			sight_lines_up.append(sight_line)

	return new_pos, heading_dict[lines[new_pos[0], new_pos[1]]]

lines_copy = copy.deepcopy(lines)

#find the position of the guard
guard_pos = [np.argwhere(lines == char) for char in list("><^v") if len(np.argwhere(lines==char))][0][0]

starting_pos = guard_pos.copy()
#print(guard_pos)

heading_dict = {
	">": "right",
	"<": "left",
	"^": "up",
	"v": "down"
}

heading = heading_dict[lines[guard_pos[0], guard_pos[1]]]
starting_heading = heading
#print(heading)

while guard_pos is not None:
	guard_pos, heading = path_obstructed(guard_pos, heading)


num_visited = len(np.argwhere(lines=="X"))
print(num_visited)

#part 2
#print(lines_copy)
#print(sight_lines_up)
#print(sight_lines_down)
#print(sight_lines_left)
#print(sight_lines_right)

intersections = 0

for i, up in enumerate(sight_lines_up):
	for j, right in enumerate(sight_lines_right):
		#print(up)
		#print(right)
		if right[0][0] < up[0][0] and right[0][0] > up[1][0] and up[0][1] > right[0][1] and up[0][1] < right[1][1]:
			intersections += int(j <= i)
			#print(j <= i)
		elif right[0][0] < up[0][0] and right[0][0] > up[1][0]:
			between_path = lines_copy[right[0][0], up[0][1]:right[0][1]]
			#print("------------ up -> right")
			#print(between_path)
			#print(up, right)
			#print(i, j)
			#print("-------------")
			if "#" not in between_path:
				intersections += int(j <= i)
				#print(j <= i)

for i, right in enumerate(sight_lines_right):
	for j, down in enumerate(sight_lines_down):
		if down[0][1] > right[0][1] and down[0][1] < right[1][1] and right[0][0] > down[0][0] and right[0][0] < down[1][0]:
			intersections += int(j <= i)
			#print(j <= i)
		elif down[0][1] > right[0][1] and down[0][1] < right[1][1]:
			between_path = lines_copy[right[0][0]:down[0][0], down[0][1]]
			#print("----------- right -> down")
			#print(between_path)
			#print(right, down)
			#print(i, j)
			#print("----------")
			if "#" not in between_path:
				intersections += int(j <= i)
				#print(j <= i)

for i, down in enumerate(sight_lines_down):
	for j, left in enumerate(sight_lines_left):
		if left[0][0] > down[0][0] and left[0][0] < down[1][0] and down[0][1] < left[0][1] and down[0][1] > left[1][1]:
			intersections += int(j <= i)
			#print(j <= i)
		elif left[0][0] > down[0][0] and left[0][0] < down[1][0]:
			between_path = lines_copy[left[0][0], left[0][1]:down[0][1]]
			#print("---------- down -> left")
			#print(between_path)
			#print(down, left)
			#print(i, j)
			#print("----------")
			if "#" not in between_path:
				intersections += int(j <= i)
				#print(j <= i)

for i, left in enumerate(sight_lines_left):
	for j, up in enumerate(sight_lines_up):
		if up[0][1] < left[0][1] and up[0][1] > left[1][1] and left[0][0] < up[0][0] and left[0][0] > up[1][0]:
			intersections += int(j <= i)
			#print(j <= i)
		elif up[0][1] < left[0][1] and up[0][1] > left[1][1]:
			between_path = lines_copy[up[0][0]:left[0][0], up[0][1]]
			#print("--------- left -> up")
			#print(between_path)
			#print(left, up)
			#print(i, j)
			#print("----------")
			if "#" not in between_path:
				intersections += int(j <= i)
				#print(j <= i)


print(intersections)

