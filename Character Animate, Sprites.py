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

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

#Variables to be used later
x = 250
y = 250
width = 64
height = 64
velocity = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()

#Remember to have the RUNNING_WINDOW code near the start of every pygame program!
RUNNING_WINDOW = True

#Main loop
while RUNNING_WINDOW:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
#The code above tells the program to stay open until the 'X' is pressed.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += velocity
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            Left = False
            walkCount = 0
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
    
    redrawGameWindow()

#Remember to have this line of code at the bottom of every pygame program!
pygame.quit()
