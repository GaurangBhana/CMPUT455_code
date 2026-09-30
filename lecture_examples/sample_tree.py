# Cmput 455 sample code
# Written by Martin Mueller
# Refactored to work with integer-indexed sample tree data.

from typing import Dict, List, Union
from sample_tree_data import generate_sample_tree, node_id
from game import Game
from game_basics import COLOR_STR, BLACK, WHITE, WinnerColor


class SampleTree(Game):

    def __init__(self) -> None:
        self._tree: Dict[int, List[int]]
        self._score: Dict[int, int]
        self._tree, self._score = generate_sample_tree()
        super().__init__()

    def reset_game(self) -> None:
        super().reset_game()
        self.current: int = 0  # Root node ID
        super().play(0) # needed for undo to find root state
        self.to_play = BLACK

    def play(self, location: int) -> bool:
        assert not self.end_of_game()
        assert location in self._tree[self.current]
        self.current = location
        return super().play(location)

    def undo_move(self) -> None:
        old = self.current
        super().undo_move()
        self.current = self.last_move()

    def static_eval(self) -> int:
        assert self.end_of_game()
        return self._score[self.current]

    def int_eval(self) -> int:
        score: int = self.static_eval()
        if self.to_play == WHITE:
            return -score
        return score

    def winner(self) -> WinnerColor:
        assert False

    def boolean_eval(self) -> bool:
        assert False

    def end_of_game(self) -> bool:
        return self._tree[self.current] == []

    def legal_moves(self) -> List[int]:
        return self._tree[self.current]

    def __str__(self) -> str:
        return f"{self.current}"
    
    def code(self) -> int:
        raise NotImplementedError
