import numpy as np
import sys

ALPHAMAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MIN_BOARD_SIZE = 3
MAX_BOARD_SIZE = 9 #arbitrary limit

def print_flip_board(array):
    print "   "+" ".join([alph for alph in ALPHAMAP[0:len(array)] ])
    for x in xrange(0, len(array)):
        print "%i" % x , array[x]

def do_flip(array):
    ##!! Rules here !! 
    ainv = array -1
    for x in xrange(0, len(array)):
        for y in xrange(0, len(array[x])):
            if ainv[x][y] == 0:
                array[x][y] = 0
            else:
                array[x][y] = 1
        
def app(board_size=MIN_BOARD_SIZE):
    GAMEOVER = False
    board_size = MIN_BOARD_SIZE if board_size < MIN_BOARD_SIZE else board_size
    board_size = MAX_BOARD_SIZE if board_size > MAX_BOARD_SIZE else board_size
    board_square = []
    column = [0 for c in range(0, board_size)]
    board_square = [column for r in range(0, board_size)]
    a = np.array(board_square)

    while not GAMEOVER:        
        print_flip_board(a)
        flipin = raw_input('Flip a piece: ')
        if 'q' in flipin:
            GAMEOVER = True
        else:
            try:
                y = ALPHAMAP.index(chr(ord(flipin[0].upper())))
                x = int(flipin[1])
                a[x][y] = 0 if a[x][y] == 1 else 1
                do_flip(a)
            except:
                print "wrong input"

if __name__=='__main__':
    app( 3 if len(sys.argv) <= 1 else int(sys.argv[1]) )
