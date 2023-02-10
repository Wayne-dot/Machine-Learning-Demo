import pygame


# Shape

# define dimension


def start(win):
    going = False
    # intital draw
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                win.fill((14, 174, 243))
                pygame.time.delay(10000)






pygame.font.init()

# size will be set in dimension, surface object
win = pygame.display.set_mode(size=(500, 500))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            win.fill((14, 174, 243))
            pygame.time.delay(10000)

# title
# pygame.display.set_caption("Tetris by Wayne")


print(win)
