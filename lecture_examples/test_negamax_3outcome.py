from game_basics import BLACK, WHITE, DRAW, WinnerColor, color_as_string, winner_as_string
from game_3outcome import Game3Outcome
from negamax_3outcome import solve_for_color

PlayerTimes = tuple[float, float]

def solve_for_win_loss_draw(game: Game3Outcome) -> tuple[WinnerColor, PlayerTimes]:
    win_black, time_black = solve_for_color(game, BLACK)
    if win_black:
        return BLACK, (time_black, -1)
    else:
        winner: WinnerColor = DRAW
        win_white, time_white = solve_for_color(game, WHITE)
        if win_white:
            winner = WHITE
        return winner, (time_black, time_white)

def solve_and_print(game: Game3Outcome, correct_result: WinnerColor) -> None: 
    print(f"Board, {color_as_string(game.to_play)} to play:\n{game}")
    #game.print()
    winner: WinnerColor
    time_used: tuple[float, float]
    winner, time_used = solve_for_win_loss_draw(game)
    win_str: str = winner_as_string(winner)
    print(f"Result: {win_str}\n"
          f"Times used (-1 = not searched): "
          f"Black {time_used[0]:.4f}, White {time_used[1]:.4f}\n")
    assert winner == correct_result
