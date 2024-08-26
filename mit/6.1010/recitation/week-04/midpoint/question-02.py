import time

# Find Path Algorithm
def find_path(neighbors_function: callable, start: set, goal_test: callable) -> list[set]:
    """
    Return the shortest path through a graph from a given starting state to
    Any state that satisfies a given goal condition.

    Parameters:
        * neighbors_function(state) is a function which returns a list of legal
          neighbor states
        * start is the starting state for the search
        * goal_test(state) is a function which returns True if the given state
          is a goal state for the search, and False otherwise.
    
    Returns:
        A shortest path from start to a state satisfying goal_test(state)
        as a tuple of states, or None if no path exists.
        Note the state representation must be hashable.
    """
    if goal_test(start):
        return (start,)
    
    agenda = [(start,)]
    visited = [start] #> using a list, rather than a set
    
    while agenda:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]

        for neighbor in neighbors_function(terminal_state):
            if neighbor not in visited:
                new_path = this_path + (neighbor,)
                
                if goal_test(neighbor):
                    return new_path

                agenda.append(new_path)
                visited.append(neighbor)
    
    return None


# General Free Food Bonanza Program
def free_food_bonanza(board: list[list]) -> int:
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

    def make_state(board: list[list]) -> set:
        """Creates an individual state representation of a board

        Args:
            board (list[list]): what the board looks like in the current state

        Returns:
            set: a snapshot of the state of the board, including the location  of 
                 the student, location of wall(s) and pizza(s), and board dimensions
        """
        nrow = len(board)
        ncol = len(board[0])

        walls = []
        pizza = []

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'S':
                    position = (i, j)
                if board[i][j] == 'W':
                    walls.append((i, j))
                if board[i][j] == 'F':
                    pizza.append((i, j))
        
        return (position, walls, pizza, (nrow, ncol))
    
    def create_new_state(position: set, walls: list[set], pizza: list[set], nrow: int, ncol: int) -> set:
        """Create a new state representation

        Args:
            position (set): The x,y coordinates of the student
            walls (list[set]): A list of coordinates where walls are located
            pizza (list[set]): A list of coordinates where pizza is located
            nrow (int): The number of rows of the board
            ncol (int): The number of columns of the board

        Returns:
            set: A set representing the state of the board
        """
        return (position, walls, pizza, (nrow, ncol))

    def get_position(state: set) -> set:
        """Get the position of the student of the state of the board

        Args:
            state (set): The state representation of the board

        Returns:
            set: The x,y coordinates of the student
        """
        return state[0]

    def get_walls(state: set) -> list[set]:
        """Get the position of the wall(s) of the state of the board

        Args:
            state (set): The state representation of the board

        Returns:
            list[set]: A list of the x,y coordinates of any walls on the board
        """
        return state[1]

    def get_pizza(state: set) -> list[set]:
        """Get the position of the pizza(s) of the state of the board

        Args:
            state (set): The state representation of the board

        Returns:
            list[set]: A list of the x,y coordinates of any pizzas on the board
        """
        return state[2]

    def get_dimensions(state: set) -> set:
        """Get the dimensions (number of rows and columns) of the state of the board

        Args:
            state (set): The state representation of the board

        Returns:
            set: A set of the number of rows and number of columns of the board
        """
        return state[3]

    def get_neighbors(state: set) -> list[set]:
        """Get all possible neighboring states of a current position on the state of a board

        Args:
            state (set): The state representation of the board

        Returns:
            list[set]: A list of all possible neighbors (up, down, left, right) states of the current state
        """
        position = get_position(state)
        dimensions = get_dimensions(state)
        walls = get_walls(state)
        pizza = get_pizza(state)


        i, j = position
        nrows, ncols = dimensions

        neighbors = []
        for row, col in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            collected = []

            #> cannot land on a wall
            if (row, col) in walls:
                continue

            #> cannot go out of bounds
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                continue

            #> mark if pizza is collected
            if (row, col) in pizza:
                collected.append((row, col))
            
            neighbors.append(
                create_new_state((row, col), walls, [coord for coord in pizza if coord not in collected], nrows, ncols)
            )
        
        return neighbors

    def goal_check(state: set) -> bool:
        """Check if the state of a board meets a goal condition

        Args:
            state (set): The state representation of the board

        Returns:
            bool: True, if all pizza has been collected in the state, False otherwise
        """
        return get_pizza(state) == []
    
    start = make_state(board)
    path = find_path(get_neighbors, start, goal_check)

    return len(path) - 1


# Tests
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


# Main
if __name__ == "__main__":
    test_simple()
    test_direction()
    test_all()
    test_large()