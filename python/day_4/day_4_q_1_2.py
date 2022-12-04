with open(r'python/day_4/day_4_q_1_2_input.txt', 'r') as file:
    lines = file.read().splitlines()

summa = 0
for line in lines:
    sections = line.split(',')
    section_1 = [int(number) for number in sections[0].split('-')]
    section_2 = [int(number) for number in sections[1].split('-')]

    range_1 = {number for number in range(section_1[0], section_1[1] + 1)}
    range_2 = {number for number in range(section_2[0], section_2[1] + 1)}

    common_areas = set(range_1).intersection(range_2)

    # fully overlap
    # if len(common_areas) == len(range_1) or len(common_areas) == len(range_2):
    #     summa += 1
    #     pass

    # partly overlap
    if common_areas:
        summa += 1
        pass

print(summa)
