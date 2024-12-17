import re

file = open("input_day3.txt", 'r')
f = file.read()
file.close()

answer = 0
pattern_mul = re.compile('mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)')
pattern_do = re.compile('do\(\)')
pattern_dont = re.compile('don\'t\(\)')
pattern_condition = re.compile('don\'t\(\)|do\(\)')

last_index = 0
string_last = "do()"
for s in re.finditer(pattern_condition, f):
    sub_string = f[last_index: s.span()[0]]
    last_index = s.span()[1]

    if(re.fullmatch(pattern_do, string_last)):
        valid_list = re.findall('mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', sub_string)
        for txt in valid_list:
            newstr = txt.replace("mul(", "")
            newstr = newstr.replace(")", "")
            numbers = newstr.split(",")
            numbers = splitLine = list(map(int, numbers))
            if (len(numbers) > 2):
                continue
            answer += numbers[0] * numbers[1]
    string_last = s.group()

if(re.fullmatch(pattern_do, string_last)):
    valid_list = re.findall('mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', f[last_index:-1])
    for txt in valid_list:
        newstr = txt.replace("mul(", "")
        newstr = newstr.replace(")", "")
        numbers = newstr.split(",")
        numbers = splitLine = list(map(int, numbers))
        if (len(numbers) > 2):
            continue
        answer += numbers[0] * numbers[1]

print(answer)