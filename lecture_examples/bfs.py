# Cmput 455 sample code
# Breadth-first search on a tree
# This will NOT work on general graphs
# Written by Martin Mueller

from collections import deque
from typing import Dict, List, Optional, Tuple, Deque

Tree = Dict[int, List[int]]

# breadth-first search on tree
# returns (found, num_nodes)
def bfs(tree: Tree, start: int, treasure: int) -> Tuple[bool, int]:
    num_nodes: int = 0
    queue: Deque[int] = deque()
    queue.append(start)
    while len(queue) > 0:
        node = queue.popleft()
        num_nodes += 1
        if node == treasure:
            return True, num_nodes
        for child in tree[node]:
            queue.append(child)
    return False, num_nodes
