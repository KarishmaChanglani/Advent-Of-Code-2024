file = open("input_day2.txt", 'r')
f = file.readlines()
file.close()

safe_list_count = 0

unsafe_lists = []

for line in f:
    line = line.strip()
    splitLine = line.split(' ')
    splitLine = list(map(int, splitLine))
    if all(splitLine[i] < splitLine[i + 1] and (splitLine[i+1] - splitLine[i]) <= 3 for i in range(len(splitLine) - 1)):
        safe_list_count += 1
    elif all(splitLine[i] > splitLine[i + 1] and (splitLine[i] - splitLine[i+1]) <= 3 for i in range(len(splitLine) - 1)):
        safe_list_count += 1
    else:
        unsafe_lists.append(splitLine)

print(safe_list_count)
