# import psychopy modules
from psychopy import visual, core, event, monitors

# set monitor parameters, IMPORTANT!!!
myMon = monitors.Monitor("mac15", distance=57.0, width =32.0)
myMon.setSizePix((800,600))

# create a window
myWin = visual.Window((800,600), monitor=myMon, units="deg")

# prepare stimuli in memory
myGabor = visual.GratingStim(myWin, tex="sin", mask="gauss", size=6.0, ori=45.0)

# draw a gabor on the display and wait for key responses.
while True:
    myGabor.setOri(0.1, "+")
    myGabor.draw()
    myWin.flip()
    key = event.getKeys()
    if len(key)>0:  # press any key to quit
        core.quit()
