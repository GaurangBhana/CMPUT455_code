# Cmput 455 sample code
# Test cases for solving TicTacToe by a series 
# of depth-limited searches
# Written by Martin Mueller

import time
from alphabeta_depth_limited import call_alphabeta_depth_limited, DepthLimitedSearchFunction
from tic_tac_toe import TicTacToe

MAX_DEPTH_TIC_TAC_TOE: int = 11 # more than deep enough, 9 moves max.

def time_search(
    name: str,
    search: DepthLimitedSearchFunction,
    root: TicTacToe,
    depth: int
) -> None:
    start: float = time.process_time()
    result: int = search(root, depth)
    time_used: float = time.process_time() - start
    print(f"{name} Depth {depth} Result {result} Time used: {time_used: .4f}")

# call depth-limited search for all depths
# Note: this code does not distinguish 
# between a proven draw and "no win found"
# both are evaluated as 0
def iterative_deepening(t: TicTacToe, max_depth: int) -> None:
    print(t)
    for depth in range(max_depth + 1):
        time_search("Depth-limited Alphabeta", 
                    call_alphabeta_depth_limited, t, depth)

t = TicTacToe()
iterative_deepening(t, MAX_DEPTH_TIC_TAC_TOE)

t.play(0)
t.play(3) # Mistake, now X can win
iterative_deepening(t, MAX_DEPTH_TIC_TAC_TOE)
