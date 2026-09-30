# Cmput 455 sample code
# Estimate number of TicTacToe states in the tree model (not DAG)
# with simple formula which ignores the early wins
# Written by Martin Mueller

def estimate_TTT() -> list[int]:
    nodes: int = 1 # number of nodes at root level
    result: list[int] = [nodes]
    for branching_factor in range(9, 0, -1):
        nodes *= branching_factor # number of nodes at next level
        result.append(nodes)
    return result

print("Estimated Tic Tac Toe positions in the tree model: ", estimate_TTT())
