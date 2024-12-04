file = open("d1.txt", "r")
text = file.read()
file.close()


rows = text.split("\n")

#part 1
column1 = []
column2 = []

for row in rows:
	parts = row.split()
	column1.append(int(parts[0]))
	column2.append(int(parts[1]))

column1.sort()
column2.sort()

diff = 0
for i in range(len(column1)):
	curdif = (column1[i] - column2[i]) * ((1) * (column1[i] > column2[i]) + (-1) * (column1[i] < column2[i])) #replace with abs you dummy
	diff += curdif

print(diff)


#part2

score = 0
for i in range(len(column1)):
	score += column2.count(column1[i]) * column1[i]

print(score)