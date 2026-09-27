# Cmput 455 sample code
# Naive minimax without any pruning
# Written by Martin Mueller

from game_basics import BLACK
from game import Game
from search_basics import INFINITY

def minimax_OR(state: Game) -> int:
    if state.end_of_game():
        return state.int_eval_for_color(BLACK)
    best: int = -INFINITY
    for m in state.legal_moves():
        state.play(m)
        value: int = minimax_AND(state)
        if value > best:
            best = value
        state.undo_move()
    return best

def minimax_AND(state: Game) -> int:
    if state.end_of_game():
        return state.int_eval_for_color(BLACK)
    best: int = INFINITY
    for m in state.legal_moves():
        state.play(m)
        value: int = minimax_OR(state)
        if value < best:
            best = value
        state.undo_move()
    return best
