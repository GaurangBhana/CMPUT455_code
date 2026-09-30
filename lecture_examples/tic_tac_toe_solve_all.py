# Cmput 455 sample code
# Solve all TicTacToe states (Tree and DAG models)
# Written by Martin Mueller

from typing import List, Optional, Set, Tuple
from game_basics import BLACK, WHITE, EMPTY, opponent, Color
from tic_tac_toe import TicTacToe
from negamax_boolean_tt import negamax
from transposition_table_simple import TranspositionTable

ScoreAtDepth = List[int]
ScoreAtAllDepths = List[ScoreAtDepth]
TT = TranspositionTable[int, bool]

def print_to_play_stats(d: int, to_play: int, our_scores: ScoreAtDepth, opp_scores: ScoreAtDepth) -> None:
    b_wins = opp_scores[1]
    w_wins = our_scores[0]
    draws = our_scores[1] - opp_scores[1]
    if to_play == WHITE:
        b_wins, w_wins = w_wins, b_wins
    print(f"Depth {d}: {b_wins} black, {draws} draws, {w_wins} white, "
          f"{sum(our_scores)} total positions")

def print_stats(w_scores: ScoreAtAllDepths, b_scores: ScoreAtAllDepths) -> None:
    to_play = BLACK
    for d in range(10):
        if to_play == BLACK:
            print_to_play_stats(d, to_play, b_scores[d], w_scores[d])
        else:
            print_to_play_stats(d, to_play, w_scores[d], b_scores[d])
        to_play = opponent(to_play)

def solve_at_depth(
    state: TicTacToe,
    depth: int,
    scores: ScoreAtAllDepths,
    tt: TT,
    visited: Optional[Set[int]] = None
) -> None:
    code = state.code()
    if visited is not None:
        if code in visited:
            return
        visited.add(code)

    result: bool = negamax(state, tt)
    scores[depth][int(result)] += 1

    if state.end_of_game():
        return

    for i in range(9):
        if state.board[i] == EMPTY:
            state.play(i)
            solve_at_depth(state, depth + 1, scores, tt, visited)
            state.undo_move()

def solve_ttt_for_color(t: TicTacToe, color: Color, tt: TT, dag: bool = False) -> ScoreAtAllDepths:
    t.set_draw_winner(color)
    scores: ScoreAtAllDepths = [[0] * 2 for _ in range(10)]
    visited: Optional[Set[int]] = set() if dag else None
    solve_at_depth(t, 0, scores, tt, visited)
    return scores

def solve_ttt(use_dag: bool = False) -> None:
    state_space = "DAG" if use_dag else "Tree"
    print(f"Solve all TicTacToe states in {state_space} model black win/draw/white win")
    
    t = TicTacToe()
    ttw: TT = TranspositionTable()
    w_scores = solve_ttt_for_color(t, WHITE, ttw, use_dag)
    
    ttb: TT = TranspositionTable()
    b_scores = solve_ttt_for_color(t, BLACK, ttb, use_dag)
    
    print_stats(w_scores, b_scores)

if __name__ == "__main__":
    solve_ttt(use_dag=True)
    print()
    solve_ttt(use_dag=False)