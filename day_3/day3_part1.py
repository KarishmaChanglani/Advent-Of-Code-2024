import re

file = open("input_day3.txt", 'r')
f = file.read()
file.close()

answer = 0

valid_list = re.findall('mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', f)
for txt in valid_list:
    newstr = txt.replace("mul(", "")
    newstr = newstr.replace(")","")
    numbers = newstr.split(",")
    numbers = list(map(int, numbers))
    if(len(numbers) > 2):
        continue
    answer += numbers[0] * numbers[1]

print(answer)