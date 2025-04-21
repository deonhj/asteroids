import pygame
import constants
from player import Player

def main():

    # print("Starting Asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")

    #initialize the game
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0)) # Fill the screen with black

        player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()