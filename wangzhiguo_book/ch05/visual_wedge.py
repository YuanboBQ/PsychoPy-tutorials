# import psychopy modules
from psychopy import visual, core, event
import numpy as np

# create a window
myWin = visual.Window(size=(600,400), units="pix", fullscr=False, color=[0,0,0])

# prepare the stimuli
wedge = visual.RadialStim(myWin, tex='sqrXsqr', mask=None, size=300, 
                           radialCycles =6, angularCycles=8, visibleWedge=(0,45))                           
while True:
    wedge.ori += 1
    wedge.radialPhase +=0.05
    wedge.draw()
    myWin.flip()
    # press Q to quit the program
    if len(event.getKeys(['q'])):
        myWin.close()
        core.quit()

