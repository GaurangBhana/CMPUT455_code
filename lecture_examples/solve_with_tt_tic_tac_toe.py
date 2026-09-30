# Cmput 455 sample code
# Boolean Negamax for TicTacToe, with transposition table
# Written by Martin Mueller

from game_basics import EMPTY, BLACK, WHITE, WinnerColor, opponent, winner_as_string
from tic_tac_toe import TicTacToe
from transposition_table_simple import TranspositionTable
from negamax_boolean_tt import negamax, TT
import time

def call_search(state: TicTacToe) -> bool:
    tt: TT = TranspositionTable() # use separate table for each color
    return negamax(state, tt)

def solve(state: TicTacToe) -> WinnerColor:
    state.set_draw_winner(opponent(state.to_play))
    win: bool = call_search(state)
    if win:
        return state.to_play
    # loss or draw, do second search to find out
    state.set_draw_winner(state.to_play)
    if call_search(state):
        return EMPTY # draw
    else: # loss
        return opponent(state.to_play)

def test_solve_with_tt() -> None:
    t = TicTacToe()
    start: float = time.process_time()
    result: WinnerColor = solve(t)
    time_used: float = time.process_time() - start
    print(f"Result: {winner_as_string(result)}\n"
          f"Time used: {time_used:.4f}")

test_solve_with_tt()
