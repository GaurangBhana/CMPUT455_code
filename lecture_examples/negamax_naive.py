# Cmput 455 sample code
# Naive negamax without any pruning
# Written by Martin Mueller

from game import Game
from search_basics import INFINITY

def negamax(state: Game) -> int:
    if state.end_of_game():
        return state.int_eval()
    best: int = -INFINITY
    for m in state.legal_moves():
        state.play(m)
        value: int = -negamax(state)
        if value > best:
            best = value
        state.undo_move()
    return best
