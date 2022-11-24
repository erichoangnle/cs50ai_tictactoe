"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X and O on board
    count_X = 0
    count_O = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_X += 1
            elif board[i][j] == O:
                count_O += 1

    # X gets the first move
    if count_X == 0 and count_O == 0:
        return X
    # O's move
    elif count_X > count_O:
        return O
    # X's move
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Declare empty set
    actions = set()

    # Check if cells are EMPTY
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                # Add cell to set
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy of original board
    copy_board = copy.deepcopy(board)

    i = action[0]
    j = action[1]

    # Check if action is valid
    if copy_board[i][j] is not None:
        raise ValueError("Not a valid move!")

    # If move is valid
    if player(copy_board) == X:
        copy_board[i][j] = X
    elif player(copy_board) == O:
        copy_board[i][j] = O

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for winner in row
    i = 0
    while i < 3:
        x = 0
        o = 0
        for j in range(3):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
        if x == 3:
            return X
        elif o == 3:
            return O
        x = 0
        o = 0
        i += 1

    # Check for winner in column
    j = 0
    while j < 3:
        x = 0
        o = 0
        for i in range(3):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
        if x == 3:
            return X
        elif o == 3:
            return O
        x = 0
        o = 0
        j += 1

    # Check for winner in diagonal
    if board[0][0] is not None and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[2][2] == X:
            return X
        else:
            return O

    # Check for winner in diagonal
    if board[0][2] is not None and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[2][0] == X:
            return X
        else:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Count empty cell
    empty = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                empty += 1
    
    # Check if game is over
    if empty == 0 or winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Return None if terminal
    if terminal(board):
        return None

    # if not terminal
    else:
        v = []

        # Player X's turn
        if player(board) == X:
            moves = actions(board)

            # Calculate outcomes for possible moves
            for action in moves:
                v.append(min_value(result(board, action)))

            # Print out possible moves and outcomes
            print(moves)
            print(v)

            # Return move with best possible outcome
            for i in range(len(v)):
                if v[i] == max(v):
                    return list(actions(board))[i]
        
        # Player O's turn
        else:
            moves = actions(board)

            # Calculate outcomes for possible moves
            for action in moves:
                v.append(max_value(result(board, action)))

            # Print out possible moves and outcomes
            print(moves)
            print(v)

            # Return move with best possible outcome
            for i in range(len(v)):
                if v[i] == min(v):
                    return list(actions(board))[i]

        return


def max_value(board):
    """
    Calculate the maximum outcome of a moves
    Assuming opponent play optimally
    """
    # Check if game's over
    if terminal(board):
        return utility(board)

    # Calculate outcome of a moves
    else:

        v = -2
        for action in actions(board):
            v = max(v, min_value(result(board, action)))

        # No need to compare if v is already at highest value
        if v == 1:
            return v
        return v


def min_value(board):
    """
    Calculate minimum outcome of a move
    Assuming opponent play optimally
    """
    # Check if game's over
    if terminal(board):
        return utility(board)

    #Calculate outcome of a move
    else:

        v = 2
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        
        # No need to compare if v is already at lowest value
        if v == -1:
            return v

        return v