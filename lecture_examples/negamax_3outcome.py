from game_basics import is_black_white, opponent, Color, WinnerColor
from game_3outcome import Game3Outcome
from negamax_boolean import negamax_timed

def solve_for_color(game: Game3Outcome, color: Color) -> tuple[bool, float]: 
    assert is_black_white(color)
    restore: WinnerColor = game.draw_winner

    # to check if color can win, count all draws as win for opponent
    game.set_draw_winner(opponent(color))
    is_win: bool
    time_used: float
    is_win, time_used = negamax_timed(game)
    
    # flip result if color is not to_play
    if color != game.to_play:
        is_win = not is_win
    game.set_draw_winner(restore)
    return is_win, time_used
