import numpy as np



def print_flip_board(array):
    #simple, no formatting
    print " "+" ".join([alph for alph in "ABCDEFGHJKLM"[0:len(array)] ])
    for x in xrange(0, len(array)):
        print array[x]

def do_flip(array):
    ainv = array -1
    for x in xrange(0, len(array)):
        for y in xrange(0, len(array[x])):
            if ainv[x][y] == 0:
                array[x][y] = 0
            else:
                array[x][y] = 1
        
def app():
    GAMEOVER = False
    a = np.array([ [0,0,0],
                   [0,0,0],
                   [0,0,0] ])
    # a = np.array([ [0,0],
    #                [0,0] ])

    while not GAMEOVER:        
        print_flip_board(a)
        flipin = raw_input('Flip a piece: ')
        if flipin == 'q':
            GAMEOVER = True
        try:
            x = int(flipin[0])
            y = int(flipin[1])
            a[x][y] = 1
            do_flip(a)
        except:
            print "wrong input"


if __name__=='__main__':
    app()
