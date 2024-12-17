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
    print(i)
    total_sum += abs(first_list[i] - second_list[i])

print(total_sum)