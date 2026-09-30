from game21 import Game21
from game_basics import win_str
from negamax_boolean_tt import negamax_timed

def run_solve_game21(max_size: int) -> None:
    for size in range(max_size + 1):
        game = Game21(size)
        is_win: bool
        time_used: float
        is_win, time_used = negamax_timed(game)
        print(f"Game {size} solved as {win_str(is_win)} in {time_used:.2e} seconds")

def test_solve_game21(max_size: int) -> None:
    for size in range(max_size + 1):
        game = Game21(size)
        is_win: bool
        is_win, _ = negamax_timed(game)
        assert is_win == (size % 4 != 0) # losing iff multiple of 4

if __name__ == "__main__":
    run_solve_game21(1000)
    # I tried 10000...
    # ...Game 2971 solved as win in 7.56e-03 seconds
    # RecursionError: maximum recursion depth exceeded
