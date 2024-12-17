file = open("input_day1.txt", 'r')
f = file.readlines()
file.close()

first_list = []
second_list = []

for line in f:
    line = line.strip()
    splitLine = line.split('   ')
    first_list.append(splitLine[0])
    second_list.append(splitLine[1])

first_list = list(map(int, first_list))
second_list = list(map(int, second_list))

total_sum = 0

first_list.sort()
second_list.sort()

for i in range(len(first_list)):
    current_count = second_list.count(first_list[i])
    total_sum += first_list[i]*current_count

print(total_sum)