# this is a simple response time task, Red -> z, Green -> /
# import psychopy modules
from psychopy import visual, core, event
import random
# create aa window
myWin = visual.Window(size=(600,400), units="pix")
# create a target 
tar = visual.GratingStim(myWin, size = 100, tex=None, mask='circle')
# minimal trial list
trials = [['red', 'z'], ['green', 'slash']]
testList = trials[:] * 4 # test a total of 8 trials.
random.shuffle(testList) # randomize the trial order
# open a data file to save the subject responses
data = open('myData.csv', 'w') # comma separated text file
# loop through all the trials
for t in testList:
    tarColor, corResp = t # unpacking the trial parameters
    tar.color = tarColor
    tar.draw() # draw the target 
    myWin.flip()
    tarTime = core.getTime()
    gotKey = False
    while not gotKey: # wait until a key is pressed
        resp = event.getKeys(['z', 'slash'], timeStamped=True)
        if len(resp) > 0: 
            key, respTime = resp[0]
            trialData = [tarColor, corResp, key, tarTime, respTime]
            trialData = map(str, trialData) # make sure all elements are strings
            data.write(','.join(trialData) + '\n') # write trial data to file
            gotKey = True
    myWin.clearBuffer() # clear the display and wait for a second
    myWin.flip()
    core.wait(1.0)

# after all trials have been tested, close the data file and quit
data.close()
core.quit()

