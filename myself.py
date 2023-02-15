import pygame


# Shape

# define dimension


def general():
    pass
#   create a grid
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    print(grid)



def start(win):
    going = True

    while going:
        win.fill((198, 242, 249))
        #show a thing where it says press the key to start the game
        pygame.display.update()
        # draw and display update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            if event.type == pygame.KEYDOWN:
                print(event.type)
                general()
    pygame.display.quit()





pygame.font.init()

# size will be set in dimension, win = surface object
win = pygame.display.set_mode(size=(500, 500))
# title
pygame.display.set_caption("Tetris by Wayne")
start(win)
