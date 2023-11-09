import pygame
import random

class Piece():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 50, 50)
        self.prev = None
        self.next = None
        
    def pickUp(self, snake) -> bool:
        if((snake.head.x >= self.x and (snake.head.x +50) <= self.x ) and (snake.head.y >= self.y and (snake.head.y + 50) <= self.y)):
            print("IN")
            snake.addPiece()
            return True
        return False
            
        
class Snake():
    def __init__(self):
        self.head = Piece(200, 200)
        self.tail = Piece(200, 200)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.pieces = [self.head]
        self.length = 0
        
    def addPiece(self):
        piece = Piece(self.tail.next.x-50, self.tail.next.y-50)
        if self.length == 0:
            piece.next = self.head
            self.tail.next = piece
            self.head.prev = piece
        else:
            piece.next = self.tail.next
            self.tail.next.prev = piece
            self.tail.next = piece
        self.pieces.append(piece)
        self.length += 1
        
    def collision(self) -> bool:
        if(self.length == 0):
            return False
        for piece in self.pieces[1:]:
            if piece.x == self.pieces[0].x and piece.y == self.pieces[0].y:
                return True
        return False
    
    def length(self) -> int:
        return self.length

        
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    snake = Snake()
    direction = 0
    x = random.randint(0, 1280 - 50)
    y = random.randint(0, 720 - 50)
    
    while running:
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        for piece in snake.pieces:
            pygame.draw.rect(screen, "red", piece.rect)

        piece = Piece(x, y)
        if(piece.pickUp(snake)):
            x = random.randint(0, 1280 - 50)
            y = random.randint(0, 720 - 50)
        pygame.draw.rect(screen, "green", piece.rect)
        
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
        
        if(snake.collision()):
            print("Oops! Bad!")
            running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
    

if __name__ == "__main__":
    main()
    