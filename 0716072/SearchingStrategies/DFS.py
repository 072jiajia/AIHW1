from chess_board import *
import numpy as np


def next_step_list_for_DFS(pos, goal):
    '''
    In DFS, in order to get the answer faster, I let the 
    list of next step have some order. the direction of 
    nslist[0], nslist[1] is the same as (pos -> goal)
    '''
    (x, y) = pos
    nslist = []

    # determine the ↗ ↖ ↘ ↙ which is the first one we go
    if goal[0] > pos[0]:
        dir_x = 1
    else:
        dir_x = -1
    if goal[1] > pos[1]:
        dir_y = 1
    else:
        dir_y = -1

    # append all possible moves to the list
    for (dx, dy) in next_step_list_for_DFS.move:
        nextstep = (x + dx * dir_x, y + dy * dir_y)
        if in_board(nextstep):
            nslist.append(nextstep)
    return nslist


# all direction of moving
next_step_list_for_DFS.move = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                               (-1, -2), (-2, -1), (1, -2), (2, -1)]


def SearchStep(pos, steps):
    DFS.expanded += 1
    '''
    This is the searching steps for DFS
    '''

    if steps >= SearchStep.BestStepNum:
        # if steps >= SearchStep.BestStepNum, we cannot
        # find any path which has smaller number of steps
        # than BestStepNum, so return False
        return False

    if pos == SearchStep.goal:
        # if pos == goal, initialize answer as [SearchStep.goal]
        # and I will push back every step into it
        # return True (path exists)
        SearchStep.BestStepNum = steps
        SearchStep.answer = [SearchStep.goal]
        return True

    ans = False

    NextStepList = next_step_list_for_DFS(pos, SearchStep.goal)
    for nextstep in NextStepList:
        if nextstep not in SearchStep.Explored:
            # if possible next step has not been search
            # change the value into True in the explored table and search it
            SearchStep.Explored.add(nextstep)
            ret = SearchStep(nextstep, steps+1)
            # after searching it change the value into False
            # in the explored table
            SearchStep.Explored.remove(nextstep)
            # if path exist, append this step and make
            # ans = True which means path exists
            if ret != False:
                SearchStep.answer.append(pos)
                ans = True

    return ans


# In order to run faster, I defined some variables here
SearchStep.goal = None
SearchStep.Explored = None
SearchStep.BestStepNum = None
SearchStep.answer = []


def DFS(start, goal):
    DFS.expanded = 0
    # initializing Explored Table
    SearchStep.Explored = set()
    SearchStep.Explored.add(start)

    # initializing other parameters
    SearchStep.start = start
    SearchStep.goal = goal
    SearchStep.BestStepNum = float('inf')
    SearchStep.answer = []
    # DFS
    SearchStep(start, 0)
    # print
    Path = SearchStep.answer[::-1]
    for step in Path:
        STR = '(' + str(step[0]) + ',' + str(step[1]) + ')'
        print(STR, end='')
    print()
    return DFS.expanded
