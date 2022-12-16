# Import Data
with open("day-02.txt", "r") as file:
    games = [combos for combos in file.read().strip().split("\n")]


# Question 1

## Scoring System
##
## | Shape Selected | Points |   | Outcome | Points |   | Code | Meaning |
## |:--------------:|:------:|   |:-------:|:------:|   |:----:|:-------:|
## |      Rock      |    1   |   |  Lost   |    0   |   | A, X |  Rock   |
## |      Paper     |    2   |   |  Draw   |    3   |   | B, Y |  Paper  |
## |     Scissor    |    3   |   |  Won    |    6   |   | C, Z | Scissor |
##
## All Possible Combinations
## | Left | Right | Outcome |  Points   |
## |:----:|:-----:|:-------:|:---------:|
## |  A   |   X   |   Draw  | 1 + 3 = 4 |
## |  A   |   Y   |   Win   | 2 + 6 = 8 |
## |  A   |   Z   |   Lose  | 3 + 0 = 3 |
## |  B   |   X   |   Lose  | 1 + 0 = 1 |
## |  B   |   Y   |   Draw  | 2 + 3 = 5 |
## |  B   |   Z   |   Win   | 3 + 6 = 9 |
## |  C   |   X   |   Win   | 1 + 6 = 7 |
## |  C   |   Y   |   Lose  | 2 + 0 = 2 |
## |  C   |   Z   |   Draw  | 3 + 3 = 6 |

## Score Outcomes
scores = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

## Calculate Points
points = 0
for game in games:
    points += scores[game]

## Print Answer
print("Answer 1: ", points)


# Question 2

## Scoring System
##
## | Shape Selected    | Points |   | Outcome | Points |   | Code | Meaning |
## |:-----------------:|:------:|   |:-------:|:------:|   |:----:|:-------:|
## |     Rock (A)      |    1   |   |  Lost   |    0   |   |   X  |  Lose   |
## |     Paper (B)     |    2   |   |  Draw   |    3   |   |   Y  |  Draw   |
## |     Scissor (C)   |    3   |   |  Won    |    6   |   |   Z  |  Win    |
##
## All Possible Combinations
## | Left | Right | Outcome |  Points   |
## |:----:|:-----:|:-------:|:---------:|
## |  A   |   C   |  X (L)  | 3 + 0 = 3 |
## |  A   |   A   |  Y (D)  | 1 + 3 = 4 |
## |  A   |   B   |  Z (W)  | 2 + 6 = 8 |
## |  B   |   A   |  X (L)  | 1 + 0 = 1 |
## |  B   |   B   |  Y (D)  | 2 + 3 = 5 |
## |  B   |   C   |  Z (W)  | 3 + 6 = 9 |
## |  C   |   B   |  X (L)  | 2 + 0 = 2 |
## |  C   |   C   |  Y (D)  | 3 + 3 = 6 |
## |  C   |   A   |  Z (W)  | 1 + 6 = 7 |

## Score Outcomes
scores = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

## Calculate Points
points = 0
for game in games:
    points += scores[game]

## Print Answer
print("Answer 2: ", points)