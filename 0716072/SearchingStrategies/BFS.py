from chess_board import *
import queue


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


def BFS(start, goal):
    BFS.expanded = 0
    # initializing the queue for BFS
    Q = queue.Queue()
    Q.put(start)

    # this is a dictionary for two purposes
    # 1. To remember the last step and it will be easier to get route
    # 2. it can also be used as the explored set
    TraceBackDict = {start: 'start'}

    while not Q.empty():
        pos = Q.get()
        BFS.expanded += 1

        if pos == goal:
            break

        NextStepList = next_step_list(pos)
        for NextStep in NextStepList:
            if NextStep in TraceBackDict:
                # for the NextStep which has been explored, skip it
                continue
            Q.put(NextStep)
            TraceBackDict[NextStep] = pos

    # print
    Path = GetRoute(start, goal, TraceBackDict)
    for step in Path:
        STR = '(' + str(step[0]) + ',' + str(step[1]) + ')'
        print(STR, end='')
    print()
    return BFS.expanded
