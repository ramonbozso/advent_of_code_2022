import pprint

with open('python\day_9\day_9_input.txt', 'r') as file:
    lines = file.read().splitlines()

size = 30
starting_grid = [['.'] * size for _ in range(size)]
head_how_far_from_start = [0, 0]  # up, right
tail_how_far_from_start = [0, 0]  # up, right


def jump_sideways():
    vertical_diff = abs(head_how_far_from_start[0] -
                        tail_how_far_from_start[0])
    horizontal_diff = abs(head_how_far_from_start[1] -
                          tail_how_far_from_start[1])

    if vertical_diff > 1:
        if horizontal_diff == 1:
            return 'jump'
        return 'move'
    if horizontal_diff > 1:
        if vertical_diff == 1:
            return 'jump'
        return 'move'


# def add_to_grid():
#     row = tail_how_far_from_start[0] + size // 2
#     col = tail_how_far_from_start[1] + size // 2

#     starting_grid[row][col] = True
#     pass

# for line in lines:
#     move, steps = line.split(' ')

#     for step in range(int(steps)):
#         if move == 'R':
#             head_how_far_from_start[1] += 1
#             tail_move = jump_sideways()
#             if tail_move == 'move':
#                 tail_how_far_from_start[1] += 1
#                 add_to_grid()
#             elif tail_move == 'jump':
#                 tail_how_far_from_start[1] += 1
#                 tail_how_far_from_start[0] = head_how_far_from_start[0]
#                 add_to_grid()
#         elif move == 'U':
#             head_how_far_from_start[0] += 1
#             tail_move = jump_sideways()
#             if tail_move == 'move':
#                 tail_how_far_from_start[0] += 1
#                 add_to_grid()
#             elif tail_move == 'jump':
#                 tail_how_far_from_start[0] += 1
#                 tail_how_far_from_start[1] = head_how_far_from_start[1]
#                 add_to_grid()
#         elif move == 'L':
#             head_how_far_from_start[1] -= 1
#             tail_move = jump_sideways()
#             if tail_move == 'move':
#                 tail_how_far_from_start[1] -= 1
#                 add_to_grid()
#             elif tail_move == 'jump':
#                 tail_how_far_from_start[1] -= 1
#                 tail_how_far_from_start[0] = head_how_far_from_start[0]
#                 add_to_grid()
#         elif move == 'D':
#             head_how_far_from_start[0] -= 1
#             tail_move = jump_sideways()
#             if tail_move == 'move':
#                 tail_how_far_from_start[0] -= 1
#                 add_to_grid()
#             elif tail_move == 'jump':
#                 tail_how_far_from_start[0] -= 1
#                 tail_how_far_from_start[1] = head_how_far_from_start[1]
#                 add_to_grid()
#     pass
head = [0, 0]
rope = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
]


def needs_move(head, tail):
    vertical_diff = abs(head[0] - tail[0])
    horizontal_diff = abs(head[1] - tail[1])

    if vertical_diff > 1:
        if horizontal_diff == 1:
            return 'jump'
        return 'move'
    if horizontal_diff > 1:
        if vertical_diff == 1:
            return 'jump'
        return 'move'


def add_to_grid(knot):
    row = knot[0] + size // 2
    col = knot[1] + size // 2

    starting_grid[row][col] = True
    print('added to grid', row, col)
    pass


for line in lines:
    move, steps = line.split(' ')
    print(rope[-1])
    for step in range(int(steps)):
        if move == 'R':
            head[1] += 1
            current_head = head
            for index, knot in enumerate(rope):
                tail_move = needs_move(current_head, knot)
                if tail_move == 'move':
                    rope[index][1] += 1
                elif tail_move == 'jump':
                    rope[index][1] += 1
                    rope[index][0] = current_head[0]
                current_head = knot
                if index == 8:
                    add_to_grid(knot)
        elif move == 'U':
            head[0] += 1
            current_head = head
            for index, knot in enumerate(rope):
                tail_move = needs_move(current_head, knot)
                if tail_move == 'move':
                    rope[index][0] += 1
                elif tail_move == 'jump':
                    rope[index][0] += 1
                    rope[index][1] = current_head[1]
                current_head = knot
                if index == 8:
                    add_to_grid(knot)
        elif move == 'L':
            head[1] -= 1
            current_head = head
            for index, knot in enumerate(rope):
                tail_move = needs_move(current_head, knot)
                if tail_move == 'move':
                    rope[index][1] -= 1
                elif tail_move == 'jump':
                    rope[index][1] -= 1
                    rope[index][0] = current_head[0]
                current_head = knot
                if index == 8:
                    add_to_grid(knot)
        elif move == 'D':
            head[0] -= 1
            current_head = head
            for index, knot in enumerate(rope):
                tail_move = needs_move(current_head, knot)
                if tail_move == 'move':
                    rope[index][0] -= 1
                elif tail_move == 'jump':
                    rope[index][0] -= 1
                    rope[index][1] = current_head[1]
                current_head = knot
                if index == 8:
                    add_to_grid(knot)
    debug_grid = list(list(row) for row in starting_grid)
    debug_grid.reverse()
    for index, row in enumerate(debug_grid):
        print(index + 1, row)
    pass
print(head)
print(rope)
# pprint.pprint(starting_grid)

summ = 0
for row in starting_grid:
    for col in row:
        if col == True:
            summ += 1
print(summ)
import json
with open('file.json', 'w') as file:
    json.dump(starting_grid, file)
