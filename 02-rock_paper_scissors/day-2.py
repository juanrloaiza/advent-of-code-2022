OPPONENT = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

SELF = {
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

DEFEATED_BY = {
    'ROCK': 'PAPER',
    'PAPER': 'SCISSORS',
    'SCISSORS': 'ROCK'
}

WINS_AGAINST = {v: k for k, v in DEFEATED_BY.items()}

# Part 1
# -------------


def calculate_score(opponent: str, self: str):

    OWN_SCORE = {
        'ROCK': 1,
        'PAPER': 2,
        'SCISSORS': 3
    }

    # Calculate the base score based in what you played.
    score = OWN_SCORE[self]

    # If you play whatever defeats your opponent, you win.
    if DEFEATED_BY[opponent] == self:
        return score + 6

    # Otherwise, if you play the same, you draw.
    elif self == opponent:
        return score + 3

    # Finally, the remaining alternative is that you lost.
    else:
        return score


# Load the input and calculate!
with open('input.txt') as file:
    plays = file.read().split('\n')

scores = [calculate_score(OPPONENT[play[0]], SELF[play[2]]) for play in plays]

print(f"If you followed the guide, you would get {sum(scores)} points.")

# Part 2
# -------------


def calculate_play(opponent: str, result: str):

    if result == 'Y':
        return opponent
    elif result == 'X':
        return WINS_AGAINST[opponent]
    elif result == 'Z':
        return DEFEATED_BY[opponent]
    else:
        raise TypeError("Result must be 'X', 'Y', or 'Z'.")


scores = []
for play in plays:
    opponent = OPPONENT[play[0]]
    self = calculate_play(opponent, play[2])
    scores.append(calculate_score(opponent, self))

print(f"Following new instructions, you would get {sum(scores)} points.")
