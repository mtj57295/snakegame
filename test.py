import sys
sys.dont_write_bytecode = True
from CreateBoard import Board
from SolveBoard import Graph
from Graphics import Graphics

def initBoard():
    value = int(raw_input('Enter number of rows and cols (5 min/ 30 max): '))
    if value < 5:
        print 'Below 5'
        exit()
    numObstacles = int(raw_input('Enter number of ladders and snakes to produce (max 40% ladders): '))
    if float(numObstacles)/(value*value) > .40 or float(numObstacles)/(value*value) == .40:
        print 'Higer than 40%'
        exit()
    board = Board(value, value)
    board.createObstacles(numObstacles)
    board.printBoard()
    return board

def initGraph(ladders, snakes):
    graph = Graph(board.ROWS*board.COLS)
    dice = [1, 2, 3, 4, 5, 6]
    i = 0
    for r in range(board.ROWS):
        for c in range(board.COLS):
            graph.addVertex(i)
            ladder = board.board[r][c]
            if ladder[0] == 'L':
                if ladder in ladders:
                    ladders[ladder] += [i]
                else:
                    ladders[ladder] = [i]
            snake = board.board[r][c]
            if snake[0] == 'S':
                if snake in snakes:
                    snakes[snake] += [i]
                else:
                    snakes[snake] = [i]
            i += 1

    for i in range(graph.V):
        for roll in dice:
            if i + roll <= graph.V:
                graph.addEdge(i, i + roll)

    for l in ladders:
        graph.graph[ ladders[l][0] ].neighbors = graph.graph[ ladders[l][1] ].neighbors
    for s in snakes:
        graph.graph[ snakes[s][1] ].neighbors = graph.graph[ snakes[s][0] ].neighbors
    return graph

ladders = {}
snakes = {}
board = initBoard()
graph = initGraph(ladders, snakes)

graph.BFS(0)
graph.printPath(graph.V)
print "Total Number of rolls is: " + str(len(graph.graph[graph.V].path))

graphics = Graphics(board.ROWS)
graphics.drawBoard(board)
graphics.drawSnakesAndLadders(ladders, snakes)
graphics.drawPath(graph.graph[graph.V].path, ladders, graph)
graphics.win.getMouse()
graphics.win.close()
