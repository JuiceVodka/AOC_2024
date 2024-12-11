file = open("d11.txt", "r")
arrangement = [(stone) for stone in list(map(int, file.readline().split()))]
print(arrangement)

def blink(arrangement):
	for i, group in enumerate(arrangement):
		if type(group) == type(tuple()):
			newgroup = []
			for j, substone in enumerate(group):
				if substone == 0:
					newgroup.append(1)
				elif len(str(substone)) % 2 == 0:
					subgroup1 = int(str(substone)[:len(str(substone))//2])
					subgroup2 = int(str(substone)[len(str(substone))//2:])
					newgroup.append(subgroup1)
					newgroup.append(subgroup2)
				else:
					newgroup.append(substone*2024)
			newgroup = tuple(newgroup)
			arrangement[i] = newgroup
		else:
			if group == 0:
				arrangement[i] = 1
			elif len(str(group)) % 2 == 0:
				subgroup1 = int(str(group)[:len(str(group))//2])
				subgroup2 = int(str(group)[len(str(group))//2:])
				arrangement[i] = (subgroup1, subgroup2)
			else:
				arrangement[i] *= 2024

arr_copy = arrangement.copy()
prev_len = 0
for i in range(25):
	blink(arrangement)


num_stones = 0

for subgroup in arrangement:
	num_stones += len(subgroup)
print(num_stones)


#part 2

memo_dict = {}

def blink_rec(stone):
	if stone == 0:
		return 1
	elif len(str(stone)) % 2 == 0:
		return (int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:]))
	return stone * 2024

def split_count(stone, blinks):
	if blinks == 0:
		memo_dict[(stone, blinks)] = 1
		return 1
	if memo_dict.get((stone, blinks)) is not None:
		return memo_dict[(stone, blinks)]

	blink_rez = blink_rec(stone)
	splits = 0
	if type(blink_rez) == type(tuple()):
		result = 0
		for substone in blink_rez:
			subresult = split_count(substone, blinks-1)
			result += subresult
		memo_dict[(stone, blinks)] = result
		return result

	else:
		result = split_count(blink_rez, blinks-1)
		memo_dict[(stone, blinks)] = result
		return result


print(arr_copy)

total_stones = 0
for i, stone in enumerate(arr_copy):
	rez = split_count(stone, 75)
	total_stones += rez
print(total_stones)

