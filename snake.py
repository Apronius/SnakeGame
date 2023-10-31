import pygame

class Piece():
    def __init__(self):
        self.pos = None
        self.prev = None
        self.next = None
        
class Snake():
    def __init__(self):
        self.pieces = [self.head]
        self.head = Piece()
        self.tail = Piece()
        self.head.next = None
        self.head.prev = self.tail
        self.tail.next = self.head
        self.head.pos = (200, 200)
        self.length = 0
        
    def addPiece(self):
        piece = Piece()
        if self.length == 0:
            piece.next = self.head
            self.head.prev = piece
        else:
            piece.next = self.head
            piece.prev = self.head.prev
            self.head.prev.next = piece
            self.head.prev = piece
            self.pieces.append(piece)
        self.length += 1
        
    def collision(self) -> bool:
        for piece in self.pieces[1:]:
            if piece.pos == self.pieces[0].pos:
                return True
        return False

        
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    rec = pygame.Rect(posX, posY, 50, 50) 
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        pygame.draw.rect(screen, "red", rec)
        #pygame.draw.rect(screen, "blue", screen.get_width() / 2, screen.get_height() / 2,20,20, 0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            posY -= 300 * dt
        if keys[pygame.K_s]:
            posY += 300 * dt
        if keys[pygame.K_a]:
            posX -= 300 * dt
        if keys[pygame.K_d]:
            posX += 300 * dt


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
    

if __name__ == "__main__":
    main()
    