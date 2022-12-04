with open(r'python\day_2\day_2_q_1_2_input.txt', 'r') as file:
    lines = file.read().splitlines()

ELF_ROCK = 'A'
ELF_PAPER = 'B'
ELF_SCISSORS = 'C'

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSORS = 'Z'

POINT_ROCK = 1
POINT_PAPER = 2
POINT_SCISSORS = 3

POINT_LOSS = 0
POINT_DRAW = 3
POINT_WIN = 6

FIRST_RULES = {
    ELF_ROCK: {
        MY_ROCK: POINT_ROCK + POINT_DRAW,
        MY_PAPER: POINT_PAPER + POINT_WIN,
        MY_SCISSORS: POINT_SCISSORS + POINT_LOSS
    },
    ELF_PAPER: {
        MY_ROCK: POINT_ROCK + POINT_LOSS,
        MY_PAPER: POINT_PAPER + POINT_DRAW,
        MY_SCISSORS: POINT_SCISSORS + POINT_WIN
    },
    ELF_SCISSORS: {
        MY_ROCK: POINT_ROCK + POINT_WIN,
        MY_PAPER: POINT_PAPER + POINT_LOSS,
        MY_SCISSORS: POINT_SCISSORS + POINT_DRAW
    }
}

summa = 0

# q1
for line in lines:
    elf_choice, my_choice = line.split(' ')
    roud_point = FIRST_RULES.get(elf_choice).get(my_choice)
    # summa += roud_point

CHOOSE_TO_LOSE = 'X'
CHOOSE_TO_DRAW = 'Y'
CHOOSE_TO_WIN = 'Z'
SECOND_RULES = {
    ELF_ROCK: {
        CHOOSE_TO_LOSE: POINT_SCISSORS + POINT_LOSS,
        CHOOSE_TO_DRAW: POINT_ROCK + POINT_DRAW,
        CHOOSE_TO_WIN: POINT_PAPER + POINT_WIN
    },
    ELF_PAPER: {
        CHOOSE_TO_LOSE: POINT_ROCK + POINT_LOSS,
        CHOOSE_TO_DRAW: POINT_PAPER + POINT_DRAW,
        CHOOSE_TO_WIN: POINT_SCISSORS + POINT_WIN
    },
    ELF_SCISSORS: {
        CHOOSE_TO_LOSE: POINT_PAPER + POINT_LOSS,
        CHOOSE_TO_DRAW: POINT_SCISSORS + POINT_DRAW,
        CHOOSE_TO_WIN: POINT_ROCK + POINT_WIN
    }
}

# q2
for line in lines:
    elf_choice, my_choice = line.split(' ')
    roud_point = SECOND_RULES.get(elf_choice).get(my_choice)
    summa += roud_point

print(summa)