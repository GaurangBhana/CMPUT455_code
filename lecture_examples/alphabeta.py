# Cmput 455 sample code
# Alphabeta algorithm
# Written by Martin Mueller

from search_basics import INFINITY
from game import Game

def alphabeta(state: Game, alpha: int, beta: int) -> int:
    if state.end_of_game():
        return state.int_eval()
    m: int = 0
    for m in state.legal_moves():
        state.play(m)
        value: int = -alphabeta(state, -beta, -alpha)
        if value > alpha:
            alpha = value
        state.undo_move()
        if value >= beta: 
            return beta   # or value in failsoft (later)
    return alpha

# initial call with full window
def call_alphabeta(root_state: Game) -> int:
    return alphabeta(root_state, -INFINITY, INFINITY)
