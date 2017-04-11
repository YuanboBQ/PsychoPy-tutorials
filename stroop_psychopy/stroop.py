# -*- coding: utf-8 -*-
'''
stroop
xxxxx

2016-07-20
writed by leosun
'''
#load the modules used in this exp.
from psychopy import core, visual, gui, data, event, gamma, monitors, sound
from psychopy.tools.filetools import fromFile, toFile
from scipy.io import matlab
import time, os, math, csv

try: expInfo = fromFile('stropp_LastParams.pickle')#try to get a previous parameters file    
except: expInfo = {'observer':'01_syl', 'gender':['m','f'],'age':30}#if not there then use a default set        
dateStr = time.strftime("_20%y_%m_%d_%H%M", time.localtime())#add the current time

#present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='Stroop', order=['observer','gender','age'])
if dlg.OK: toFile('stroop_LastParams.pickle', expInfo)#save params to file for next time
else: core.quit()#the user hit cancel so exit

#create the subject datafile
new_path = os.path.join(os.getcwd()+'/data/', expInfo['observer']+'_'+expInfo['gender']+str(expInfo['age']))
if not os.path.isdir(new_path): os.makedirs(new_path)

#create the formal experiment condition list
stimList = []
for word in ['R','G']:
    for color in ['red','green']:
        stimList.append( {'word':word,'color':color} )

#organise them with the trial handler
trials = data.TrialHandler(stimList, 10, method='random')#create the within-block random sequence
trials.data.addDataType( ['RT', 'accuracy'] )

#load the material
fn = os.getcwd()+'/material'

#define the parameters of stimuli
fixSize = 40 
monitorSize = (1024, 768)
center =  (0.0, 0.0) # the centers of the windows

#define the duration of stimuli
frameRate = 100
frameDura = 1000/frameRate
fixDura = 500
rpDura = 1500
itiDura = 1000
frames4Fix = round(fixDura/frameDura)
frames4RP = round(rpDura/frameDura)
frames4ITI = round(itiDura/frameDura)

# Create a window to draw
myWin = visual.Window(monitorSize, color=(128, 128,128), fullscr=False, units='pix',
                      blendMode='avg', colorSpace='rgb255')

#define lots of stimuli, make a list
intr1 = visual.ImageStim(myWin, image=fn+'/introduction1.png',size=(1024,768), pos=center, units='pix')
fix = visual.TextStim(myWin, text='+', pos=center, color='black', bold=True, height=fixSize) 
restPrompt = visual.TextStim(myWin, text=u'休息一下', color='black', pos=center, height=49)
overPrompt = visual.TextStim(myWin, text=u'实验结束，谢谢！', color='black', pos=center, height=49)

beep = sound.Sound(value=2000,secs=0.2,sampleRate=44100, bits=8)

#run the experiment
timer = core.Clock()
event.Mouse(visible=False)

#the formal experiment starts here
#introduction display:untill response
event.clearEvents()
while True:
    intr1.draw()
    myWin.flip()        
    if len(event.getKeys()) > 0: break     

#the loop starts here
for thisTrial in trials: 
    #decide which word
    if thisTrial['word']=='R': textWord = u'红'
    elif thisTrial['word']=='G': textWord = u'绿'
   
    stimu = visual.TextStim(myWin, text=textWord, color=thisTrial['color'], pos=center, height=30)
    
    ###fixation display: 500ms
    event.clearEvents() 
    for frameN in range(int(frames4Fix)):#fixation loops start here
        fix.draw()
        flip_time0 = myWin.flip()        
    
    ###text+response display:1500 ms or untill response
    event.clearEvents()    
    isRunning = 0
    overRT = 0    
    for frameN in range(int(frames4RP)):#Response loops start here 
        stimu.draw()
        flip_time1 = myWin.flip()
        
        trials.data.add('RT', 0)
        for key in event.getKeys(): #check the keyboard events           
            #record the response time
            if key in ['left','right']:
                RT = round((flip_time1-flip_time0)*1000)
                trials.data.add('RT', RT)
                overRT = 1
                break            
            if key in ['q','escape']: isRunning = 1;break            
        if overRT==1 or isRunning==1:break
    if isRunning==1:
        myWin.close()             
    if overRT==1:
        #record the accuray
        if (key=='left' and thisTrial['color']=='red') or \
           (key=='right' and thisTrial['color']=='green') :
              trials.data.add('accuracy', 1) 
        else: 
            trials.data.add('accuracy', -1) 
            beep.play()
            core.wait(0.5)
else:
		    trials.data.add('accuracy', -1)
		    beep.play()
            core.wait(0.5)           
        
    ###ITI display
    for frameN in range(int(frames4ITI)):#ITI loops starts here
        myWin.flip()  
    
    ###rest prompt display
    event.clearEvents()
    if trials.thisN+1==40:
        while True:             
            overPrompt.draw()
            myWin.flip()
            if len(event.getKeys()) > 0: break
    elif (trials.thisN+1)%20==0:
        while True:             
            restPrompt.draw()
            myWin.flip()
            if len(event.getKeys()) > 0: break
            
#save and analysis the data after the experiment
dataFN = new_path+'/'+expInfo['observer']+dateStr
fnn=dataFN+'.csv'
df = trials.saveAsWideText(fnn) #wide is useful for analysis with R or SPSS. Also returns dataframe df
myWin.close()
 
