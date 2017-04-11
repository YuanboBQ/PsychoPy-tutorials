#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), Sat Sep 21 10:36:44 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import csv # so we can create the practice and test trials
import random # so we can randomize
import Tkinter # creates the demographic sheet

# get image file names
projectDirectory= os.getcwd()
topFileNames=os.listdir(os.path.join(projectDirectory,'top')) # all top JPEG files
bottomFileNames=os.listdir(os.path.join(projectDirectory,'bottom')) # all bottom JPEG files
# remove any non-jpeg files
restartLoop = True
while restartLoop:
    for i in range(len(topFileNames)):
        if ".JPEG" not in topFileNames[i]:
            topFileNames.pop(i)
            restartLoop = True
            break
        if ".JPEG" not in bottomFileNames[i]:
            bottomFileNames.pop(i)
            restartLoop = True
            break
        if i == len(topFileNames)-1:
            restartLoop = False
testConditions=list(csv.reader(open('testFaceConditions.csv','rU'))) # 4 testTrialTypes X 3 alignment X 2 cue

# remove header row from testConditions file
testConditions=testConditions[1:]

# create all possible 720 trials (24 * 30)
testConditionsAll = testConditions*30

random.shuffle(testConditionsAll)

# expand testCondition information into separable objects
topCongruent, bottomCongruent, xPosTop, yPosTop, xPosBot, yPosBot, cueTop, cueBot, corAnsOne, corAnsTwo = zip(*testConditionsAll)


# 196 possible study images * 4 so that the possible pool >= 720
# this also ensures each image max==4 presentations
studyTopPossible = topFileNames * 4
studyTopFaces = random.sample(studyTopPossible,720)
random.shuffle(studyTopFaces)

studyBottomPossible = bottomFileNames * 4
studyBottomFaces = random.sample(studyBottomPossible,720)
random.shuffle(studyBottomFaces)

# create a file for this session's test trials
# since all of this information is saved in the data file, we will rewrite the file for each subject
thisSession='thisTestSession.csv'
with open(thisSession, 'wb') as w:
    writer=csv.writer(w)
    writer.writerow(['studyTopFaces','studyBottomFaces','testTopFaces','testBottomFaces', 'xPosTop', 'yPosTop', 'xPosBot', 'yPosBot', 'cueTop', 'cueBot', 'corAnsOne','corAnsTwo'])
    for i in range(len(studyTopFaces)):
        if topCongruent[i] == 1:
            topSel = studyTopFaces[i] # testTop==studyTop
        else:
            rSel = random.randint(0,195)
            if topFileNames[rSel] != studyTopFaces[i]: # make sure we didn't randomly select studyTopFace[i]
                topSel = topFileNames[rSel]
            else:
                rSel = random.randint(0,195) # if we did randomly select studyTopFace[i], reselect
                topSel = topFileNames[rSel]
        if bottomCongruent[i] == 1:
            botSel = studyBottomFaces[i]
        else:
            rSel = random.randint(0,195)
            if bottomFileNames[rSel] != studyBottomFaces[i]:
                botSel = bottomFileNames[rSel]
            else:
                rSel = random.randint(0,195)
                botSel = bottomFileNames[rSel]
        # write out the information for all 720 trials for this session
        writer.writerow([studyTopFaces[i],studyBottomFaces[i],topSel, botSel, xPosTop[i], yPosTop[i], xPosBot[i], yPosBot[i], cueTop[i], cueBot[i], corAnsOne[i],corAnsTwo[i]])

#select 16 faces for the practice trials
practiceTopFaces = random.sample(studyTopPossible,16)
practiceBotFaces = random.sample(studyBottomPossible,16)
practiceConditions = random.sample(testConditions,16)

# expand practiceConditions information into separable objects
topCongruent, bottomCongruent, xPosTop, yPosTop, xPosBot, yPosBot, cueTop, cueBot, corAnsOne, corAnsTwo = zip(*practiceConditions)

# create a file for this session's practice trials
thisPracticeSession='thisPracticeSession.csv'
with open(thisPracticeSession, 'wb') as w:
    writer=csv.writer(w)
    writer.writerow(['studyTopFaces','studyBottomFaces','testTopFaces','testBottomFaces', 'xPosTop', 'yPosTop', 'xPosBot', 'yPosBot', 'cueTop', 'cueBot', 'corAnsOne','corAnsTwo'])
    for i in range(len(practiceTopFaces)):
        if topCongruent[i] == 1:
            topSel = practiceTopFaces[i] # testTop==studyTop
        else:
            rSel = random.randint(0,195)
            if topFileNames[rSel] != practiceTopFaces[i]: # make sure we didn't randomly select studyTopFace[i]
                topSel = topFileNames[rSel]
            else:
                rSel = random.randint(0,195) # if we did randomly select studyTopFace[i], reselect
                topSel = topFileNames[rSel]
        if bottomCongruent[i] == 1:
            botSel = practiceBotFaces[i]
        else:
            rSel = random.randint(0,195)
            if bottomFileNames[rSel] != practiceBotFaces[i]:
                botSel = bottomFileNames[rSel]
            else:
                rSel = random.randint(0,195)
                botSel = bottomFileNames[rSel]
        # write out the information for all 720 trials for this session
        writer.writerow([studyTopFaces[i],studyBottomFaces[i],topSel, botSel, xPosTop[i], yPosTop[i], xPosBot[i], yPosBot[i], cueTop[i], cueBot[i],corAnsOne[i],corAnsTwo[i]])

# Store info about the experiment session
expName = u'sequentialResponseBuilder'  # from the Builder filename that created this script
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win._getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "practInstr"
practInstrClock = core.Clock()
practiceInstructions = visual.TextStim(win=win, ori=0, name='practiceInstructions',
    text=u'Press [s] for same\r\nPress [k] for different\r\n\r\nPress [spacebar] to begin',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationBackground = visual.Rect(win=win, name='fixationBackground',units=u'pix', 
    width=[256, 259][0], height=[256, 259][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace=u'rgb',
    fillColor=[-1,-1,-1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
fixationCross = visual.TextStim(win=win, ori=0, name='fixationCross',
    text='+',    font='Arial',
    units='pix', pos=[0, -1.5], height=200, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "studyTrial"
studyTrialClock = core.Clock()
studyFaceTop = visual.ImageStim(win=win, name='studyFaceTop',units=u'pix',
    image='sin', mask=None,
    ori=0, pos=[0,67], size=[256,131],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
studyFaceBottom = visual.ImageStim(win=win, name='studyFaceBottom',units=u'pix',
    image='sin', mask=None,
    ori=0, pos=[0,-64], size=[256,128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
topOval = visual.ImageStim(win=win, name='topOval',units=u'pix',
    image=u'oval_top.png', mask=None,
    ori=0, pos=[0, 67], size=[256, 128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)
botOval = visual.ImageStim(win=win, name='botOval',units=u'pix',
    image=u'oval_bottom.png', mask=None,
    ori=0, pos=[0, -64], size=[256, 128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "maskTrial"
maskTrialClock = core.Clock()
mask = visual.ImageStim(win=win, name='mask',units='pix',
    image='mask_gb.png', mask=None,
    ori=0, pos=[0, 0], size=[256, 259],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "testTrial"
testTrialClock = core.Clock()
topTest = visual.ImageStim(win=win, name='topTest',units='pix',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[256,131],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
topOvalTest = visual.ImageStim(win=win, name='topOvalTest',units=u'pix',
    image=u'oval_top.png', mask=None,
    ori=0, pos=[0,0], size=[256, 128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)
bottomTest = visual.ImageStim(win=win, name='bottomTest',units='pix',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[256, 128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)
botOvalTest = visual.ImageStim(win=win, name='botOvalTest',units=u'pix',
    image=u'oval_bottom.png', mask=None,
    ori=0, pos=[0,0], size=[256, 128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-4.0)
cue1top = visual.ImageStim(win=win, name='cue1top',units=u'pix',
    image=u'cueTop.png', mask=None,
    ori=0, pos=[0,0], #size=[128, 25],
    color=[1,1,1], colorSpace=u'rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-5.0)
cue1bottom = visual.ImageStim(win=win, name='cue1bottom',units=u'pix',
    image=u'cueBottom.png', mask=None,
    ori=0, pos=[0,0], #size=[128, 25],
    color=[1,1,1], colorSpace=u'rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-6.0)
backgroundMisaligned = visual.Rect(win=win, name='backgroundMisaligned',units=u'pix',
    width=[320, 262][0], height=[320, 262][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace=u'rgb',
    fillColor=[-1,-1,-1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=-0.0)
backgroundVeryMisaligned = visual.Rect(win=win, name='backgroundVeryMisaligned',units=u'pix',
    width=[384, 262][0], height=[384, 262][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace=u'rgb',
    fillColor=[-1,-1,-1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=-0.0)
backgroundStripe = visual.Rect(win=win, name='backgroundStripe',units=u'pix',
    width=[256, 3][0], height=[256, 3][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=0.0)
backgroundStripeMisaligned = visual.Rect(win=win, name='backgroundStripeMisaligned',units=u'pix',
    width=[320, 6][0], height=[320, 6][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=0.0)
backgroundStripeVeryMisaligned = visual.Rect(win=win, name='backgroundStripeVeryMisaligned',units=u'pix',
    width=[384, 6][0], height=[320, 6][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=0.0)
    
# Initialize components for Routine "testTrial2"
testTrial2Clock = core.Clock()
topTest2 = visual.ImageStim(win=win, name='topTest2',units='pix',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[256,131],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
topOvalTest2 = visual.ImageStim(win=win, name='topOvalTest2',units=u'pix',
    image=u'oval_top.png', mask=None,
    ori=0, pos=[0,0], size=[256, 128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)
bottomTest2 = visual.ImageStim(win=win, name='bottomTest2',units='pix',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[256, 128],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)
botOvalTest2 = visual.ImageStim(win=win, name='botOvalTest2',units=u'pix',
    image=u'oval_bottom.png', mask=None,
    ori=0, pos=[0,0], size=[256, 128],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-4.0)
cue2top = visual.ImageStim(win=win, name='cue2top',units=u'pix',
    image=u'cueTop.png', mask=None,
    ori=0, pos=[0,0], #size=[128, 25],
    color=[1,1,1], colorSpace=u'rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-5.0)
cue2bottom = visual.ImageStim(win=win, name='cue2bottom',units=u'pix',
    image=u'cueBottom.png', mask=None,
    ori=0, pos=[0,0], #size=[128, 25],
    color=[1,1,1], colorSpace=u'rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-6.0)
backgroundMisaligned = visual.Rect(win=win, name='backgroundMisaligned',units=u'pix',
    width=[320, 262][0], height=[320, 262][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace=u'rgb',
    fillColor=[-1,-1,-1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=-0.0)
backgroundVeryMisaligned = visual.Rect(win=win, name='backgroundVeryMisaligned',units=u'pix',
    width=[384, 262][0], height=[384, 262][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace=u'rgb',
    fillColor=[-1,-1,-1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=-0.0)
backgroundStripe = visual.Rect(win=win, name='backgroundStripe',units=u'pix',
    width=[256, 3][0], height=[256, 3][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=0.0)
backgroundStripeMisaligned = visual.Rect(win=win, name='backgroundStripeMisaligned',units=u'pix',
    width=[320, 6][0], height=[320, 6][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=0.0)
backgroundStripeVeryMisaligned = visual.Rect(win=win, name='backgroundStripeVeryMisaligned',units=u'pix',
    width=[384, 6][0], height=[320, 6][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True, depth=0.0)

# Initialize components for Routine "testInst"
testInstClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Press [s] for same\r\nPress [k] for different\r\n\r\nPress [spacebar] to begin',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

#------Prepare to start Routine "practInstr"-------
t = 0
practInstrClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
startPractice = event.BuilderKeyResponse()  # create an object of type KeyResponse
startPractice.status = NOT_STARTED
# keep track of which components have finished
practInstrComponents = []
practInstrComponents.append(practiceInstructions)
practInstrComponents.append(startPractice)
for thisComponent in practInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "practInstr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = practInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *practiceInstructions* updates
    if t >= 0.0 and practiceInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        practiceInstructions.tStart = t  # underestimates by a little under one frame
        practiceInstructions.frameNStart = frameN  # exact frame index
        practiceInstructions.setAutoDraw(True)

    # *startPractice* updates
    if t >= 0.0 and startPractice.status == NOT_STARTED:
        # keep track of start time/frame for later
        startPractice.tStart = t  # underestimates by a little under one frame
        startPractice.frameNStart = frameN  # exact frame index
        startPractice.status = STARTED
        # keyboard checking is just starting
        startPractice.clock.reset()  # now t=0
        event.clearEvents()
    if startPractice.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            startPractice.keys = theseKeys[-1]  # just the last key pressed
            startPractice.rt = startPractice.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "practInstr"-------
for thisComponent in practInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
practiceLoop = data.TrialHandler(nReps=1, method=u'random',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'thisPracticeSession.csv'),
    seed=None, name='practiceLoop')
thisExp.addLoop(practiceLoop)  # add the loop to the experiment
thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop.keys():
        exec(paramName + '= thisPracticeLoop.' + paramName)

for thisPracticeLoop in practiceLoop:
    currentLoop = practiceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop.keys():
            exec(paramName + '= thisPracticeLoop.' + paramName)

    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(fixationBackground)
    fixationComponents.append(fixationCross)
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *fixationBackground* updates
        if t >= 0.0 and fixationBackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationBackground.tStart = t  # underestimates by a little under one frame
            fixationBackground.frameNStart = frameN  # exact frame index
            fixationBackground.setAutoDraw(True)
        elif fixationBackground.status == STARTED and t >= (0.0 + .5):
            fixationBackground.setAutoDraw(False)

        # *fixationCross* updates
        if t >= 0.0 and fixationCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross.tStart = t  # underestimates by a little under one frame
            fixationCross.frameNStart = frameN  # exact frame index
            fixationCross.setAutoDraw(True)
        elif fixationCross.status == STARTED and t >= (0.0 + .5):
            fixationCross.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "studyTrial"-------
    t = 0
    studyTrialClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    studyFaceTop.setImage(os.path.join('top',studyTopFaces))
    studyFaceBottom.setImage(os.path.join('bottom',studyBottomFaces))
    # keep track of which components have finished
    studyTrialComponents = []
    studyTrialComponents.append(studyFaceTop)
    studyTrialComponents.append(studyFaceBottom)
    studyTrialComponents.append(topOval)
    studyTrialComponents.append(botOval)
    for thisComponent in studyTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "studyTrial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = studyTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *studyFaceTop* updates
        if t >= 0.0 and studyFaceTop.status == NOT_STARTED:
            # keep track of start time/frame for later
            studyFaceTop.tStart = t  # underestimates by a little under one frame
            studyFaceTop.frameNStart = frameN  # exact frame index
            studyFaceTop.setAutoDraw(True)
        elif studyFaceTop.status == STARTED and t >= (0.0 + .4):
            studyFaceTop.setAutoDraw(False)

        # *studyFaceBottom* updates
        if t >= 0.0 and studyFaceBottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            studyFaceBottom.tStart = t  # underestimates by a little under one frame
            studyFaceBottom.frameNStart = frameN  # exact frame index
            studyFaceBottom.setAutoDraw(True)
        elif studyFaceBottom.status == STARTED and t >= (0.0 + .4):
            studyFaceBottom.setAutoDraw(False)

        # *topOval* updates
        if t >= 0.0 and topOval.status == NOT_STARTED:
            # keep track of start time/frame for later
            topOval.tStart = t  # underestimates by a little under one frame
            topOval.frameNStart = frameN  # exact frame index
            topOval.setAutoDraw(True)
        elif topOval.status == STARTED and t >= (0.0 + .4):
            topOval.setAutoDraw(False)

        # *botOval* updates
        if t >= 0.0 and botOval.status == NOT_STARTED:
            # keep track of start time/frame for later
            botOval.tStart = t  # underestimates by a little under one frame
            botOval.frameNStart = frameN  # exact frame index
            botOval.setAutoDraw(True)
        elif botOval.status == STARTED and t >= (0.0 + .4):
            botOval.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in studyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "studyTrial"-------
    for thisComponent in studyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "maskTrial"-------
    t = 0
    maskTrialClock.reset()  # clock
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskTrialComponents = []
    maskTrialComponents.append(mask)
    for thisComponent in maskTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "maskTrial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *mask* updates
        if t >= 0.0 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # underestimates by a little under one frame
            mask.frameNStart = frameN  # exact frame index
            mask.setAutoDraw(True)
        elif mask.status == STARTED and t >= (0.0 + 2.0):
            mask.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "maskTrial"-------
    for thisComponent in maskTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "testTrial"-------
    t = 0
    testTrialClock.reset()  # clock
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    topTest.setPos([xPosTop,yPosTop])
    topTest.setImage(os.path.join('top',testTopFaces))
    topOvalTest.setPos([xPosTop, yPosTop])
    bottomTest.setPos([xPosBot,yPosBot])
    bottomTest.setImage(os.path.join('bottom',testBottomFaces))
    botOvalTest.setPos([xPosBot, yPosBot])
    cue1top.setOpacity(cueTop)
    cue1top.setPos([xPosTop,yPosTop+34])
    cue1bottom.setOpacity(cueBot)
    cue1bottom.setPos([xPosBot,yPosBot-32])
    cue1response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    cue1response.status = NOT_STARTED
    # keep track of which components have finished
    testTrialComponents = []
    if xPosTop == 32:
        background = backgroundMisaligned
        strip = backgroundStripeMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    elif xPosTop == 64:
        background = backgroundVeryMisaligned
        strip = backgroundStripeVeryMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    else:
        background = fixationBackground
        strip = backgroundStripe
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    testTrialComponents.append(topTest)
    testTrialComponents.append(topOvalTest)
    testTrialComponents.append(bottomTest)
    testTrialComponents.append(botOvalTest)
    testTrialComponents.append(cue1top)
    testTrialComponents.append(cue1bottom)
    testTrialComponents.append(cue1response)
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "testTrial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *topTest* updates
        if t >= 0.0 and topTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            topTest.tStart = t  # underestimates by a little under one frame
            topTest.frameNStart = frameN  # exact frame index
            topTest.setAutoDraw(True)
            background.setAutoDraw(True)
            strip.setAutoDraw(True)
        elif topTest.status == STARTED and t >= (0.0 + 2.5):
            topTest.setAutoDraw(False)
            background.setAutoDraw(False)
            strip.setAutoDraw(False)

        # *topOvalTest* updates
        if t >= 0.0 and topOvalTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            topOvalTest.tStart = t  # underestimates by a little under one frame
            topOvalTest.frameNStart = frameN  # exact frame index
            topOvalTest.setAutoDraw(True)
        elif topOvalTest.status == STARTED and t >= (0.0 + 2.5):
            topOvalTest.setAutoDraw(False)

        # *bottomTest* updates
        if t >= 0.0 and bottomTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottomTest.tStart = t  # underestimates by a little under one frame
            bottomTest.frameNStart = frameN  # exact frame index
            bottomTest.setAutoDraw(True)
        elif bottomTest.status == STARTED and t >= (0.0 + 2.5):
            bottomTest.setAutoDraw(False)

        # *botOvalTest* updates
        if t >= 0.0 and botOvalTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            botOvalTest.tStart = t  # underestimates by a little under one frame
            botOvalTest.frameNStart = frameN  # exact frame index
            botOvalTest.setAutoDraw(True)
        elif botOvalTest.status == STARTED and t >= (0.0 + 2.5):
            botOvalTest.setAutoDraw(False)

        # *cue1top* updates
        if t >= 0.0 and cue1top.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue1top.tStart = t  # underestimates by a little under one frame
            cue1top.frameNStart = frameN  # exact frame index
            cue1top.setAutoDraw(True)
        elif cue1top.status == STARTED and t >= (0.0 + 2.5):
            cue1top.setAutoDraw(False)

        # *cue1bottom* updates
        if t >= 0.0 and cue1bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue1bottom.tStart = t  # underestimates by a little under one frame
            cue1bottom.frameNStart = frameN  # exact frame index
            cue1bottom.setAutoDraw(True)
        elif cue1bottom.status == STARTED and t >= (0.0 + 2.5):
            cue1bottom.setAutoDraw(False)

        # *cue1response* updates
        if t >= 0.0 and cue1response.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue1response.tStart = t  # underestimates by a little under one frame
            cue1response.frameNStart = frameN  # exact frame index
            cue1response.status = STARTED
            # keyboard checking is just starting
            cue1response.clock.reset()  # now t=0
            event.clearEvents()
        elif cue1response.status == STARTED and t >= (0.0 + 2.5):
            cue1response.status = STOPPED
        if cue1response.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'k'])
            if len(theseKeys) > 0:  # at least one key was pressed
                cue1response.keys = theseKeys[-1]  # just the last key pressed
                cue1response.rt = cue1response.clock.getTime()
                # was this 'correct'?
                if (cue1response.keys == str(corAnsOne)): cue1response.corr = 1
                else: cue1response.corr=0
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "testTrial"-------
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(cue1response.keys) == 0:  # No response was made
       cue1response.keys=None
       # was no response the correct answer?!
       if str(corAnsOne).lower() == 'none': cue1response.corr = 1  # correct non-response
       else: cue1response.corr = 0  # failed to respond (incorrectly)
    # store data for practiceLoop (TrialHandler)
    practiceLoop.addData('cue1response.keys',cue1response.keys)
    practiceLoop.addData('cue1response.corr', cue1response.corr)
    if cue1response.keys != None:  # we had a response
        practiceLoop.addData('cue1response.rt', cue1response.rt)

    #------Prepare to start Routine "testTrial2"-------
    t = 0
    testTrial2Clock.reset()  # clock
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    topTest2.setPos([xPosTop,yPosTop])
    topTest2.setImage(os.path.join('top',testTopFaces))
    topOvalTest2.setPos([xPosTop, yPosTop])
    bottomTest2.setPos([xPosBot,yPosBot])
    bottomTest2.setImage(os.path.join('bottom',testBottomFaces))
    botOvalTest2.setPos([xPosBot, yPosBot])
    cue2top.setOpacity(1-cueTop)
    cue2top.setPos([xPosTop,yPosTop+34])
    cue2bottom.setOpacity(1-cueBot)
    cue2bottom.setPos([xPosBot,yPosBot-32])
    cue2response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    cue2response.status = NOT_STARTED
    # keep track of which components have finished
    testTrialComponents = []
    if xPosTop == 32:
        background = backgroundMisaligned
        strip = backgroundStripeMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    elif xPosTop == 64:
        background = backgroundVeryMisaligned
        strip = backgroundStripeVeryMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    else:
        background = fixationBackground
        strip = backgroundStripe
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    testTrialComponents.append(topTest2)
    testTrialComponents.append(topOvalTest2)
    testTrialComponents.append(bottomTest2)
    testTrialComponents.append(botOvalTest2)
    testTrialComponents.append(cue2top)
    testTrialComponents.append(cue2bottom)
    testTrialComponents.append(cue2response)
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "testTrial2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testTrial2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *topTest2* updates
        if t >= 0.0 and topTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            topTest2.tStart = t  # underestimates by a little under one frame
            topTest2.frameNStart = frameN  # exact frame index
            topTest2.setAutoDraw(True)
            background.setAutoDraw(True)
            strip.setAutoDraw(True)
        elif topTest2.status == STARTED and t >= (0.0 + 2.5):
            topTest2.setAutoDraw(False)
            background.setAutoDraw(False)
            strip.setAutoDraw(False)

        # *topOvalTest2* updates
        if t >= 0.0 and topOvalTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            topOvalTest2.tStart = t  # underestimates by a little under one frame
            topOvalTest2.frameNStart = frameN  # exact frame index
            topOvalTest2.setAutoDraw(True)
        elif topOvalTest2.status == STARTED and t >= (0.0 + 2.5):
            topOvalTest2.setAutoDraw(False)

        # *bottomTest* updates
        if t >= 0.0 and bottomTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottomTest2.tStart = t  # underestimates by a little under one frame
            bottomTest2.frameNStart = frameN  # exact frame index
            bottomTest2.setAutoDraw(True)
        elif bottomTest2.status == STARTED and t >= (0.0 + 2.5):
            bottomTest2.setAutoDraw(False)

        # *botOvalTest2* updates
        if t >= 0.0 and botOvalTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            botOvalTest2.tStart = t  # underestimates by a little under one frame
            botOvalTest2.frameNStart = frameN  # exact frame index
            botOvalTest2.setAutoDraw(True)
        elif botOvalTest2.status == STARTED and t >= (0.0 + 2.5):
            botOvalTest2.setAutoDraw(False)

        # *cue2top* updates
        if t >= 0.0 and cue2top.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue2top.tStart = t  # underestimates by a little under one frame
            cue2top.frameNStart = frameN  # exact frame index
            cue2top.setAutoDraw(True)
        elif cue2top.status == STARTED and t >= (0.0 + 2.5):
            cue2top.setAutoDraw(False)

        # *cue2bottom* updates
        if t >= 0.0 and cue2bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue2bottom.tStart = t  # underestimates by a little under one frame
            cue2bottom.frameNStart = frameN  # exact frame index
            cue2bottom.setAutoDraw(True)
        elif cue2bottom.status == STARTED and t >= (0.0 + 2.5):
            cue2bottom.setAutoDraw(False)

        # *cue2response* updates
        if t >= 0.0 and cue2response.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue2response.tStart = t  # underestimates by a little under one frame
            cue2response.frameNStart = frameN  # exact frame index
            cue2response.status = STARTED
            # keyboard checking is just starting
            cue2response.clock.reset()  # now t=0
            event.clearEvents()
        elif cue2response.status == STARTED and t >= (0.0 + 2.5):
            cue2response.status = STOPPED
        if cue2response.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'k'])
            if len(theseKeys) > 0:  # at least one key was pressed
                cue2response.keys = theseKeys[-1]  # just the last key pressed
                cue2response.rt = cue2response.clock.getTime()
                # was this 'correct'?
                if (cue2response.keys == str(corAnsOne)): cue2response.corr = 1
                else: cue2response.corr=0
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "testTrial"-------
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(cue2response.keys) == 0:  # No response was made
       cue2response.keys=None
       # was no response the correct answer?!
       if str(corAnsOne).lower() == 'none': cue1response.corr = 1  # correct non-response
       else: cue2response.corr = 0  # failed to respond (incorrectly)
    # store data for practiceLoop (TrialHandler)
    practiceLoop.addData('cue2response.keys',cue2response.keys)
    practiceLoop.addData('cue2response.corr', cue2response.corr)
    if cue2response.keys != None:  # we had a response
        practiceLoop.addData('cue2response.rt', cue2response.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'practiceLoop'


#------Prepare to start Routine "testInst"-------
t = 0
testInstClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
testInstComponents = []
testInstComponents.append(text)
testInstComponents.append(key_resp_2)
for thisComponent in testInstComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "testInst"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = testInstClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "testInst"-------
for thisComponent in testInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
testLoop = data.TrialHandler(nReps=1, method=u'random',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'thisTestSession.csv'),
    seed=None, name='testLoop')
thisExp.addLoop(testLoop)  # add the loop to the experiment
thisTestLoop = testLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTestLoop.rgb)
if thisTestLoop != None:
    for paramName in thisTestLoop.keys():
        exec(paramName + '= thisTestLoop.' + paramName)

for thisTestLoop in testLoop:
    currentLoop = testLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTestLoop.rgb)
    if thisTestLoop != None:
        for paramName in thisTestLoop.keys():
            exec(paramName + '= thisTestLoop.' + paramName)

    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(fixationBackground)
    fixationComponents.append(fixationCross)
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *fixationBackground* updates
        if t >= 0.0 and fixationBackground.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationBackground.tStart = t  # underestimates by a little under one frame
            fixationBackground.frameNStart = frameN  # exact frame index
            fixationBackground.setAutoDraw(True)
        elif fixationBackground.status == STARTED and t >= (0.0 + .5):
            fixationBackground.setAutoDraw(False)

        # *fixationCross* updates
        if t >= 0.0 and fixationCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross.tStart = t  # underestimates by a little under one frame
            fixationCross.frameNStart = frameN  # exact frame index
            fixationCross.setAutoDraw(True)
        elif fixationCross.status == STARTED and t >= (0.0 + .5):
            fixationCross.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "studyTrial"-------
    t = 0
    studyTrialClock.reset()  # clock
    frameN = -1
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    studyFaceTop.setImage(os.path.join('top', studyTopFaces))
    studyFaceBottom.setImage(os.path.join('bottom', studyBottomFaces))
    # keep track of which components have finished
    studyTrialComponents = []
    studyTrialComponents.append(studyFaceTop)
    studyTrialComponents.append(studyFaceBottom)
    studyTrialComponents.append(topOval)
    studyTrialComponents.append(botOval)
    for thisComponent in studyTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "studyTrial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = studyTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *studyFaceTop* updates
        if t >= 0.0 and studyFaceTop.status == NOT_STARTED:
            # keep track of start time/frame for later
            studyFaceTop.tStart = t  # underestimates by a little under one frame
            studyFaceTop.frameNStart = frameN  # exact frame index
            studyFaceTop.setAutoDraw(True)
        elif studyFaceTop.status == STARTED and t >= (0.0 + .4):
            studyFaceTop.setAutoDraw(False)

        # *studyFaceBottom* updates
        if t >= 0.0 and studyFaceBottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            studyFaceBottom.tStart = t  # underestimates by a little under one frame
            studyFaceBottom.frameNStart = frameN  # exact frame index
            studyFaceBottom.setAutoDraw(True)
        elif studyFaceBottom.status == STARTED and t >= (0.0 + .4):
            studyFaceBottom.setAutoDraw(False)

        # *topOval* updates
        if t >= 0.0 and topOval.status == NOT_STARTED:
            # keep track of start time/frame for later
            topOval.tStart = t  # underestimates by a little under one frame
            topOval.frameNStart = frameN  # exact frame index
            topOval.setAutoDraw(True)
        elif topOval.status == STARTED and t >= (0.0 + .4):
            topOval.setAutoDraw(False)

        # *botOval* updates
        if t >= 0.0 and botOval.status == NOT_STARTED:
            # keep track of start time/frame for later
            botOval.tStart = t  # underestimates by a little under one frame
            botOval.frameNStart = frameN  # exact frame index
            botOval.setAutoDraw(True)
        elif botOval.status == STARTED and t >= (0.0 + .4):
            botOval.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in studyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "studyTrial"-------
    for thisComponent in studyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "maskTrial"-------
    t = 0
    maskTrialClock.reset()  # clock
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskTrialComponents = []
    maskTrialComponents.append(mask)
    for thisComponent in maskTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "maskTrial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *mask* updates
        if t >= 0.0 and mask.status == NOT_STARTED:
            # keep track of start time/frame for later
            mask.tStart = t  # underestimates by a little under one frame
            mask.frameNStart = frameN  # exact frame index
            mask.setAutoDraw(True)
        elif mask.status == STARTED and t >= (0.0 + 2.0):
            mask.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "maskTrial"-------
    for thisComponent in maskTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "testTrial"-------
    t = 0
    testTrialClock.reset()  # clock
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    topTest.setPos([xPosTop,yPosTop])
    topTest.setImage(os.path.join('top',testTopFaces))
    topOvalTest.setPos([xPosTop, yPosTop])
    bottomTest.setPos([xPosBot,yPosBot])
    bottomTest.setImage(os.path.join('bottom',testBottomFaces))
    botOvalTest.setPos([xPosBot, yPosBot])
    cue1top.setOpacity(cueTop)
    cue1top.setPos([xPosTop,yPosTop+34])
    cue1bottom.setOpacity(cueBot)
    cue1bottom.setPos([xPosBot,yPosBot-32])
    cue1response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    cue1response.status = NOT_STARTED
    # keep track of which components have finished
    testTrialComponents = []
    if xPosTop == 32:
        background = backgroundMisaligned
        strip = backgroundStripeMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    elif xPosTop == 64:
        background = backgroundVeryMisaligned
        strip = backgroundStripeVeryMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    else:
        background = fixationBackground
        strip = backgroundStripe
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    testTrialComponents.append(topTest)
    testTrialComponents.append(topOvalTest)
    testTrialComponents.append(bottomTest)
    testTrialComponents.append(botOvalTest)
    testTrialComponents.append(cue1top)
    testTrialComponents.append(cue1bottom)
    testTrialComponents.append(cue1response)
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "testTrial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *topTest* updates
        if t >= 0.0 and topTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            topTest.tStart = t  # underestimates by a little under one frame
            topTest.frameNStart = frameN  # exact frame index
            topTest.setAutoDraw(True)
            background.setAutoDraw(True)
            strip.setAutoDraw(True)
        elif topTest.status == STARTED and t >= (0.0 + 2.5):
            topTest.setAutoDraw(False)
            background.setAutoDraw(False)
            strip.setAutoDraw(False)

        # *topOvalTest* updates
        if t >= 0.0 and topOvalTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            topOvalTest.tStart = t  # underestimates by a little under one frame
            topOvalTest.frameNStart = frameN  # exact frame index
            topOvalTest.setAutoDraw(True)
        elif topOvalTest.status == STARTED and t >= (0.0 + 2.5):
            topOvalTest.setAutoDraw(False)

        # *bottomTest* updates
        if t >= 0.0 and bottomTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottomTest.tStart = t  # underestimates by a little under one frame
            bottomTest.frameNStart = frameN  # exact frame index
            bottomTest.setAutoDraw(True)
        elif bottomTest.status == STARTED and t >= (0.0 + 2.5):
            bottomTest.setAutoDraw(False)

        # *botOvalTest* updates
        if t >= 0.0 and botOvalTest.status == NOT_STARTED:
            # keep track of start time/frame for later
            botOvalTest.tStart = t  # underestimates by a little under one frame
            botOvalTest.frameNStart = frameN  # exact frame index
            botOvalTest.setAutoDraw(True)
        elif botOvalTest.status == STARTED and t >= (0.0 + 2.5):
            botOvalTest.setAutoDraw(False)

        # *cue1top* updates
        if t >= 0.0 and cue1top.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue1top.tStart = t  # underestimates by a little under one frame
            cue1top.frameNStart = frameN  # exact frame index
            cue1top.setAutoDraw(True)
        elif cue1top.status == STARTED and t >= (0.0 + 2.5):
            cue1top.setAutoDraw(False)

        # *cue1bottom* updates
        if t >= 0.0 and cue1bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue1bottom.tStart = t  # underestimates by a little under one frame
            cue1bottom.frameNStart = frameN  # exact frame index
            cue1bottom.setAutoDraw(True)
        elif cue1bottom.status == STARTED and t >= (0.0 + 2.5):
            cue1bottom.setAutoDraw(False)

        # *cue1response* updates
        if t >= 0.0 and cue1response.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue1response.tStart = t  # underestimates by a little under one frame
            cue1response.frameNStart = frameN  # exact frame index
            cue1response.status = STARTED
            # keyboard checking is just starting
            cue1response.clock.reset()  # now t=0
            event.clearEvents()
        elif cue1response.status == STARTED and t >= (0.0 + 2.5):
            cue1response.status = STOPPED
        if cue1response.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'k'])
            if len(theseKeys) > 0:  # at least one key was pressed
                cue1response.keys = theseKeys[-1]  # just the last key pressed
                cue1response.rt = cue1response.clock.getTime()
                # was this 'correct'?
                if (cue1response.keys == str(corAnsOne)): cue1response.corr = 1
                else: cue1response.corr=0
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "testTrial"-------
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(cue1response.keys) == 0:  # No response was made
       cue1response.keys=None
       # was no response the correct answer?!
       if str(corAnsOne).lower() == 'none': cue1response.corr = 1  # correct non-response
       else: cue1response.corr = 0  # failed to respond (incorrectly)
    # store data for practiceLoop (TrialHandler)
    practiceLoop.addData('cue1response.keys',cue1response.keys)
    practiceLoop.addData('cue1response.corr', cue1response.corr)
    if cue1response.keys != None:  # we had a response
        practiceLoop.addData('cue1response.rt', cue1response.rt)

    #------Prepare to start Routine "testTrial2"-------
    t = 0
    testTrial2Clock.reset()  # clock
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    topTest2.setPos([xPosTop,yPosTop])
    topTest2.setImage(os.path.join('top',testTopFaces))
    topOvalTest2.setPos([xPosTop, yPosTop])
    bottomTest2.setPos([xPosBot,yPosBot])
    bottomTest2.setImage(os.path.join('bottom',testBottomFaces))
    botOvalTest2.setPos([xPosBot, yPosBot])
    cue2top.setOpacity(1-cueTop)
    cue2top.setPos([xPosTop,yPosTop+34])
    cue2bottom.setOpacity(1-cueBot)
    cue2bottom.setPos([xPosBot,yPosBot-32])
    cue2response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    cue2response.status = NOT_STARTED
    # keep track of which components have finished
    testTrialComponents = []
    if xPosTop == 32:
        background = backgroundMisaligned
        strip = backgroundStripeMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    elif xPosTop == 64:
        background = backgroundVeryMisaligned
        strip = backgroundStripeVeryMisaligned
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    else:
        background = fixationBackground
        strip = backgroundStripe
        testTrialComponents.append(background)
        testTrialComponents.append(strip)
    testTrialComponents.append(topTest2)
    testTrialComponents.append(topOvalTest2)
    testTrialComponents.append(bottomTest2)
    testTrialComponents.append(botOvalTest2)
    testTrialComponents.append(cue2top)
    testTrialComponents.append(cue2bottom)
    testTrialComponents.append(cue2response)
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "testTrial2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testTrial2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *topTest2* updates
        if t >= 0.0 and topTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            topTest2.tStart = t  # underestimates by a little under one frame
            topTest2.frameNStart = frameN  # exact frame index
            topTest2.setAutoDraw(True)
            background.setAutoDraw(True)
            strip.setAutoDraw(True)
        elif topTest2.status == STARTED and t >= (0.0 + 2.5):
            topTest2.setAutoDraw(False)
            background.setAutoDraw(False)
            strip.setAutoDraw(False)

        # *topOvalTest2* updates
        if t >= 0.0 and topOvalTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            topOvalTest2.tStart = t  # underestimates by a little under one frame
            topOvalTest2.frameNStart = frameN  # exact frame index
            topOvalTest2.setAutoDraw(True)
        elif topOvalTest2.status == STARTED and t >= (0.0 + 2.5):
            topOvalTest2.setAutoDraw(False)

        # *bottomTest* updates
        if t >= 0.0 and bottomTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            bottomTest2.tStart = t  # underestimates by a little under one frame
            bottomTest2.frameNStart = frameN  # exact frame index
            bottomTest2.setAutoDraw(True)
        elif bottomTest2.status == STARTED and t >= (0.0 + 2.5):
            bottomTest2.setAutoDraw(False)

        # *botOvalTest2* updates
        if t >= 0.0 and botOvalTest2.status == NOT_STARTED:
            # keep track of start time/frame for later
            botOvalTest2.tStart = t  # underestimates by a little under one frame
            botOvalTest2.frameNStart = frameN  # exact frame index
            botOvalTest2.setAutoDraw(True)
        elif botOvalTest2.status == STARTED and t >= (0.0 + 2.5):
            botOvalTest2.setAutoDraw(False)

        # *cue2top* updates
        if t >= 0.0 and cue2top.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue2top.tStart = t  # underestimates by a little under one frame
            cue2top.frameNStart = frameN  # exact frame index
            cue2top.setAutoDraw(True)
        elif cue2top.status == STARTED and t >= (0.0 + 2.5):
            cue2top.setAutoDraw(False)

        # *cue2bottom* updates
        if t >= 0.0 and cue2bottom.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue2bottom.tStart = t  # underestimates by a little under one frame
            cue2bottom.frameNStart = frameN  # exact frame index
            cue2bottom.setAutoDraw(True)
        elif cue2bottom.status == STARTED and t >= (0.0 + 2.5):
            cue2bottom.setAutoDraw(False)

        # *cue2response* updates
        if t >= 0.0 and cue2response.status == NOT_STARTED:
            # keep track of start time/frame for later
            cue2response.tStart = t  # underestimates by a little under one frame
            cue2response.frameNStart = frameN  # exact frame index
            cue2response.status = STARTED
            # keyboard checking is just starting
            cue2response.clock.reset()  # now t=0
            event.clearEvents()
        elif cue2response.status == STARTED and t >= (0.0 + 2.5):
            cue2response.status = STOPPED
        if cue2response.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'k'])
            if len(theseKeys) > 0:  # at least one key was pressed
                cue2response.keys = theseKeys[-1]  # just the last key pressed
                cue2response.rt = cue2response.clock.getTime()
                # was this 'correct'?
                if (cue2response.keys == str(corAnsOne)): cue2response.corr = 1
                else: cue2response.corr=0
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "testTrial"-------
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(cue2response.keys) == 0:  # No response was made
       cue2response.keys=None
       # was no response the correct answer?!
       if str(corAnsOne).lower() == 'none': cue1response.corr = 1  # correct non-response
       else: cue2response.corr = 0  # failed to respond (incorrectly)
    # store data for practiceLoop (TrialHandler)
    practiceLoop.addData('cue2response.keys',cue2response.keys)
    practiceLoop.addData('cue2response.corr', cue2response.corr)
    if cue2response.keys != None:  # we had a response
        practiceLoop.addData('cue2response.rt', cue2response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'testLoop'

#collect demographics data
root = Tkinter.Tk()
root.wm_title("Demographics Survey")

#age
Tkinter.Label(root, text="Age:").grid(row=0, column=0,sticky=Tkinter.W) #.pack(anchor='w')
ageText = Tkinter.Entry(root); ageText.grid(row=0, column=0,sticky=Tkinter.E) #.pack(anchor='e')

#sex
Tkinter.Label(root, text="Sex:").grid(row=2,sticky=Tkinter.W)#pack(anchor='w')
sexVar = Tkinter.StringVar()
Tkinter.Radiobutton(root, text="Male", variable=sexVar, value='male').grid(row=3, column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Radiobutton(root, text="Female", variable=sexVar, value='female').grid(row=4,column=0,sticky=Tkinter.W)#.pack(anchor='w')

#marital status
Tkinter.Label(root, text="Marital Status:").grid(row=5,sticky=Tkinter.W)#.pack(anchor='w')
marVar = Tkinter.StringVar()
Tkinter.Radiobutton(root, text="Single", variable=marVar, value='single').grid(row=6,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Radiobutton(root, text="Not married, living with partner", variable=marVar, value='nmlvp').grid(row=7,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Radiobutton(root, text="Married", variable=marVar, value='married').grid(row=8,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Radiobutton(root, text="Widowed", variable=marVar, value='widowed').grid(row=9,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Radiobutton(root, text="Separated/divorced", variable=marVar, value='sep/div').grid(row=10,column=0,sticky=Tkinter.W)#.pack(anchor='w')

#race/ethnicity
Tkinter.Label(root, text="Race/Ethnicity").grid(row=10,column=0,sticky=Tkinter.W)#.pack(anchor='w')
aVar = Tkinter.IntVar(); hVar = Tkinter.IntVar(); wVar = Tkinter.IntVar()
bVar = Tkinter.IntVar(); pVar = Tkinter.IntVar(); oVar = Tkinter.IntVar()
Tkinter.Checkbutton(root, text="Asian", variable=aVar).grid(row=11,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Checkbutton(root, text="Hispanic", variable=hVar).grid(row=12,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Checkbutton(root, text="White/Caucasian", variable=wVar).grid(row=13,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Checkbutton(root, text="Black/African American", variable=bVar).grid(row=14,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Checkbutton(root, text="Pacific Islander", variable=pVar).grid(row=15,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Checkbutton(root, text="Other:", variable=oVar).grid(row=16,column=0,sticky=Tkinter.W)#.pack(anchor='w')
otherEth = Tkinter.Entry(root); otherEth.grid(row=16,column=0,sticky=Tkinter.E)#.pack(anchor='e')

#spacing
Tkinter.Label(root, text="    ").grid(row=0,column=1)

#highest level of education
Tkinter.Label(root, text="Highest Level of Education:").grid(row=0,column=2,sticky=Tkinter.W)#.pack(anchor='w')
eduVar = Tkinter.StringVar()
Tkinter.Radiobutton(root, text="Grade school (grades 1-6)", variable=eduVar, value="grade school").grid(row=1,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Middle school (grades 7-9)", variable=eduVar, value="middle school").grid(row=2,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="High school (grades 10-12)", variable=eduVar, value="high school").grid(row=3,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Vocational education", variable=eduVar, value="vocational education").grid(row=4,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Some college clases", variable=eduVar, value="some college").grid(row=5,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="College degree", variable=eduVar, value="college degree").grid(row=6,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Post college professional degree", variable=eduVar, value="post-coll prof deg").grid(row=7,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Graduate, medical, or law degree", variable=eduVar, value="grad degree").grid(row=8,column=2,sticky=Tkinter.W)#pack(anchor='w')

#Employment Status
Tkinter.Label(root, text="Employment Status:").grid(row=17,column=0,sticky=Tkinter.W)#pack(anchor='w')
empVar = Tkinter.StringVar()
Tkinter.Radiobutton(root, text="Student", variable=empVar, value="student").grid(row=18,column=0,sticky=Tkinter.W)#.pack(anchor='w')
Tkinter.Radiobutton(root, text="Retired/unemployed", variable=empVar, value="retired/unemployed").grid(row=19,column=0,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Part-time", variable=empVar, value="part-time").grid(row=20,column=0,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Full-time", variable=empVar, value="full-time").grid(row=21,column=0,sticky=Tkinter.W)#pack(anchor='w')

#Household income
Tkinter.Label(root, text="Household Income:").grid(row=9,column=2,sticky=Tkinter.W)#pack(anchor='w')
hhiVar = Tkinter.StringVar()
Tkinter.Radiobutton(root, text="Less than $7,500", variable=hhiVar, value="<7500").grid(row=10,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="$7,500 - $14,999", variable=hhiVar, value="7500-14999").grid(row=11,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="$15,000 - $24,999", variable=hhiVar, value="15000-24999").grid(row=12,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="$25,000 - $39,999", variable=hhiVar, value="25000-39999").grid(row=13,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="$40,000 - $74,999", variable=hhiVar, value="40000-74999").grid(row=14,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="$75,000 - $99,999", variable=hhiVar, value="75000-99999").grid(row=15,column=2,sticky=Tkinter.W)#pack(anchor='w')
Tkinter.Radiobutton(root, text="Over $100,000", variable=hhiVar, value=">100000").grid(row=16,column=2,sticky=Tkinter.W)#pack(anchor='w')

def submitCallback():
    print "saving data..."
    dataFile.write("------------\n") #separator
    print "Age:", ageText.get()
    dataFile.write("Age:," + ageText.get() + "\n")
    print "Sex:", sexVar.get()
    dataFile.write("Sex:," + sexVar.get() + "\n")
    print "Marital status:", marVar.get()
    dataFile.write("Marital Status:," + marVar.get() + "\n")
    print "Race/ethnicity:",
    dataFile.write("Race/ethnicity:,")
    if aVar.get() != 0:
        print "asian",
        dataFile.write("asian,")
    if hVar.get() != 0:
        print "hispanic/latino",
        dataFile.write("hispanic/latino,")
    if wVar.get() != 0:
        print "white/caucasian",
        dataFile.write("white/caucasian,")
    if bVar.get() != 0:
        print "black/african american",
        dataFile.write("black/african american,")
    if pVar.get() != 0:
        print "pacific islander",
        dataFile.write("pacific islander,")
    if oVar.get() != 0:
        print "other:", otherEth.get(),
        dataFile.write("other:" + otherEth.get() + ",\n")
    print ""
    print "Highest level of education:", eduVar.get()
    dataFile.write("Highest level of education:," + eduVar.get() + "\n")
    print "Employment status:", empVar.get()
    dataFile.write("Employment status:," + empVar.get() + "\n")
    print "Household income:", hhiVar.get()
    dataFile.write("Household income:," + hhiVar.get() + "\n")
    #close logging file and program
    root.quit()
    dataFile.close()
    #window.close()
    core.quit()

Tkinter.Button(root, text="Submit", command=submitCallback).grid(row=22,column=1,sticky=Tkinter.W)#pack()

win.close()
core.quit()