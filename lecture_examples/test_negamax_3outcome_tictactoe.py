# Cmput 455 sample code
# Solve TicTacToe with Boolean Negamax
# Written by Martin Mueller

from game_basics import DRAW, BLACK
from tic_tac_toe import TicTacToe
from test_negamax_3outcome import solve_and_print

# An example game, with some mistakes by both. 
# Solves game after every move.
def test_solve_game() -> None:
    t = TicTacToe()
    solve_and_print(t, DRAW)
    t.play(0)
    solve_and_print(t, DRAW)
    t.play(3)
    solve_and_print(t, BLACK)
    t.play(1)
    solve_and_print(t, BLACK)
    t.play(4)
    solve_and_print(t, BLACK)
    t.play(5)
    solve_and_print(t, DRAW)
    t.play(2)
    solve_and_print(t, DRAW)
    t.play(6)
    solve_and_print(t, DRAW)
    t.play(7)
    solve_and_print(t, DRAW)
    t.play(8)
    solve_and_print(t, DRAW)

if __name__ == "__main__":
    test_solve_game()

