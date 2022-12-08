with open('python\day_5\day_5_input.txt', 'r') as file:
    lines = file.read().splitlines()

tree = {}
current_path = []
for line in lines:
    parts = line.split(' ')

    first = parts[0]
    second = parts[1]
    third = parts[2] if len(parts) > 2 else None

    if second == 'cd':
        if third == '..':
            current_path.pop()
        else:
            current_path.append(third)
            tree['/'.join(current_path)] = 0
    elif second == 'ls':
        continue
    else:
        if first == 'dir':
            continue

        for i in range(len(current_path)):
            if i == 0:
                str_path = '/'
            else:
                str_path = '/'.join(current_path[:i + 1])
            tree[str_path] += int(first)

current_size = tree['/']
unused_space = 70000000 - current_size
free_up = 30000000 - unused_space

possible_directories = []
for key, value in tree.items():
    if value > free_up:
        possible_directories.append(value)
print(sorted(possible_directories))