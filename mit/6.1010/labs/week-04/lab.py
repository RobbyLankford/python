"""
6.1010 Lab:
Snekoban Game
"""

import json
import typing

# NO ADDITIONAL IMPORTS!

direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}


# GETTERS
def get_position(game: dict) -> set:
   return game["position"]

def get_walls(game: dict) -> list[set]:
    return game["walls"]

def get_targets(game: dict) -> list[set]:
   return game["targets"]

def get_computers(game: dict) -> list[set]:
   return game["computers"]

def get_dimensions(game: dict) -> set:
   return game["dim"]


# HELPERS
def make_representation(pos: set, walls: list[set], targets: list[set], computers: list[set], dimension: set) -> dict:
    """Make an internal representation of a game board state

    Args:
        pos (set): The player's current position in (row, col) format
        walls (list[set]): A list of positions in (row, col) format where walls are located
        targets (list[set]): A list of positions in (row, col) format where targets are located
        computers (list[set]): A list of positions in (row, col) format where computers are located
        dimension (set): The dimensions of the game board in (nrow, ncol) format

    Returns:
        dict: A dictionary representation of the game board state
    """
    return {'position': pos, 'walls': walls, 'targets': targets, 'computers': computers, 'dim': dimension}


def update_position(position: set, direction: str) -> set:
    """Update the position of a player (or computer)

    Args:
        position (set): The current position in (row, col) format
        direction (str): One of "up", "down", "left", "right", the direction to be moved

    Returns:
        set: A new position after applying the directional movement
    """
    i, j = direction_vector[direction]
    row, col = position

    return (row + i, col + j)


def check_out_of_bounds(position: set, dimensions: set) -> bool:
    """Check if a position would go out of bounds

    Args:
        position (set): The position in (row, col) format
        dimensions (set): The dimensions of the game board in (nrow, ncol) format

    Returns:
        bool: True, if the position is out of bounds, False otherwise
    """
    row, col = position
    nrow, ncol = dimensions

    if (row < 0 or row >= nrow) or (col < 0 or col >= ncol):
        return True
    
    return False


def check_hit_wall(position: set, walls: list[set]) -> bool:
    """Check if a position would run into a wall

    Args:
        position (set): The position in (row, col) format
        walls (list[set]): A list of wall positions in (row, col) format

    Returns:
        bool: True, if the position is included in the list of wall positions, False otherwise
    """
    return position in walls


def check_hit_computer(position: set, computers: list[set], remove: set = None) -> bool:
    """Check if moving a computer would hit another computer

    Args:
        position (set): The position in (row, col) format
        computers (list[set]): A list of computer positions in (row, col) format
        remove (set, optional): If desired, a computer position in (row, col) to remove from the list. Defaults to None.

    Returns:
        bool: True, if moving the computer would hit another computer, False otherwise
    """
    if remove is not None:
        comp_positions = [computer for computer in computers if computer != remove]
    else:
        comp_positions = computers

    return position in comp_positions


def check_can_move_computer(old_position: set, new_position: set, game: dict) -> bool:
    """Check if a computer can be moved from one position to another

    Args:
        old_position (set): The old position of the computer in (row, col) format
        new_position (set): The (potential) new position of the computer in (row, col) format
        game (dict): The dictionary representation of a game board state

    Returns:
        bool: True, if the computer can be moved, False otherwise
    """
    new_comp_oob = check_out_of_bounds(new_position, get_dimensions(game))
    new_comp_hit_wall = check_hit_wall(new_position, get_walls(game))
    new_comp_hit_comp = check_hit_computer(new_position, get_computers(game), old_position)

    if new_comp_hit_wall or new_comp_oob or new_comp_hit_comp:
        return False
    
    return True


def validate_move(position: set, direction: str, game: dict) -> bool:
    """Check if a player's move would be valid if executed

    Args:
        position (set): The old position of the player
        direction (str): The direction, one of "up", "down", "left", "right", that the player would move
        game (dict): The dictionary representation of a game board state

    Returns:
        bool: True, if the move would be a valid move, False otherwise
    """
    outside_dimensions = check_out_of_bounds(position, get_dimensions(game))
    
    hit_wall = check_hit_wall(position, get_walls(game))

    if position in get_computers(game):
        possible_computer_pos = update_position(position, direction)
        can_move_computer = check_can_move_computer(position, possible_computer_pos, game)
    else:
        #> Just set to true because moving a computer is not even a question in this scenario
        can_move_computer = True
    
    if outside_dimensions or hit_wall or not can_move_computer:
        return False
    else:
        return True


def update_game(new_position: set, direction: str, game: dict) -> dict:
    """Update the game board representation after moving the player in a specific direction

    Args:
        new_position (set): The new position in (row, col) format
        direction (str): The direction, one of "up", "down", "left", "right", that was moved by the player
        game (dict): The dictionary representation of a game board state

    Returns:
        dict: The dictionary representation of the updated game board state
    """

    #> Wall Locations
    walls = [wall for wall in get_walls(game)]

    #> Computer Locations
    if new_position in get_computers(game):
        new_comp_pos = update_position(new_position, direction)
        computers = [computer for computer in get_computers(game) if computer != new_position]
        computers.append(new_comp_pos)
    else:
        computers = [computer for computer in get_computers(game)]
    
    #> Target Locations
    targets = [target for target in get_targets(game) if target not in computers]

    #> Dimensions
    dim = game['dim']

    return make_representation(new_position, walls, targets, computers, dim)


# MAIN FUNCTIONS
def make_new_game(level_description: list[list]) -> dict:
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions.
    """
    nrow = len(level_description)
    ncol = len(level_description[0])

    walls = set()
    targets = set()
    computers = set()

    for row in range(nrow):
        for col in range(ncol):
            item = level_description[row][col]

            if item == ["wall"]:
                walls.add((row, col))
            if item == ["target"]:
                targets.add((row, col))
            if item == ["computer"]:
                computers.add((row, col))
            if item == ["player"]:
                position = (row, col)
    
    return make_representation(position, walls, targets, computers, (nrow, ncol))


def victory_check(game: dict) -> bool:
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """
    return len(get_targets(game)) == 0


def step_game(game: dict, direction: str) -> dict:
    """
    Given a game representation (of the form returned from make_new_game),
    return a new game representation (of that same form), representing the
    updated game after running one step of the game.  The user's input is given
    by direction, which is one of the following:
        {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    current_position = get_position(game)
    possible_position = update_position(current_position, direction)

    move_is_valid = validate_move(possible_position, direction, game)

    if move_is_valid:
        return update_game(possible_position, direction, game)
    else:
        return game


def dump_game(game: dict) -> list[list]:
    """
    Given a game representation (of the form returned from make_new_game),
    convert it back into a level description that would be a suitable input to
    make_new_game (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """
    dim = get_dimensions(game)
    nrow = dim[0]
    ncol = dim[1]
    
    game_board = []
    for i in range(nrow):

        row = []
        for j in range(ncol):
            if (i, j) == get_position(game):
                row.append(["player"])
            elif (i, j) in get_walls(game):
                row.append(["wall"])
            elif (i, j) in get_targets(game):
                row.append(["target"])
            elif (i, j) in get_computers(game):
                row.append(["computer"])
            else:
                row.append([])

        game_board.append(row)

    return game_board


# SOLVER FUNCTIONS
def get_neighbors(game: dict) -> list[dict]:
    """Return all valid neighboring game states of a game state

    Args:
        game (dict): The dictionary representation of a game board state

    Returns:
        list[dict]: A list of valid neighboring game states
    """
    position = get_position(game)

    neighbors = []
    for direction in ["up", "down", "left", "right"]:
        possible_move = update_position(position, direction)

        if validate_move(possible_move, direction, game):
            neighbors.append(update_game(possible_move, direction, game))
    
    return neighbors


def get_direction(old_position: set, new_position: set) -> str:
    """Determine the direction moved to get to a new position from an old one

    Args:
        old_position (set): The (row, column) of the old position
        new_position (set): The (row, column) of the new position

    Returns:
        str: The direction traveled ("up", "down", "left", or "right")
    """
    drow = new_position[0] - old_position[0]
    dcol = new_position[1] - old_position[1]

    for direction, movement in direction_vector.items():
        if (drow, dcol) == movement:
            return direction
    
    return None


def get_move_sequence(path: list[dict]) -> list[str]:
    """For a list of game states, get the direction traveled between each state

    Args:
        path (list[dict]): A list of dictionary representations of a game board states

    Returns:
        list[str]: A list of directions moved between states
    """
    positions = [get_position(path) for path in path]

    sequence = []
    for i in range(len(positions) - 1):
        sequence.append(get_direction(positions[i], positions[i+1]))
   
    return sequence


def solve_puzzle(game: dict) -> list[str]:
    """
    Given a game representation (of the form returned from make_new_game), find
    a solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """
    agenda = [[game]]
    visited = [game]

    while agenda:
        current_path = agenda.pop(0)
        terminal_state = current_path[-1]

        for neighbor in get_neighbors(terminal_state):
            if neighbor not in visited:
                new_path = current_path + [neighbor]

                if victory_check(neighbor):
                    return get_move_sequence(new_path)
                
                agenda.append(new_path)
                visited.append(neighbor)
        
    return None


if __name__ == "__main__":
    pass
