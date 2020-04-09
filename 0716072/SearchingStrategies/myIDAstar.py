from chess_board import *
from .heuristic import myheuristic


def DFS_for_IDAstar(pos, goal, steps, depth):
    myIDAstar.expanded += 1

    if pos == goal:
        # if achieved goal point, return True
        DFS_for_IDAstar.answer.append(pos)
        return True
    if steps + myheuristic(pos, goal) >= depth:
        # (g + h) > depth, return
        return False

    nslist = next_step_list(pos)

    for next_step in nslist:
        PATH = DFS_for_IDAstar(next_step, goal, steps+1, depth)

        if PATH:
            # If Path is True, It means it had achieved the goal point
            # in order to make this code run faster, I save me route
            # in the parameter DFS_for_IDAstar.answer rather than just
            # return [pos] + Path, which Path used to store path(~goal)
            DFS_for_IDAstar.answer.append(pos)
            return True

    return False


DFS_for_IDAstar.answer = []


def myIDAstar(start, goal):
    myIDAstar.expanded = 0
    # initialize parameters
    DFS_for_IDAstar.answer = []
    depth = 0
    while True:
        # IDAstar
        PATH = DFS_for_IDAstar(start, goal, 0, depth)
        # if path exist, return answer
        # else depth++
        if PATH != False:
            Path = DFS_for_IDAstar.answer[::-1]
            # print
            for step in Path:
                STR = '(' + str(step[0]) + ',' + str(step[1]) + ')'
                print(STR, end='')
            print()
            return myIDAstar.expanded
        else:
            depth += 1
