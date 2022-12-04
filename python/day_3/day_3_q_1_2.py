with open(r'python/day_3/day_3_q_1_2_input.txt', 'r') as file:
    lines = file.read().splitlines()

# lowecase letters: a-z 1-26, ASCII a-z 97-122, diff -> 96
# uppercase letters: A-Z 27-52, ASCII A-Z 65-90, diff -> 38
diff_for_lower = 96
diff_for_upper = 38

summa = 0

# look for common item
# for line in lines:
#     first_half = line[:len(line) // 2]
#     second_half = line[len(line) // 2:]

#     common_item = list(set(first_half).intersection(set(second_half)))[0]

#     if common_item.islower():
#         prio = ord(common_item) - diff_for_lower
#     else:
#         prio = ord(common_item) - diff_for_upper

#     summa += prio

# common item in bags gropup by 3
for every_third_index in range(0, len(lines), 3):
    first_line = lines[every_third_index - 3]
    second_line = lines[every_third_index - 2]
    third_line = lines[every_third_index - 1]

    common_item = list(
        set(first_line).intersection(set(second_line)).intersection(
            set(third_line)))[0]

    if common_item.islower():
        prio = ord(common_item) - diff_for_lower
    else:
        prio = ord(common_item) - diff_for_upper

    summa += prio

print(summa)
