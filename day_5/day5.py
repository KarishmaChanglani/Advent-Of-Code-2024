import graphlib


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


def is_valid(update_to_check, check_rules):
    for a, b in check_rules:
        if a in update_to_check and b in update_to_check:
            i, j = update_to_check.index(a), update_to_check.index(b)
            if i > j:
                return False
    return True


def sort(bad_update, sorting_rules):
    i = 0
    while i != len(bad_update):
        i = len(bad_update)
        for rule in sorting_rules:
            a, b = rule[0], rule[1]
            # Value check
            if a not in bad_update or b not in bad_update:
                continue
            first_page = bad_update.index(a)
            second_page = bad_update.index(b)
            if first_page > second_page:
                i -= 1
                bad_update.pop(first_page)
                bad_update.insert(second_page, a)

    return bad_update


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
        if is_valid(update, rules):
            answer += update[int(abs(len(update) / 2))]
        else:
            bad_updates.append(update)
    print("First part:" + str(answer))

    answer = 0

    for update in bad_updates:
        new = sort(update, rules)
        if new is not None:
            answer += new[int(abs(len(new) / 2))]

    print("Second part:" + str(answer))
