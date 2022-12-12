with open('python\day_9\day_9_input.txt', 'r') as file:
    lines = file.read().splitlines()

size = 1000
starting_grid = [['.'] * size for _ in range(size)]

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


def jump_tail(moving_head, moving_tail, move):
    if move == 'R' or move == 'L':
        moving_tail[0] = moving_head[0]
    elif move == 'U' or move == 'D':
        moving_tail[1] = moving_head[1]


def move_part(moving_part, move):
    if move == 'R':
        moving_part[1] += 1
    elif move == 'U':
        moving_part[0] += 1
    elif move == 'L':
        moving_part[1] -= 1
    elif move == 'D':
        moving_part[0] -= 1


def move_tail(moving_head, moving_tail):
    horizontal_diff = moving_head[0] - moving_tail[0]
    vertical_diff = moving_head[1] - moving_tail[1]

    if vertical_diff > 1:
        current_move = 'R'
        if horizontal_diff == 1:
            move_part(moving_tail, current_move)
            jump_tail(moving_head, moving_tail, current_move)
        elif horizontal_diff == -1:
            move_part(moving_tail, current_move)
            jump_tail(moving_head, moving_tail, current_move)
        else:
            move_part(moving_tail, current_move)
    elif vertical_diff < -1:
        if horizontal_diff == 1:
            move_part(moving_tail, 'L')
            jump_tail(moving_head, moving_tail, 'L')
        elif horizontal_diff == -1:
            move_part(moving_tail, 'L')
            jump_tail(moving_head, moving_tail, 'L')
        else:
            move_part(moving_tail, 'L')
    if horizontal_diff > 1:
        if vertical_diff == 1:
            move_part(moving_tail, 'U')
            jump_tail(moving_head, moving_tail, 'U')
        elif vertical_diff == -1:
            move_part(moving_tail, 'U')
            jump_tail(moving_head, moving_tail, 'U')
        else:
            move_part(moving_tail, 'U')
    elif horizontal_diff < -1:
        if vertical_diff == 1:
            move_part(moving_tail, 'D')
            jump_tail(moving_head, moving_tail, 'D')
        elif vertical_diff == -1:
            move_part(moving_tail, 'D')
            jump_tail(moving_head, moving_tail, 'D')
        else:
            move_part(moving_tail, 'D')


def add_to_grid(knot):
    row = knot[0] + size // 2
    col = knot[1] + size // 2

    starting_grid[row][col] = True


for line in lines:
    move, steps = line.split(' ')  # R 5
    for step in range(int(steps)):
        current_head = head
        current_tail = rope[0]
        move_part(current_head, move)
        move_tail(current_head, current_tail)
        # add_to_grid(current_tail)
        for i in range(1, 9):
            current_head = current_tail
            current_tail = rope[i]
            move_tail(current_head, current_tail)

            if i == 8:
                add_to_grid(current_tail)

print(head)
print(rope)

summ = 0
for row in starting_grid:
    for col in row:
        if col == True:
            summ += 1
print(summ)

# starting_grid.reverse()
# for index, row in enumerate(starting_grid):
#     print(index + 1, row)