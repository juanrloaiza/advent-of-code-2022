# Day 2 - Advent of Code 2022

OPPONENT = {'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSORS'}

SELF = {'X': 'ROCK', 'Y': 'PAPER', 'Z': 'SCISSORS'}

options = ['ROCK', 'PAPER', 'SCISSORS']


def wins_against(option):
    return options[(options.index(option) + 1) % 3]


def loses_against(option):
    return options[(options.index(option) - 1) % 3]


# Part 1
# -------------


def calculate_score(opponent: str, self: str):

    # Calculate the base score based in what you played.
    score = options.index(self) + 1

    # If you play whatever defeats your opponent, you win.
    if wins_against(opponent) == self:
        return score + 6

    # Otherwise, if you play the same, you draw.
    elif self == opponent:
        return score + 3

    # Finally, your opponent plays whatever wins against you, you lose.
    elif wins_against(self) == opponent:
        return score

    # Any other option fails.
    else:
        raise TypeError("Move must be ROCK, PAPER or SCISSORS")


# Load the input and calculate!
with open('input.txt') as file:
    plays = file.read().split('\n')

scores = [calculate_score(OPPONENT[play[0]], SELF[play[2]]) for play in plays]

print(f"If you followed the guide, you would get {sum(scores)} points.")

# Part 2
# -------------


def calculate_play(opponent: str, result: str):

    # If you need to draw, return whatever the opponent played.
    if result == 'Y':
        return opponent

    # If you need to lose, return whatever loses against the opponent.
    elif result == 'X':
        return loses_against(opponent)

    # If you need to win, return whatever wins against the opponent.
    elif result == 'Z':
        return wins_against(opponent)

    # Any other option fails.
    else:
        raise TypeError("Result must be 'X', 'Y', or 'Z'.")


scores = []
for play in plays:
    opponent = OPPONENT[play[0]]
    self = calculate_play(opponent, play[2])
    scores.append(calculate_score(opponent, self))

print(f"Following new instructions, you would get {sum(scores)} points.")
