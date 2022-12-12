import networkx as nx
with open('python\day_12\d12_input.txt', 'r') as file:
    lines = file.read().splitlines()

height_map = {}
moves = [
    (1, 0),  # up
    (0, 1),  # right
    (-1, 0),  # down
    (0, -1),  # left
]

start = None
end = None
for row_index, line in enumerate(lines):
    for column_index, character in enumerate(line):
        if character == 'S':
            height_map[(row_index, column_index)] = ord('a')
            # start = (row_index, column_index)
        elif character == 'E':
            height_map[(row_index, column_index)] = ord('z')
            end = (row_index, column_index)
        else:
            height_map[(row_index, column_index)] = ord(character)

grid = nx.DiGraph()

for (x, y), c in height_map.items():
    current_pos = (x, y)
    for x_move, y_move in moves:
        next_pos = (x + x_move, y + y_move)
        next_character = height_map.get(next_pos, 123)  # z -> 122
        next_move_value = c + 1
        if next_character <= next_move_value:  # we can only move 1 up or 0 or any number down
            grid.add_edge(current_pos, next_pos)
# print(grid)
# print(len(nx.shortest_path(grid, start, end)) - 1)

# part 2
short_paths = []
for key, value in height_map.items():
    if value == ord('a'):
        start = key
        try:
            quick_path = nx.shortest_path(grid, start, end)
        except Exception:
            continue

        short_paths.append(len(quick_path) - 1)
print(min(short_paths))