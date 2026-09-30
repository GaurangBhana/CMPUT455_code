# Cmput 455 sample code
# Simple transposition table for TicTacToe solver
# This is much slower than an array-based table in C/C++
# which is used in competitive programs
# Written by Martin Mueller

from typing import Dict, Generic, Optional, TypeVar

# Declare generic type variables for Key (code) and Value (score)
K = TypeVar('K')
V = TypeVar('V')


class TranspositionTable(Generic[K, V]):
    # Table is stored in a dictionary, with board code as key, 
    # and minimax score as the value

    # Empty dictionary
    def __init__(self) -> None:
        self.table: Dict[K, V] = {}

    # Used to print the whole table with print(tt)
    def __repr__(self) -> str:
        return self.table.__repr__()
        
    def store(self, code: K, score: V) -> None:
        self.table[code] = score
    
    # Python dictionary returns 'None' if key not found by get()
    def lookup(self, code: K) -> Optional[V]:
        return self.table.get(code)