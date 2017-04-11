# import psychopy modules
from psychopy import visual, core, event
import numpy as np
# create two windows
win0 = visual.Window(size=(600,400), units="pix", screen=0)
win1 = visual.Window(size=(600,400), units="pix", screen=1)

# create an aperture
wedge = visual.RadialStim(win0, radialCycles=8, angularCycles=8, size=400, visibleWedge=(0,30))
msg = visual.TextStim(win1, text='', height=30,color='black', wrapWidth=760) 

# mouse-contingent moving window
while True:
    wedge.ori += 5
    cycleN = int(wedge.ori/360) + 1
    msg.text='This is Cycle # ' + str(cycleN)
    wedge.draw()
    msg.draw()
    win0.flip()
    win1.flip()
    # press Q to quit the program
    if len(event.getKeys(['q'])):
        core.quit()

