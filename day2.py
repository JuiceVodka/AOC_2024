file = open("d2.txt", "r")
reports = file.readlines()
file.close()

reports = [report[:-1] if report[-1] == "\n" else report for report in reports]

#part 1
valid_num = 0
for report in reports:
	readings = [int(reading) for reading in report.split()]
	dec = readings[0] > readings[1]
	valid = True
	for i in range(1, len(readings)):
		if dec == True and readings[i] >= readings[i-1]:
			valid = False
			break
		elif dec == False and readings[i] <= readings[i-1]:
			valid = False
			break
		elif abs(readings[i] - readings[i-1]) > 3 or abs(readings[i] - readings[i-1]) < 1:
			valid = False
			break
	#print(valid)
	valid_num += int(valid)

print(valid_num)

#part2

valid_num = 0
for report in reports:
	readings = [int(reading) for reading in report.split()]
	dec = readings[0] > readings[1]
	valid = True
	for i in range(1, len(readings)):
		if dec == True and readings[i] >= readings[i-1]:
			valid = False
			break
		elif dec == False and readings[i] <= readings[i-1]:
			valid = False
			break
		elif abs(readings[i] - readings[i-1]) > 3 or abs(readings[i] - readings[i-1]) < 1:
			valid = False
			break
	#print(valid)
	valid_num += int(valid)
	if not valid:
		for k, to_remove in enumerate(readings):
			readings_fixed = readings.copy()
			del readings_fixed[k]
			dec = readings_fixed[0] > readings_fixed[1]
			valid = True
			for i in range(1, len(readings_fixed)):
				if dec == True and readings_fixed[i] >= readings_fixed[i-1]:
					#print(readings_fixed, "NON MONOTONE")
					valid = False
					break
				elif dec == False and readings_fixed[i] <= readings_fixed[i-1]:
					#print(readings_fixed, "NON MONOTONE")
					valid = False
					break
				elif abs(readings_fixed[i] - readings_fixed[i-1]) > 3 or abs(readings_fixed[i] - readings_fixed[i-1]) < 1:
					#print(readings_fixed, "TOO BIG GAP")
					valid = False
					break
			if valid:
				valid_num += 1
				break
	#print(readings, valid)
	

print(valid_num)