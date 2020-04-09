

# I make it a list in order to easily modify this variable
BOARDSIZE = [8]


def in_board(pos):
    '''
    determine whether the position is in chess board
    '''
    if(pos[0] >= 0 and pos[0] < BOARDSIZE[0] and
       pos[1] >= 0 and pos[1] < BOARDSIZE[0]):
        return True
    return False


def next_step_list(pos):
    '''
    Return a list of the next steps
    '''
    (x, y) = pos
    nslist = []
    if in_board((x-1, y-2)):
        nslist.append((x-1, y-2))
    if in_board((x-2, y-1)):
        nslist.append((x-2, y-1))
    if in_board((x+2, y-1)):
        nslist.append((x+2, y-1))
    if in_board((x+1, y-2)):
        nslist.append((x+1, y-2))
    if in_board((x-1, y+2)):
        nslist.append((x-1, y+2))
    if in_board((x-2, y+1)):
        nslist.append((x-2, y+1))
    if in_board((x+1, y+2)):
        nslist.append((x+1, y+2))
    if in_board((x+2, y+1)):
        nslist.append((x+2, y+1))
    return nslist
