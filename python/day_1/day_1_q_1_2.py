with open('python/day_1/day_1_q_1_2_input.txt', 'r') as file:
    lines = file.read().splitlines()

previous_max = 0
current_calories = 0
top_three = [0, 0, 0]

for line in lines:
    if line == '':
        if current_calories >= previous_max:
            previous_max = current_calories

        if any(current_calories > elem for elem in top_three):
            top_three = sorted(top_three, reverse=True)
            top_three[2] = current_calories

        current_calories = 0
    else:
        current_calories = current_calories + int(line)

print(previous_max)
print(sum(top_three))