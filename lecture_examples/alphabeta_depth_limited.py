# Cmput 455 sample code
# Alphabeta algorithm, depth-limited
# Written by Martin Mueller

from typing import Callable
from search_basics import INFINITY
from game import Game

# depth-limited alphabeta
def alphabeta_depth_limited(state: Game, alpha: int, beta: int, depth: int) -> int:
    if state.end_of_game() or depth == 0:
        return state.int_eval() 
    for m in state.legal_moves():
        state.play(m)
        value = -alphabeta_depth_limited(state, -beta, -alpha, depth - 1)
        if value > alpha:
            alpha = value
        state.undo_move()
        if value >= beta: 
            return beta   # or value in failsoft (later)
    return alpha


# Type alias for a depth-limited search function
DepthLimitedSearchFunction = Callable[[Game, int], int]

# initial call with full window
def call_alphabeta_depth_limited(root_state: Game, depth: int) -> int:
    return alphabeta_depth_limited(root_state, -INFINITY, INFINITY, depth)
