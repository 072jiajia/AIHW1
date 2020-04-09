from chess_board import *
from FibonacciHeap import *
from .heuristic import heuristic


def GetRoute(start, goal, TracebackDict):
    '''
    This is a function for getting the route from
    start point to goal point
    ========================================
    for every step we append the point(step)
    to the end of the route, so we get the
    route from goal point to start point.
    Finally, we return the reverse of the list
    '''
    step = goal
    ans = []

    while step != start:
        ans.append(step)
        step = TracebackDict[step]
    ans.append(step)
    return ans[::-1]


class SQUARE:
    '''
    record the data of a square (a point)
    (x, y) = position
    g = g()
    h = heuristic()
    '''

    def __init__(self, x, y, g=float('inf'), h=float('inf')):
        self.x = x
        self.y = y
        self.g = g
        self.h = h


def Astar(start, goal):
    Astar.expanded = 0

    # a dict to remember the last step
    TraceBackDict = {}
    # explored set
    Explored = set()

    # initialize heap
    HEAP = FibonacciHeap()
    NODE = {}
    Index = {}
    (x, y) = start
    NODE[start] = SQUARE(x, y, 0, heuristic(start, goal))
    Index[start] = HEAP.Insert(NODE[start].h, NODE[start])

    while not HEAP.empty():
        # while the heap is not empty, pop the first one
        # and check whether it is goal point
        Astar.expanded += 1
        MIN = HEAP.ExtractMin()
        pos = (MIN.x, MIN.y)
        Explored.add(pos)
        g = MIN.g
        h = MIN.h
        if pos == goal:
            break

        NextStepList = next_step_list(pos)
        for next_step in NextStepList:
            if next_step in Explored:
                continue

            # for the next step which has not been explored,
            # conpute it's f, g, h, and compare with the original one
            (x, y) = next_step
            new_h = heuristic((x, y), goal)
            new_g = g + 1
            new_f = new_g + new_h
            if next_step in NODE:
                if NODE[next_step].g > new_g:
                    # if a node is in the heap, and have smaller g, change it's key,
                    # as Fibonacci heap has O(1) in decreasing key and O(log n) in
                    # increasing key as the same point has the same h(), so new_g < g,
                    # new_h == h --> new_f < f, so we always change key in O(1)
                    NODE[next_step].g = new_g
                    NODE[next_step].h = new_h
                    HEAP.ChangeKey(Index[next_step], new_f)
                    TraceBackDict[next_step] = pos
            else:
                # if it's not in the heap, insert it and
                # add some information to TraceBackDict
                NODE[next_step] = SQUARE(x, y, new_g, new_h)
                Index[next_step] = HEAP.Insert(new_f, NODE[next_step])
                TraceBackDict[next_step] = pos

    # print
    Path = GetRoute(start, goal, TraceBackDict)
    for step in Path:
        STR = '(' + str(step[0]) + ',' + str(step[1]) + ')'
        print(STR, end='')
    print()
    return Astar.expanded
