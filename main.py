from winCheck import *
from firebase import firebase
import socket
'''
game is currently stored online

- create password for game entry

- assign players so they can take turns 

- create second script to emulate second player

- move to browser, not command line?



'''

class Game:

    def __init__(self, height = 6, width = 7):
        self.height = height
        self.width = width
        self.board = []

        # get user's IP address
        self.address = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address.connect(("8.8.8.8", 80))
        print(self.address.getsockname()[0])
        self.address.close()

    def makeBoard(self):

        board = []
        row = []
        self.board = [[' . ' for i in range(self.width)] for j in range(self.height)]

        # board co-ordinates
        # [0][0] = top left
        # [row][col]
        # [0][self.width-1] = top righrt
        # [self.height-1][0] = bottom left

        data = {
                'board': self.board,
                'current_player': 'X',
                'winStatus': False,
                'player1' : self.address

                }

        # add game to database
        result = fire.patch('/myGame', data)


        #update board
        #fire.put('/nestedGame2/board/0/', '5', ' X ')

        # /nestedGame/board/**ROW**/, '**COL**', '*Value*

    def addCounter(self, player):

        self.board = fire.get('/nestedGame2/board', None)

        # get column value for player's counter
        while True:
            try:
                askString = "\nPlayer" + player + ": choose a column"

                while True:
                    colO = input(askString)
                    col = colO - 1
                    if col >= 0 and col < self.width:
                            break
                    elif col == ' ':
                        print "boop"
                    else:
                        print "\nError, try again"
            except NameError:
                print "\nNumbers only please!\n"
                continue

            if self.board[0][col] != ' . ':
                print 'Error, pick again!'
                continue


            else:
                i = self.height - 1
                while True:

                    if self.board[i][col] != ' . ':
                        i -= 1
                        continue
                    else:
                        self.board[i][col] = player
                        break
                break

        # check for winner
        if winCheck(self.board, self.height, self.width, i, col, player):
            print "\nPlayer {0} wins!".format(player)
            return True

        fire.put('/nestedGame2/', 'board', self.board)

        return False

    def printBoard(self):
        self.board = fire.get('/nestedGame2/board', None)
        output = ''
        for r in self.board:
            rowPut = ''
            for c in r:
                rowPut += c
            print rowPut
        numString = ''
        base = ''
        for c in range(0, self.width):
            numString += " " + str( c+1 ) + " "
            base += ' _ '
        print base
        print numString


    def playGame(self):

        while True:
            self.printBoard()
            if self.addCounter(' X '):
                break
            self.printBoard()

            if self.addCounter(' O '):
                break

if __name__ == '__main__':

    fire = firebase.FirebaseApplication('https://firerow-971dc.firebaseio.com')


    g = Game()
    g.makeBoard()
    g.playGame()
