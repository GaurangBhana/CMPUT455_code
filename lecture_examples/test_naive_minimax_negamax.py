# Cmput 455 sample code
# Tests the naive minimax and negamax codes that don't use any pruning
# Written by Martin Mueller

from sample_tree import SampleTree
from sample_tree_data import node_id
from minimax_naive import minimax_OR, minimax_AND
from negamax_naive import negamax

t = SampleTree()

result: int = minimax_OR(t)
print(f"Minimax search result = {result}")
assert result == 6

result = negamax(t)
print(f"Naive negamax search result = {result}")
assert result == 6

a_index: int = node_id['a']
t.play(a_index)

result = minimax_AND(t)
print(f"Minimax search result from node a = {result}")
assert result == 3

result = negamax(t)
print(f"Naive negamax search result from node a = {result}")
assert result == -3
