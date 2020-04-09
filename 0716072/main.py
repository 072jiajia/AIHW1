from chess_board import *
from SearchingStrategies import *


def input_num(hint):
    n = -1
    while 0 > n or n >= BOARDSIZE[0]:
        try:
            n = int(input(hint))
        except:
            pass
    return n


def INPUT():
    algorithm = ''
    Algos = {'BFS', 'DFS', 'IDS', 'A*', 'IDA*', '0716072A*', '0716072IDA*'}
    hint = 'Please input your algorithm!(๑• ̀д•́ )✧\n'
    hint += 'allowed: BFS, DFS, IDS, A*, IDA*\n'
    hint += '         0716072A*,   0716072IDA*\n'
    hint += 'algorithm: '
    while True:
        algorithm = input(hint)
        if algorithm in Algos:
            break

    print('\nPlease input your starting_x, starting_y, goal_x, goal_y.')

    sx = input_num('starrting_x: ')
    sy = input_num('starrting_y: ')
    gx = input_num('goal_x: ')
    gy = input_num('goal_y: ')

    return algorithm, (sx, sy), (gx, gy)


def run(algorithm, start, goal):
    if algorithm == 'A*':
        ExpandedNodeNum = Astar(start, goal)
    elif algorithm == 'BFS':
        ExpandedNodeNum = BFS(start, goal)
    elif algorithm == 'DFS':
        ExpandedNodeNum = DFS(start, goal)
    elif algorithm == 'IDS':
        ExpandedNodeNum = IDS(start, goal)
    elif algorithm == 'IDA*':
        ExpandedNodeNum = IDAstar(start, goal)
    elif algorithm == '0716072A*':
        ExpandedNodeNum = myAstar(start, goal)
    elif algorithm == '0716072IDA*':
        ExpandedNodeNum = myIDAstar(start, goal)

    # # print Number of Expanded Nodes
    # print(ExpandedNodeNum)


def main():
    algorithm, start, goal = INPUT()
    run(algorithm, start, goal)


if __name__ == '__main__':
    main()
