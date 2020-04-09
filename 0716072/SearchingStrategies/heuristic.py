from chess_board import *
import math


def heuristic(current, goal):
    '''
    This is the heuristic function for this algorithm
    because knight can at most move |2|+|1| squares, so,
    (dx+dy)/3 must be smaller than the real min of steps
    '''
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    return (dx + dy) // 3


def myheuristic(current, goal):
    '''
    This is a heuristic function which can compute
    the actual number of steps from current to goal
    '''
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    if (dx+dy) % 2 == 0:
        if dx == 1 and dy == 1:
            if ((current[0] == 0 or current[0] == BOARDSIZE[0]-1) and
                    (current[1] == 0 or current[1] == BOARDSIZE[0]-1)):
                return 4
            if ((goal[0] == 0 or goal[0] == BOARDSIZE[0]-1) and
                    (goal[1] == 0 or goal[1] == BOARDSIZE[0]-1)):
                return 4
            else:
                return 2
        elif dx == 2 and dy == 2:
            return 4
        elif dx * 2 < dy:
            return 2 * math.ceil(dy / 4)
        elif dy * 2 < dx:
            return 2 * math.ceil(dx / 4)
        else:
            return 2 * math.ceil((dx + dy) / 6)
    else:
        if (dx + dy) == 1:
            return 3
        elif dx * 2 < dy:
            return 2 * math.ceil((dy-2) / 4) + 1
        elif dy * 2 < dx:
            return 2 * math.ceil((dx-2) / 4) + 1
        else:
            return 2 * math.ceil((dx + dy - 3) / 6) + 1
