# import psychopy modules
from psychopy import visual, core

# create a window
myWin = visual.Window(size=(800,600), units="pix", fullscr=False, color=[0,0,0])

# change the color of the window and save a JPEG
myWin.flip()
myWin.getMovieFrame()
myWin.saveMovieFrames("gray_window.jpg")

# set mouse invisible
myWin.mouseVisible = False

# print the frame rate of the display
print myWin.fps()

# wait for 2 seconds and close the window
core.wait(2)
myWin.close()

