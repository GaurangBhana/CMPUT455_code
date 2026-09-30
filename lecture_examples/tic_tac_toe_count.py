# Cmput 455 sample code
# Count number of TicTacToe states in Tree and DAG models
# Written by Martin Mueller

from typing import List, Optional
from game_basics import EMPTY
from tic_tac_toe import TicTacToe
from transposition_table_simple import TranspositionTable

TT = TranspositionTable[int, bool]
CountsAtDepth = List[int]

def count_at_depth(
    state: TicTacToe,
    depth: int,
    counts: CountsAtDepth,
    tt: Optional[TT] = None
) -> None:

    if tt is not None:
        if tt.lookup(state.code()) is not None:
            return
        tt.store(state.code(), True)

    counts[depth] += 1
    if state.end_of_game():
        return

    for i in range(9):
        if state.board[i] == EMPTY:
            state.play(i)
            count_at_depth(state, depth + 1, counts, tt)
            state.undo_move()

def count_positions(dag: bool = False) -> CountsAtDepth:
    model_name = "DAG" if dag else "Tree"
    state = TicTacToe()
    counts: CountsAtDepth = [0] * 10
    tt: Optional[TT] = TranspositionTable() if dag else None

    count_at_depth(state, 0, counts, tt)
    print(f"Tic Tac Toe positions in {model_name} model: {counts}")
    return counts

if __name__ == "__main__":
    count_positions(dag=True)
    count_positions(dag=False)
    
