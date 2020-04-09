from chess_board import *
from SearchingStrategies import *
import tracemalloc
import sys

# recursive limit
sys.setrecursionlimit(10000)


def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)
    total = sum(stat.size for stat in top_stats)
    return (total / 1024)



BOARDSIZE[0] = 100

start = (0, 0)
goal = (BOARDSIZE[0]-1, BOARDSIZE[0]-1)


tracemalloc.start()

myAstar(start, goal)

snapshot = tracemalloc.take_snapshot()
m = display_top(snapshot)
tracemalloc.clear_traces()

print('In', BOARDSIZE[0], 'x', BOARDSIZE[0], 'board')
print('From', start, 'to', goal)
print('Astar used', m, 'KiB when searching.')
