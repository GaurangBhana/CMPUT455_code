# Cmput 455 sample code
# Tests alphabeta on sample tree
# Written by Martin Mueller

from negamax_naive import negamax
from alphabeta import call_alphabeta
from sample_tree import SampleTree
from sample_tree_data import node_id

t = SampleTree()

result: int = negamax(t)
print(f"Naive negamax search result = {result}")
assert result == 6

result = call_alphabeta(t)
print(f"alphabeta negamax search result = {result}")
assert result == 6

a_index: int = node_id['a']
t.play(a_index)

result = negamax(t)
print(f"Naive negamax search result from node a = {result}")
assert result == -3

result = call_alphabeta(t)
print(f"alphabeta negamax search result from node a = {result}")
assert result == -3
