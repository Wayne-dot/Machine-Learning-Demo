import pygame


# Shape

# define dimension


def general():
    pass



def start(win):
    going = True

    while going:
        win.fill((14, 174, 243))
        pygame.display.update()
        # draw and display update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            if event.type == pygame.KEYDOWN:
                print(event.type)
                general()


pygame.font.init()

# size will be set in dimension, win = surface object
win = pygame.display.set_mode(size=(500, 500))
# title
pygame.display.set_caption("Tetris by Wayne")

start(win)

print(win)
