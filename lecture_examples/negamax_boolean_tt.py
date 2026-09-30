# Cmput 455 sample code
# Boolean Negamax
# Written by Martin Mueller

import time
from typing import List, Tuple, Optional
from game import Game
from transposition_table_simple import TranspositionTable

TT = TranspositionTable[int, bool]

def store_result(tt: TT, state: Game, result: bool) -> bool:
    tt.store(state.code(), result)
    return result

def negamax(state: Game, tt: TT) -> bool:
    result: Optional[bool] = tt.lookup(state.code())
    if result != None:
        return result
    if state.end_of_game():
        result = state.boolean_eval()
        #assert result is not None
        return store_result(tt, state, result)
    for m in state.legal_moves():
        state.play(m)
        success = not negamax(state, tt)
        state.undo_move()
        if success:
            return store_result(tt, state, True)
    return store_result(tt, state, False)

def negamax_timed(game: Game) -> Tuple[bool, float]:
    start: float = time.process_time()
    tt = TT()
    is_win: bool = negamax(game, tt)
    time_used: float = time.process_time() - start
    return is_win, time_used
