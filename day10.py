import numpy as np

file = open("d10.txt", "r")

lines =  np.array([list(map(int, list(line)[:-1])) for line in file.readlines()])


print(lines)

#part 1

visited_peaks = []
visited_coords = []

def walk_the_trail(location, curr_height):
	visited_coords.append(location)
	if curr_height == 9 and location not in visited_peaks:
		visited_peaks.append(location)


	#check 4 directions
	above = (location[0]-1, location[1])
	bellow = (location[0]+1, location[1])
	left = (location[0], location[1]-1)
	right = (location[0], location[1]+1)

	if above[0] >= 0 and lines[above] == curr_height+1 and above not in visited_coords:
		walk_the_trail(above, lines[above])

	if bellow[0] < lines.shape[0] and lines[bellow] == curr_height +1 and bellow not in visited_coords:
		walk_the_trail(bellow, lines[bellow])

	if left[1] >= 0 and lines[left] == curr_height +1 and left not in visited_coords:
		walk_the_trail(left, lines[left])

	if right[1] < lines.shape[1] and lines[right] == curr_height +1 and right not in visited_coords:
		walk_the_trail(right, lines[right])

#use some memoization, for each cell on the map you can save how many peaks are reachable from it -> if this is too slow
#not even needed

trailheads = np.argwhere(lines == 0)


score = 0
for trailhead in trailheads:
	walk_the_trail(tuple(trailhead), 0)
	score += len(visited_peaks)
	visited_peaks = []
	visited_coords = []

print(score)

#part 2
peaks = []

def walk_the_trail2(location, curr_height):
	if curr_height == 9:
		peaks.append(location)


	#check 4 directions
	above = (location[0]-1, location[1])
	bellow = (location[0]+1, location[1])
	left = (location[0], location[1]-1)
	right = (location[0], location[1]+1)

	if above[0] >= 0 and lines[above] == curr_height+1:
		walk_the_trail2(above, lines[above])

	if bellow[0] < lines.shape[0] and lines[bellow] == curr_height +1:
		walk_the_trail2(bellow, lines[bellow])

	if left[1] >= 0 and lines[left] == curr_height +1:
		walk_the_trail2(left, lines[left])

	if right[1] < lines.shape[1] and lines[right] == curr_height +1:
		walk_the_trail2(right, lines[right])


trailheads = np.argwhere(lines == 0)

score = 0
for trailhead in trailheads:
	walk_the_trail2(tuple(trailhead), 0)
	score += len(peaks)
	peaks = []

print(score)
