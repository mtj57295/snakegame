from graphics import *

class Vertex:
    def __init__(self, l, r):
        self.ladder = l
        self.rect = r

class Graphics:

    def __init__(self, size):
        self.size = size
        self.graphicBoard = [None]*((size*size))
        self.win = GraphWin('Gameboard', 1500, 950)
        self.win.setCoords(0 ,0, size, size)
        self.sizes = {}
        line = 15
        for i in range(5, 101):
            if line > 2:
                line -= .4
            self.sizes[i] = line

    def getPoint(self, rect):
        x1 = rect.getP1().getX()
        y1 = rect.getP1().getY()
        fx = float(x1) + .5
        fy = float(y1) + .5
        return Point(fx, fy)

    def drawLine(self, rect1, rect2, color, width):
        line = Line(self.getPoint(rect1), self.getPoint(rect2))
        line.setWidth(width)
        line.setFill(color)
        line.draw(self.win)

    def drawLocation(self, rect, color):
        middlePoint = self.getPoint(rect)
        c = Circle(middlePoint, .07)
        c.setFill(color)
        c.draw(self.win)

    def drawPath(self, path, ladders, graph):
        gb = self.graphicBoard
        n = len(path)
        path.reverse()
        r1 = 0
        r2 = 1
        while r2 < n:
            self.drawLocation( gb[ path[r1] ].rect, 'black' )
            ladder = gb[ path[r1] ].ladder
            if ladder in ladders:
                neighbor = graph.graph[ path[r1] ].neighbors
                self.drawLine(gb[ path[r1] ].rect, gb[ neighbor[0].ID - 1 ].rect, 'black', 2)
                self.drawLocation( gb[ neighbor[0].ID - 1 ].rect, 'black' )
                self.drawLocation( gb[ path[r1] ].rect, 'black' )
                roll = path[r2] - (neighbor[0].ID - 1)
                i = neighbor[0].ID - 1
                while i <  neighbor[0].ID - 1 + roll:
                    self.drawLine(gb[i].rect, gb[i + 1].rect, 'black', 2)
                    i += 1
            else:
                roll = path[r2] - path[r1]
                i =  path[r1]
                while i < path[r1] + roll:
                    self.drawLine(gb[i].rect, gb[i + 1].rect, 'black', 2)
                    i += 1
            r1 += 1
            r2 += 1
            if r2 == n:
                self.drawLocation(self.graphicBoard[len(self.graphicBoard)- 1].rect, 'white')

    def drawSnakesAndLadders(self, ladders, snakes):
        graph = self.graphicBoard
        for v in graph:
            if v.ladder in ladders:
                ladder1 = ladders[v.ladder][0]
                ladder2 = ladders[v.ladder][1]
                self.drawLine(graph[ladder1].rect, graph[ladder2].rect, 'green', self.sizes[self.size])
            if v.ladder in snakes:
                snake1 = snakes[v.ladder][0]
                snake2 = snakes[v.ladder][1]
                self.drawLine(graph[snake1].rect, graph[snake2].rect, 'red', self.sizes[self.size])

    def drawSquares(self, r, c, count, board, reverse):
        rect = Rectangle(Point(c ,r), Point(c + 1, r + 1))
        rect.setOutline('white')
        if ((c + r) % 2) == 0:
            rect.setFill('orange')
        else:
            rect.setFill('yellow')
        rect.draw(self.win)
        fc = float(c) + .75
        fr = float(r) + .65
        txt = Text(Point(fc, fr), count)
        txtSize = int(self.sizes[self.size])
        if txtSize < 6:
            txt.setSize(6)
        else:
            txt.setSize(txtSize)
        txt.draw(self.win)
        if reverse:
            c = abs(c - (self.size - 1))
        self.graphicBoard[count] = Vertex(board.board[r][c], rect)

    def drawBoard(self, board):
        self.win.setBackground("white")
        count = 0
        for r in range(0, board.ROWS):
            if r % 2 == 0:
                for c in range(0, board.COLS):
                    self.drawSquares(r, c, count, board, False)
                    count += 1
            else:
                c = board.COLS-1
                while c >= 0:
                    self.drawSquares(r, c, count, board, True)
                    count += 1
                    c -= 1
