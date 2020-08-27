"""
high level support for doing this and that
"""
import pygame
pygame.init()
#Remember to have this at the top of every pygame program!

screenWidth = 500
screenLength = 500
#This sets the size of the window.
win = pygame.display.set_mode((screenLength, screenWidth))
#This sets the name of the window.
pygame.display.set_caption("First Game")

#Variables to be used later
x = 250
y = 250
width = 40
height = 60
velocity = 5

isJump = False
jumpCount = 10

#Remember to have the RUNNING_WINDOW code near the start of every pygame program!
RUNNING_WINDOW = True

while RUNNING_WINDOW:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
#The code above tells the program to stay open until the 'X' is pressed.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += velocity
    if not(isJump):
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < screenLength - height:
            y += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #The 'pygame.time.wait()' is for the game to work slower because the faster your computer, the faster the animation happens.
    #Change the nnumber inside depending on how slow or fast you want it to be.
    pygame.time.wait(10)
    pygame.display.update()

#Remember to have this line of code at the bottom of every pygame program!
pygame.quit()
