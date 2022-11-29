import random
import copy

GRID_H = 5
GRID_W = 5
GRID_RAND = 0

class lights_out_game:
    #Inicializa o jogo
    #Aleatoriza a grade se GRID_RAND = 1
    #Zera movimentos realizados
    def __init__(self):
        #Matriz que guarda o estado atual do jogo.
        #Iniciada toda em 1 (todas lampadas acesas)
        self.game_grid = [[1 for i in range(GRID_W)] for j in range(GRID_H)]
        #Matriz que guarda as jogadas já feitas ao tentar solucionar o jogo.
        self.moves_grid = [[0 for i in range(GRID_W)] for j in range(GRID_H)]
        for i in range(GRID_W):
            for j in range(GRID_H):
                if (GRID_RAND == 0):
                    #Inicia a grade totalmente acesa
                    self.game_grid[i][j] = 1
                else:
                    #Aleatoriza grade inicial do jogo
                    self.game_grid[i][j] = random.randint(0, 1)
                #Zera as jogadas feitas
                self.moves_grid[i][j] = 0
    
    #Verifica se o jogo esta em um estado solucionado
    #Retorna booleano
    def isSolved(self):
        solved = True
        for i in range(GRID_W):
            for j in range(GRID_H):
                if self.game_grid[i][j] != 0:
                    solved = False
        return solved

    #Troca o estado atual da lampada nas coordenadas (x, y)
    def toggleLamp(self, x, y):
        if self.game_grid[y][x] == 0:
            self.game_grid[y][x] = 1
        else:
            self.game_grid[y][x] = 0

    #Testa um movimento do jogo
    #Inverte o estado das lampadas em formato de +
    #em torno das coordenadas da acao
    #Retorna jogo apos o movimento mas nao altera o jogo inicial
    def makeMove(self, x, y):
        game_after_move = copy.deepcopy(self)
        if x in range(5) and y in range(5):
            game_after_move.toggleLamp(x, y)
            game_after_move.moves_grid[y][x] += 1
            if x - 1 >= 0:
                game_after_move.toggleLamp(x - 1, y)
            if x + 1 <= GRID_W - 1:
                game_after_move.toggleLamp(x + 1, y)
            if y - 1 >= 0:
                game_after_move.toggleLamp(x, y - 1)
            if y + 1 <= GRID_H - 1:
                game_after_move.toggleLamp(x, y + 1)
            return game_after_move
    
    #Mostra no terminal o estado atual do jogo
    def display(self):
        print("Lights Out")
        for i in range(GRID_W):
            for j in range(GRID_H):
                if self.game_grid[i][j] == 0:
                    print("\u25FB", end = '')
                else:
                    print("\u25FC", end = '')
                    
            print("")
    
    #Retorna a quantidade de movimentos feita até agora
    def getCost(self):
        moves = 0
        for i in range(GRID_W):
            for j in range(GRID_H):
                moves += self.moves_grid[i][j]
        return moves

    #Retorna a heuristica para o estado atual
    #Heuristica atual: Numero de lampadas acesas / maximo de lampadas apagadas em 1 movimento (5)
    def getHeuristic(self):
        lamps = 0
        for i in range(GRID_W):
            for j in range(GRID_H):
                lamps += self.moves_grid[i][j]
        return lamps/5

game = lights_out_game()
game.makeMove(4, 0)
game.display()
print(game.getCost())