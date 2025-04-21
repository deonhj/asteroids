import pygame
import constants

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
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()