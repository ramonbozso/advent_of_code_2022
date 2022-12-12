with open('python\day_8.py\day_8_input.txt', 'r') as file:
    lines = file.read().splitlines()

grid = []

rows = len(lines)
cols = len(lines[0])

total_number_of_trees = rows * cols
# print(total_number_of_trees)
not_visible = 0
for row_index, line in enumerate(lines):
    row = []
    for col_index, number in enumerate(line):
        row.append(int(number))
    grid.append(row)

# q1
# for row_index, row in enumerate(grid):
#     if row_index == 0 or row_index == 98:
#         continue
#     for col_index, col in enumerate(row):
#         if col_index == 0 or col_index == 98:
#             continue
#         current_tree = grid[row_index][col_index]

#         left_side = grid[row_index][:col_index]
#         if any(current_tree <= tree for tree in left_side):
#             right_side = grid[row_index][col_index + 1:]
#             if any(current_tree <= tree for tree in right_side):
#                 upper_side = [
#                     current_row[col_index] for current_row in grid[:row_index]
#                 ]
#                 if any(current_tree <= tree for tree in upper_side):
#                     down_side = [
#                         current_row[col_index]
#                         for current_row in grid[row_index + 1:]
#                     ]
#                     if any(current_tree <= tree for tree in down_side):
#                         not_visible += 1
current_winner = 0
for row_index, row in enumerate(grid):
    if row_index == 0 or row_index == 98:
        continue
    for col_index, col in enumerate(row):
        if col_index == 0 or col_index == 98:
            continue
        current_tree = grid[row_index][col_index]
        left_side: list = grid[row_index][:col_index]
        left_points = 0
        left_side.reverse()
        for index, tree in enumerate(left_side):
            left_points += 1
            if tree >= current_tree:
                break

        right_side = grid[row_index][col_index + 1:]
        right_points = 0
        for index, tree in enumerate(right_side):
            right_points += 1
            if tree >= current_tree:
                break

        upper_side = [
            current_row[col_index] for current_row in grid[:row_index]
        ]
        upper_side.reverse()
        upper_points = 0
        for index, tree in enumerate(upper_side):
            upper_points += 1
            if tree >= current_tree:
                break

        down_side = [
            current_row[col_index] for current_row in grid[row_index + 1:]
        ]
        down_points = 0
        for index, tree in enumerate(down_side):
            down_points += 1
            if tree >= current_tree:
                break

        current_points = left_points * right_points * upper_points * down_points
        if current_winner < current_points:
            current_winner = current_points

print(current_winner)