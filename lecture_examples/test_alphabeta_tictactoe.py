# Cmput 455 sample code
# Test case for solving TicTacToe by naive negamax, alphabeta, 
# and boolean negamax
# Written by Martin Mueller

from typing import Callable
from game import Game
from negamax_naive import negamax
from alphabeta import call_alphabeta
from tic_tac_toe import TicTacToe
import time

MinimaxFunction = Callable[[Game], int]

def timed_search(name: str, search: MinimaxFunction, state: Game) -> None:
    start: float = time.process_time()
    result = search(state)
    time_used: float = time.process_time() - start
    print(f"{name} Result {result} Time used: {time_used:.4f}")

t = TicTacToe()
timed_search("Alphabeta Negamax", call_alphabeta, t)
timed_search("Naive Negamax", negamax, t)
