# Example file showing a basic pygame "game loop"
import pygame

class Player():
    
    def __init__(self, pos, prev):
        self.pos = pos
        self.prev = prev
    
    def addLength(self, length):
    
    
def main():
        # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
        
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        pygame.draw.rect(screen, "red", pygame.rect(screen.get_width() / 2, screen.get_height() / 2,20,20), 0)
        #pygame.draw.rect(screen, "blue", screen.get_width() / 2, screen.get_height() / 2,20,20, 0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_pos.y -= 300 
        if keys[pygame.K_s]:
            player_pos.y += 300 
        if keys[pygame.K_a]:
            player_pos.x -= 300 
        if keys[pygame.K_d]:
            player_pos.x += 300 


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
    

if __name__ == "__main__":
    main()
    