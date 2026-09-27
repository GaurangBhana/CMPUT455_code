# Cmput 455 sample code
# Written by Martin Mueller
# Refactored with integer node indexing, separate node names dictionary, and type hints.
# Creates the sample tree of 
# https://en.wikipedia.org/wiki/Alpha–beta_pruning 

from typing import Dict, List, Tuple

# Mapping string names to integer IDs starting from 0

node_id: Dict[str, int] = {
    'root': 0,
    'a': 1, 'b': 2, 'c': 3,
    'al': 4, 'ar': 5, 'bl': 6, 'br': 7, 'cl': 8, 'cr': 9,
    'all': 10, 'alr': 11, 'arr': 12, 'bll': 13, 'blr': 14, 'brr': 15, 'cll': 16, 'crl': 17, 'crr': 18,
    'alll': 19, 'allr': 20, 'alrl': 21, 'alrm': 22, 'alrr': 23, 'arrr': 24,
    'blll': 25, 'blrl': 26, 'blrr': 27, 'brrr': 28, 'clll': 29, 'crll': 30, 'crlr': 31, 'crrl': 32
}

def generate_sample_tree() -> Tuple[Dict[int, List[int]], Dict[int, int]]:
    """
    Generates the standard Wikipedia Alpha-Beta pruning sample tree.

    Returns:
        tree: Adjacency list mapping node index (int) -> list of child node indices (List[int]).
        scores: Leaf values mapping node index (int) -> leaf score (int).
    """

    tree: Dict[int, List[int]] = {}

    # Depth 0 (root)
    tree[0] = [1, 2, 3]

    # Depth 1
    tree[1] = [4, 5]      # a -> al, ar
    tree[2] = [6, 7]      # b -> bl, br
    tree[3] = [8, 9]      # c -> cl, cr

    # Depth 2
    tree[4] = [10, 11]    # al -> all, alr
    tree[5] = [12]        # ar -> arr
    tree[6] = [13, 14]    # bl -> bll, blr
    tree[7] = [15]        # br -> brr
    tree[8] = [16]        # cl -> cll
    tree[9] = [17, 18]    # cr -> crl, crr

    # Depth 3
    tree[10] = [19, 20]   # all -> alll, allr
    tree[11] = [21, 22, 23]  # alr -> alrl, alrm, alrr
    tree[12] = [24]       # arr -> arrr
    tree[13] = [25]       # bll -> blll
    tree[14] = [26, 27]   # blr -> blrl, blrr
    tree[15] = [28]       # brr -> brrr
    tree[16] = [29]       # cll -> clll
    tree[17] = [30, 31]   # crl -> crll, crlr
    tree[18] = [32]       # crr -> crrl

    # Depth 4: Leaves
    for id in range(19, 32 + 1): 
        tree[id] = []

    # Leaf Scores indexed by integer node ID
    scores: Dict[int, int] = {
        19: 5,  # alll
        20: 6,  # allr
        21: 7,  # alrl
        22: 4,  # alrm
        23: 5,  # alrr
        24: 3,  # arrr
        25: 6,  # blll
        26: 6,  # blrl
        27: 9,  # blrr
        28: 7,  # brrr
        29: 5,  # clll
        30: 9,  # crll
        31: 8,  # crlr
        32: 6   # crrl
    }

    return tree, scores