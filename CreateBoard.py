import random
class Board:
    def __init__(self, rows, cols):
        self.ROWS = rows
        self.COLS = cols
        self.board = [[0 for j in range(cols)]for i in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                self.board[r][c] = str(count)
                count += 1

    def getPoint(self, y1, y2):
        x = random.randint(0, self.COLS-1)
        y = random.randint(y1, y2)
        while self.board[y][x][0] == 'S' or self.board[y][x][0] == 'L':
            x = random.randint(0, self.COLS-1)
            y = random.randint(y1, y2)
        return [y, x]

    def createPoints(self, type, i):
        point1 = self.getPoint(0, self.ROWS-2)
        if point1 == None:
            return
        point2 = self.getPoint(point1[0] + 1, self.ROWS-1)
        if point2 == None:
            return
        self.board[ point1[0] ][ point1[1] ] = type + str(i)
        self.board[ point2[0] ][ point2[1] ] = type + str(i)

    def createObstacles(self, nums):
        s = 0
        l = 0
        for i in range(nums):
            if i % 2 == 0:
                self.createPoints('S', s)
                s += 1
            else:
                self.createPoints('L', l)
                l += 1

    def printBoard(self):
        for r in range(self.ROWS):
            for c in range(self.COLS):
                print str(self.board[r][c]).ljust(5),
            print '\n'

    def checkObstacles(self):
        board = self.board
        map = {}
        countS = 0
        countL = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                s = board[r][c]
                if 'S' == s[0]:
                    if s in map:
                        map[s] += 1
                    else:
                        map[s] = 1
                        countS += 1
                l = board[r][c]
                if 'L' == l[0]:
                    if l in map:
                        map[l] += 1
                    else:
                        map[l] = 1
                        countL += 1
        for i in map:
            print str(i) + " : " + str(map[i])
        print "Total in Map: " + str(len(map))
