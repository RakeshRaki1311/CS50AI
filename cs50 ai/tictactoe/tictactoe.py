"""
Tic Tac Toe Player
"""

import math

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
    boardcontents = board[0] + board[1] + board[2]
    xcount = boardcontents.count(X)
    ocount = boardcontents.count(O)
    return O if xcount > ocount else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value is None:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    from copy import deepcopy
    newboard = deepcopy(board)
    x, y = action
    if board[x][y] is not None:
        print("Board position not empty!")
        raise ValueError
    else:
        newboard[x][y] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0].count(X) == 3:
        return X
    elif board[0].count(O) == 3:
        return O

    if board[1].count(X) == 3:
        return X
    elif board[1].count(O) == 3:
        return O

    if board[2].count(X) == 3:
        return X
    elif board[2].count(O) == 3:
        return O

    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif  board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O

    if board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif  board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O

    if board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif  board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O

    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O

    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if (winner(board) is not None) or all_filled(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerofthegame = winner(board)
    if winnerofthegame == X:
        return 1
    elif winnerofthegame == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    possible_actions = list(actions(board))
    utilities = []
    for action in possible_actions:
        new_board = result(board, action)
        utilities.append(optimal_utility(new_board))

    current_player = player(board)
    if current_player == X:
        optimal = max(utilities)
    else:
        optimal = min(utilities)

    return possible_actions[utilities.index(optimal)]


def optimal_utility(board):
    """
    Returns the optimal utility for the player whose turn it is to play.
    """
    if terminal(board):
        return utility(board)

    utilities = []
    possible_actions = actions(board)
    for action in possible_actions:
        new_board = result(board, action)
        utilities.append(optimal_utility(new_board))

    next_player = player(board)
    if next_player == X:
        return max(utilities)
    else:
        return min(utilities)

def all_filled(board):
    """
    Returns True if all board is filled, False otherwise.
    """
    for i in range(len(board)):
        if board[i].count(None):
            return False

    return True

def maxvalue(board):
    if terminal(board):
        return utility(board)

    possible_actions = list(actions(board))
    for action in possible_actions:
        v = max(minvalue(result(board,action)))




'''def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];'''
