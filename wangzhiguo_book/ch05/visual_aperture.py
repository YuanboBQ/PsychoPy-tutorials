# import psychopy modules
from psychopy import visual, core, event
import numpy as np
# create a window
myWin = visual.Window(size=(800,600), units="pix", fullscr=False, color=[0,0,0], allowStencil=True)
myWin.mouseVisible = False
# create an aperture
myApt = visual.Aperture(myWin, size=100, shape='square')
#create a mouse instance
myMouse = event.Mouse(visible=False)
# prepare the stimuli
text = visual.TextStim(myWin, text="Moving window example "*32, height=30,color='black', wrapWidth=760) 
# mouse-contingent moving window
while True:
    myApt.pos = myMouse.getPos()
    text.draw()
    myWin.flip()
    # press Q to quit the program
    if len(event.getKeys(['q'])):
        myWin.close()
        core.quit()

