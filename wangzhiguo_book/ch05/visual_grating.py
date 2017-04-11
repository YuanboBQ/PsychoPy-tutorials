# import psychopy modules
from psychopy import visual, core
import numpy as np

# create a window
myWin = visual.Window(size=(800,600), units="pix", fullscr=False, color=[0,0,0])

# prepare the stimuli
gabor = visual.GratingStim(myWin, tex='sin', mask='gauss', size=150, sf =1./30, pos=(0,150))
grating = visual.GratingStim(myWin, tex='sqr', mask=None, size = 150, sf = 1./30, pos=(-200,150))
chkboard = visual.GratingStim(myWin, tex='sqrXsqr', mask='circle', size=128, sf=1./30, pos=(200,150))

# custom texture (random value on gray scale)
myTex = np.random.random((8,8))*2-1 # a 8 x 8 grid of values between -1 and 1
grayMask = visual.GratingStim(myWin, tex=myTex, mask=None, size=200, pos=(0,-150))

# show the stimuli
gabor.draw()
grating.draw()
chkboard.draw()
grayMask.draw()
myWin.flip()

# wait for 2 seconds and close the window
core.wait(10)
myWin.close()

