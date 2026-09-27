# Cmput 455 sample code
# Written by Martin Mueller
# Basic constants used by different minimax search programs

# Represent infinity by a value that is
# larger than all game values that we use,
# but small enough to be treated as a Python 3 int
INFINITY = 1000000

# Encoding of game results
# Idea: make win value larger than heuristic scores but smaller than INFINITY
PROVEN_WIN = 10000 
PROVEN_LOSS = -PROVEN_WIN
# heuristic score, can set to 1 to diffentiate from draw
UNKNOWN = 0 
DRAW = 0

