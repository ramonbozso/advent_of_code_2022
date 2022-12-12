from tqdm import tqdm
with open('python\day_11\day_11_input.txt', 'r') as file:
    lines = file.read().splitlines()

monkeys = {}
current_monkey = None
rounds = 10000
operands = {'*': lambda x, y: x * y, '+': lambda x, y: x + y}
common_szorzo = 1

for index in range(0, len(lines), 7):
    current_monkey = lines[index][7:8]
    items = lines[index + 1][18:].split(', ')
    operand = lines[index + 2][23:].split(' ')[0]
    value = lines[index + 2][23:].split(' ')[1]
    divisible = lines[index + 3][21:]
    common_szorzo *= int(divisible)
    true_to = lines[index + 4][29:]
    false_to = lines[index + 5][30:]

    monkeys[int(current_monkey)] = {
        'items': items,
        'operand': operand,
        'value': value,
        'divisible': int(divisible),
        'true_to': int(true_to),
        'false_to': int(false_to),
        'counter': 0
    }
print(common_szorzo)
for round_index in tqdm(range(rounds)):
    for key, value in monkeys.items():
        starting_items = len(value['items'])
        for item in value['items']:
            value['counter'] += 1
            if value['value'] == 'old':
                worrie_level = operands[value['operand']](int(item), int(item))
            else:
                worrie_level = operands[value['operand']](int(item),
                                                          int(value['value']))
            calm_worrie_level = worrie_level % common_szorzo
            test = True if calm_worrie_level % value[
                'divisible'] == 0 else False

            if test:
                monkeys[value['true_to']]['items'].append(calm_worrie_level)
            else:
                monkeys[value['false_to']]['items'].append(calm_worrie_level)
        for i in range(starting_items):
            value['items'].pop(0)
for key, value in monkeys.items():
    print(value['counter'])
