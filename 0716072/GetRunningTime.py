from chess_board import *
from SearchingStrategies import *
import time
import sys
# recursive limit
sys.setrecursionlimit(10000)


BOARDSIZE[0] = 100

start = (0, 0)
goal = (BOARDSIZE[0]-1, BOARDSIZE[0]-1)

st = time.time()
myAstar(start, goal)
ed = time.time()

print('In', BOARDSIZE[0], 'x', BOARDSIZE[0], 'board')
print('From', start, 'to', goal)
print('Astar takes', st-ed, 's', 'for searching.')
