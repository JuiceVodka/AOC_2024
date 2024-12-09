file = open("d9.txt", "r")

line = file.readline()[:-1]

#odd indices are free space sizes, even indices are blocks. their id is thir index / 2

#handle space moving
free_space_ix = 1
free_space_left_on_ix = int(line[free_space_ix])

chunk_to_move = len(line)-1
size_of_chunk_left = int(line[chunk_to_move])

multiplier = int(line[0])

checksum = 0
while free_space_ix < chunk_to_move:
	free_space = free_space_left_on_ix - size_of_chunk_left
	if free_space < 0:
		#increase checksum and multiplier
		multipliers = list(range(multiplier, multiplier+free_space_left_on_ix))
		checksum_to_add = sum([mul * (chunk_to_move//2) for mul in multipliers])
		multiplier += free_space_left_on_ix
		multiplier += int(line[free_space_ix+1])
		checksum += checksum_to_add

		size_of_chunk_left -= free_space_left_on_ix
		#chunk to move stays the same

		free_space_ix += 2
		free_space_left_on_ix = int(line[free_space_ix])

	elif free_space > 0:
		#increase checksum and multiplier
		multipliers = list(range(multiplier, multiplier + size_of_chunk_left))
		checksum_to_add = sum([mul * (chunk_to_move//2) for mul in multipliers])
		multiplier += size_of_chunk_left
		checksum += checksum_to_add

		#stay in the same free space
		free_space_left_on_ix -= size_of_chunk_left

		#move chunk one down
		chunk_to_move -= 2
		size_of_chunk_left = int(line[chunk_to_move])


	else:
		#perfectly aligned
		#increase checksum and mult
		multipliers = list(range(multiplier, multiplier + free_space_left_on_ix))
		checksum_to_add = sum([mul * (chunk_to_move//2) for mul in multipliers])
		multiplier += free_space_left_on_ix
		multiplier += int(line[free_space_ix+1])
		checksum += checksum_to_add

		#move both chunk and free_space
		free_space_ix += 2
		free_space_left_on_ix = int(line[free_space_ix])

		chunk_to_move -= 2
		size_of_chunk_left = int(line[chunk_to_move])

#add the residual checksum
mult = 0
for i in range(0, chunk_to_move+1, 2):
	if i == chunk_to_move:
		mults = range(mult, mult + size_of_chunk_left)
		checksum_to_add = sum([mul * i//2 for mul in mults])
		checksum += checksum_to_add
		
	else:
		mults = range(mult, mult + int(line[i]))
		checksum_to_add = sum([mul * i//2 for mul in mults])
		mult += int(line[i+1]) + int(line[i])
		checksum += checksum_to_add

print(checksum)


#part 2
import numpy as np

span_dict = {}

free_spaces_array = np.array(list(map(int, list(line[1::2]))))

line_array = list(map(int, list(line)))


for file_id in range(len(line)-1, -1, -2):
	cur_file_size = int(line[file_id])

	free_spaces = np.argwhere(free_spaces_array[:file_id//2] >= cur_file_size)

	if free_spaces.shape[0] == 0:
		span_start = sum(line_array[:file_id])
		span_dict[file_id//2] = list(range(span_start, span_start + int(line[file_id])))

	else:
		span_start = sum(line_array[:1+free_spaces[0, 0]*2])
		span_dict[file_id//2] = list(range(span_start, span_start + int(line[file_id])))
		free_spaces_array[free_spaces[0, 0]] -= int(line[file_id])
		line_array[free_spaces[0, 0]*2] += int(line[file_id])
		line_array[free_spaces[0, 0]*2 +1] -= int(line[file_id])

		
		
checksum = 0
for key in span_dict:
	checksum += sum([mult * key for mult in span_dict[key]])

print(checksum)
