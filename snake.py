import pygame
import random

X_SPACES: int = 25
Y_SPACES: int = 14

PIECE_SIZE: int = 35

class Board():
    board = []
    
    def __init__(self):
        self.board = [[pygame.Rect(50,50,PIECE_SIZE,PIECE_SIZE)]*X_SPACES]*Y_SPACES 
        print(f"row: {len(self.board)} column: {len(self.board[0])}")      
         
    def populateBoard(self):
        print(f"len board = {len(self.board)} len inner = {len(self.board[0])}")
        for r in range(Y_SPACES):
            for c in range(X_SPACES):
                self.board[r][c] = pygame.Rect(50*(r+1), 50*(c+1), PIECE_SIZE, PIECE_SIZE)
                
    def newPieceLocation(self, pieces):
        newPieceX = random.randint(X_SPACES)
        newPieceY = random.randint(Y_SPACES)
        for (x, y) in pieces:
            if(x == newPieceX and y == newPieceY):
                newPieceX = random.randint(X_SPACES)
                newPieceY = random.randint(Y_SPACES)
        return (newPieceX, newPieceY)
            
    def drawBoard(self, screen, pieces, newPiece):
        # for i in range(len(pieces)):
        #     pygame.draw.rect(screen, "red", self.board[pieces[i][0]][pieces[i][1]])
        # pygame.draw.rect(screen, "green", self.board[newPiece[0]][newPiece[1]])
        for i in range(Y_SPACES):
            for j in range(X_SPACES):
                pygame.draw.rect(screen, ("red" if j%2==0 else "green") if i%2==0 else ("green" if j%2==0 else "red"), pygame.Rect(50*(j+1), 50*(i+1), PIECE_SIZE, PIECE_SIZE))
        
    def collision(self, pieces, newPiece):
        for piece in pieces:
            if(piece[0] == newPiece[0] and piece[1] == newPiece[1]):
                 
         
         
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    direction = 0
    
    board = Board()
    board.populateBoard()

    newPiece = [5, 5]

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")
        
        pieces = [[0, 0]]

        board.drawBoard(screen, pieces, newPiece)
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            direction = 0
        elif keys[pygame.K_s]:
            direction = 1
        elif keys[pygame.K_a]:
            direction = 2
        elif keys[pygame.K_d]:
            direction = 3
        
        match direction:
            case 0:
                snake.head.rect.move_ip(0, -500 * dt)
            case 1:
                snake.head.rect.move_ip(0, 500 * dt)
            case 2:
                snake.head.rect.move_ip(-500 * dt, 0)
            case 3:
                snake.head.rect.move_ip(500 * dt, 0)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
    

if __name__ == "__main__":
    main()
    