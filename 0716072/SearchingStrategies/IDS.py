from chess_board import *
import numpy as np


def DFS_for_IDS(pos, goal, depth):
    IDS.expanded += 1
    if depth == 0:
        # when we search a node in the max depth
        # if achieved goal point, return True
        # else return False
        if pos == goal:
            DFS_for_IDS.answer.append(pos)
            return True
        else:
            return False

    nslist = next_step_list(pos)

    for (x, y) in nslist:
        if (x, y) in DFS_for_IDS.Explored:
            # If (x, y) has been explored, continue
            continue

        # Add point to explored set
        DFS_for_IDS.Explored.add((x, y))
        PATH = DFS_for_IDS((x, y), goal, depth-1)
        # Remove point from explored set
        DFS_for_IDS.Explored.remove((x, y))

        if PATH != False:
            # If Path is True, It means it had achieved the goal point
            # in order to make this code run faster, I save me route
            # in the parameter DFS_for_IDS.answer rather than just
            # return [pos] + Path, which Path used to store path(~goal)
            DFS_for_IDS.answer.append(pos)
            return True

    return False


DFS_for_IDS.answer = None
DFS_for_IDS.Explored = set()


def IDS(start, goal):
    IDS.expanded = 0
    # initialize explore set
    DFS_for_IDS.Explored = set()
    DFS_for_IDS.Explored.add(start)

    DFS_for_IDS.answer = []

    depth = 0
    while True:
        # IDsearch
        PATH = DFS_for_IDS(start, goal, depth)
        # if path exist, return answer
        # else depth++
        if PATH != False:
            Path = DFS_for_IDS.answer[::-1]
            # print
            for step in Path:
                STR = '(' + str(step[0]) + ',' + str(step[1]) + ')'
                print(STR, end='')
            print()
            return IDS.expanded
        else:
            depth += 1
