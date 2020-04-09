from chess_board import *
from SearchingStrategies import *



for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                BFS((a, b), (c, d))
                Astar((a, b), (c, d))
                DFS((a, b), (c, d))
                IDAstar((a, b), (c, d))
                Astar((a, b), (c, d))
                myAstar((a, b), (c, d))
                myIDAstar((a, b), (c, d))
