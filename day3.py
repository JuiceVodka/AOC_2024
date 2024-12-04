file = open("d3.txt", "r")
lines = file.read()
file.close()

import re

#part 1
matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', lines)


mul_sum = 0
for match in matches:
	numbers_to_mul = match.split("(")[1].replace(")", "").split(",")
	rez = int(numbers_to_mul[0]) * int(numbers_to_mul[1])
	mul_sum += rez
print(mul_sum)


#part 2
matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', lines)

enabled = True
mul_sum = 0
for match in matches:
	if match == "do()":
		enabled = True
	elif match == "don't()":
		enabled = False
	elif enabled == True:	
		numbers_to_mul = match.split("(")[1].replace(")", "").split(",")
		rez = int(numbers_to_mul[0]) * int(numbers_to_mul[1])
		mul_sum += rez

print(mul_sum)
