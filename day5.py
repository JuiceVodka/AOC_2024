file = open("d5.txt", "r")

rules = True

ordering = []
sequences = []

line = file.readline()

while line != "":
	if line == "\n":
		rules = False
		line = file.readline()
		continue
	if rules:
		rul = (int(line.split("|")[0]), int(line.split("|")[1]))
		ordering.append(rul)
	else:
		sequences.append(list(map(int, line.split(","))))
	line = file.readline()


#part 1
total = 0
wrong_sequences = []
for sequence in sequences:
	all_good = True
	for rule in ordering:
		first_ix = 0
		second_ix = 0
		if rule[0] in sequence and rule[1] in sequence:
			first_ix = sequence.index(rule[0])
			second_ix = sequence.index(rule[1])
			if first_ix > second_ix:
				all_good = False

	if all_good:
		middle_num = sequence[len(sequence)//2]
		total += middle_num
	else:
		wrong_sequences.append(sequence)
print(total)

#part 2

changes = True
while changes:
	changes = False
	for i, sequence in enumerate(wrong_sequences):
		for rule in ordering:
			first_ix = 0
			second_ix = 0
			if rule[0] in sequence and rule[1] in sequence:
				first_ix = sequence.index(rule[0])
				second_ix = sequence.index(rule[1])
				if first_ix > second_ix:
					wrong_sequences[i][first_ix], wrong_sequences[i][second_ix] = wrong_sequences[i][second_ix], wrong_sequences[i][first_ix]
					changes = True
					sequence = wrong_sequences[i]

total = 0
for sequence in wrong_sequences:
	middle_num = sequence[len(sequence)//2]
	total += middle_num

print(total)

