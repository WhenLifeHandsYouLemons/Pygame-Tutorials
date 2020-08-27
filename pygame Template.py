"""
high level support for doing this and that
"""
import pygame
pygame.init()
#Remember to have this at the top of every pygame program!

#This sets the size of the window.
WIN = pygame.display.set_mode((500, 500))
#This sets the name of the window.
pygame.display.set_caption("First Game")

#Have all your variables in one place to make it easier to change anything.
    ##!!TYPE ALL YOUR VARIABLES HERE!!##
#Change the colour values for bgColor to change the colour of the background.
bgColor = 255, 255, 255

#This make a variable called clock which defines the speed or framerate of the program.
clock = pygame.time.Clock()

#This tells the program how the window should look.
def gameWindowStyle():
    #Here you can write anything to do with the design of the screen and it should update it easily.
    WIN.fill(bgColor)
    pygame.display.update()

#Remember to have the RUNNING_WINDOW code near the start of every pygame program!
#This block of code tells the program to stay open until the 'X' is pressed.
RUNNING_WINDOW = True

#Main loop
while RUNNING_WINDOW:
#This tells the program how many frames per second there should be.
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
#The code above tells the program to stay open until the 'X' is pressed.

#Write all the code for the program under here because this is what will happen when you press run till when you press the 'X'.
    ##!!REMOVE THIS TEXT AND WRITE CODE HERE!!##

#This tells the program to run the def (gameWindowStyle).
    gameWindowStyle()



#Remember to have this line of code at the bottom of every pygame program!
pygame.quit()
