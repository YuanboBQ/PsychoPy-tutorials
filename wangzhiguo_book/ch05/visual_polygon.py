# import psychopy modules
from psychopy import visual, core

# create a window
myWin = visual.Window(size=(800,600), units="pix", fullscr=False, color=[0,0,0])

poly = visual.Polygon(myWin, edges=360, radius=100)
poly.draw()
myWin.flip()

# wait for 2 seconds and close the window
core.wait(2)
myWin.close()

