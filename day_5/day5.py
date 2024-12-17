def load_rules():
    file = open("input_day5_rules.txt", 'r')
    f = file.readlines()
    file.close()
    rules = []

    for line in f:
        split_line = line.split("|")
        split_line = tuple(map(int, split_line))
        rules.append(split_line)
    return rules


def check_update(update, rules):
    for rule in rules:
        try:
            i, j = update.index(rule[0]), update.index(rule[1])
            if (i > j):
                return False
        except ValueError:
            continue
    return True


def fix(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            i, j = update.index(rule[0]), update.index(rule[1])
            if i > j:
                temp = update[i]
                update[i] = update[j]
                update[j] = temp
    return update


if __name__ == "__main__":
    rules = load_rules()
    file = open("input_day5_updates.txt", 'r')
    f = file.readlines()
    file.close()

    answer = 0
    bad_updates = []

    for line in f:
        update = line.split(",")
        update = list(map(int, update))
        if check_update(update, rules):
            l = len(update)
            answer += update[int(abs(l / 2))]
        else:
            bad_updates.append(update)

    print("First part:" + str(answer))
    answer = 0
    for update in bad_updates:
        new_update = fix(update, rules)
        answer += new_update[int(abs(len(new_update) / 2))]

    print("Second part:" + str(answer))
