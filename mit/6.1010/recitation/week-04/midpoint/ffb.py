"""
Fill in the blanks in the free_food_bonanza function. Note you may wish to
adding additional helper functions.

Test your code by running this file.
"""


"""
Note that using different versions
of find_path may have result in better performance on the test cases --
only uncomment one version at a time though
"""
from .find_path_visited_list import find_path
# this is the last find_path() from the reading
# from .find_path_visited_set import find_path
# from .find_path_visited_dict import find_path
import time

def free_food_bonanza(board):
    """
    Given a starting board, calculate the minimum number of moves required
    for the student to collect all the food on the board.

    Parameters:
        board: a list of lists of strings, where each cell holds one of:
            - 'S' for student (exactly one on the board)
            - 'F' for food (arbitrarily many on the board)
            - 'W' for wall (arbitrarily many on the board, student may
                    not walk through them)
            - ' ' for an empty square
    Returns:
        Number of moves if board is solvable, None otherwise
    """

    def make_state(board):
        pass # some code here returns a new state

    def get_neighbors(state):
        pass # some code here returns a list of states

    def goal_check(state):
        pass # some code here returns True/False
        # depending on whether a state meets the goal conditions

    start = make_state(board)
    path = find_path(get_neighbors, start, goal_check)
    return # your code here


def test_simple():
    board = [["S"]]
    assert free_food_bonanza(board) == 0
    print("simple test works!")

def test_direction():
    board = [[" ", " ", " "],
             [" ", "S", " "],
             [" ", " ", " "]]
    assert free_food_bonanza(board) == 0, "already solved"
    board = [[" ", "F", " "],
             [" ", "S", " "],
             [" ", " ", " "]]
    assert free_food_bonanza(board) == 1, "up"
    board = [[" ", " ", " "],
             [" ", "S", "F"],
             [" ", " ", " "]]
    assert free_food_bonanza(board) == 1, "right"
    board = [[" ", " ", " "],
             ["F", "S", " "],
             [" ", " ", " "]]
    assert free_food_bonanza(board) == 1, "left"
    board = [[" ", " ", " "],
             [" ", "S", " "],
             [" ", "F", " "]]
    assert free_food_bonanza(board) == 1, "down"
    print("test direction works!")

def test_all():
    ## Example boards

    board1 = [["S", " ", " ", " ", "F"]]

    board2 = [
        ["F", " ", " ", " ", " "],
        ["W", "W", "S", "W", "F"],
        [" ", " ", " ", "W", " "],
    ]

    board3 = [
        ["W", " ", " ", "W", "F"],
        ["W", "W", " ", " ", "F"],
        ["W", " ", " ", " ", " "],
        [" ", "S", "F", " ", " "],
        ["F", "F", "F", " ", " "],
    ]

    expected_results = [4, 8, 10]

    for b, r in zip([board1, board2, board3], expected_results):
        assert free_food_bonanza(b) == r


def test_large():
    board_sizes = [10, 20, 40, 80]
    for N in board_sizes:
        board = [[" " for _ in range(N)] for _ in range(N)]
        board[0][0] = "S"
        board[N - 1][N - 1] = "F"
        print(f"Testing Board Size: {N}")
        start = time.time()
        out = free_food_bonanza(board)
        print(f"Run Took: {time.time() - start}")
        assert out == 2 * (N - 1)


if __name__ == "__main__":
    test_simple()
    test_direction()
    test_all()
    test_large()