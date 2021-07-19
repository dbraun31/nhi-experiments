#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mon 19 Jul 2021 12:56:21 PM EDT
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'compare_lines'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='compare_lines_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "GlobalDefs"
GlobalDefsClock = core.Clock()
import psychopy
import time
import random
import itertools

def determine_diagonal(start_coord_left_line, length, x_direction, y_direction):
    x_shift = 1 if x_direction == 'right' else -1
    y_shift = 1 if y_direction == 'up' else -1
    
    start_x = start_coord_left_line[0]
    start_y = start_coord_left_line[1]
    end_coord_left_line_x = start_x + x_shift* (length * cos(1.0472))
    end_coord_left_line_y = start_y + y_shift* (length * sin(1.0472))
    
    return (end_coord_left_line_x, end_coord_left_line_y)


def draw_line(start_coord, end_coord, width):

    line = psychopy.visual.Line(
    win = win,
    units='pix',
    lineColor='black',
    lineWidth = width
    )

    line.start = start_coord
    line.end = end_coord
    line.draw()
    
    
def refresh_width_combinations(n_lines, max_width):
    total_widths = np.linspace(1, max_width, n_lines)
    combinations = list(itertools.combinations(total_widths, 2))
    combinations += [(x, x) for x in total_widths]
    
    return combinations
    
    
    
    
    
    
from math import *

'''
Formula for calculating coordinates:
xx = x + (d * cos(alpha))
yy = y + (d * sin(alpha))
'''
## GLOBAL LINE PARAMETERS
length = 300
starting_point_left_x = -300
distance_between_lines = 600
## horizontal lines always zero
starting_point_y = length / 2

## LINE WIDTH ARRAY PARAMETERS
max_width = 4
n_lines = 20

## VERTICAL LINES
vertical_starting_point_line1 = (starting_point_left_x, starting_point_y)
vertical_ending_point_line1 = (starting_point_left_x, starting_point_y - length)
vertical_starting_point_line2 = (starting_point_left_x + distance_between_lines, starting_point_y)
vertical_ending_point_line2 = (starting_point_left_x + distance_between_lines, starting_point_y - length)

## HORIZONTAL LINES
horizontal_starting_point_line1 = (starting_point_left_x - (length / 2), 0) 
horizontal_ending_point_line1 = (starting_point_left_x + (length / 2), 0)
horizontal_starting_point_line2 = (horizontal_starting_point_line1[0] + distance_between_lines, 0)
horizontal_ending_point_line2  = (horizontal_ending_point_line1[0] + distance_between_lines, 0)

## DIAGONAL LINES
## forward slash (ie starts at top and goes forward)
forward_starting_point_line1 = determine_diagonal((starting_point_left_x, 0), length/2, x_direction = 'left', y_direction = 'up')
forward_ending_point_line1 = determine_diagonal((starting_point_left_x, 0), length/2, x_direction = 'right', y_direction = 'down')
forward_starting_point_line2 = (forward_starting_point_line1[0] + distance_between_lines, forward_starting_point_line1[1])
forward_ending_point_line2 = (forward_ending_point_line1[0] + distance_between_lines, forward_ending_point_line1[1])

## backward slash (ie starts at top and goes back)
backward_starting_point_line1 = determine_diagonal((starting_point_left_x, 0), length/2, x_direction = 'right', y_direction = 'up')
backward_ending_point_line1 = determine_diagonal((starting_point_left_x, 0), length/2, x_direction = 'left', y_direction = 'down')
backward_starting_point_line2 = (backward_starting_point_line1[0] + distance_between_lines, backward_starting_point_line1[1])
backward_ending_point_line2 = (backward_ending_point_line1[0] + distance_between_lines, backward_ending_point_line1[1])



RotationCondition = {
'vertical': [[vertical_starting_point_line1, vertical_ending_point_line1], 
[vertical_starting_point_line2, vertical_ending_point_line2]],

'horizontal': [[horizontal_starting_point_line1, horizontal_ending_point_line1], 
[horizontal_starting_point_line2, horizontal_ending_point_line2]],

'diagonal1': [[forward_starting_point_line1, forward_ending_point_line1], [forward_starting_point_line2, forward_ending_point_line2]],
'diagonal2': [[backward_starting_point_line1, backward_ending_point_line1], [backward_starting_point_line2, backward_ending_point_line2]]
}




    
if np.random.uniform() > .5:
    first_block = 'sequential'
    second_block= 'simultaneous'
else:
    first_block = 'simultaneous'
    second_block = 'sequential'
    
block_count = 0

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionText = visual.TextStim(win=win, name='InstructionText',
    text='In this pilot experiment, you will see two lines appear on the screen either simultaneously, or one after another. You need to judge the width of the lines and decide whether the line presented to left is larger (press the left arrow key), the line presented to the right is larger (press the right arrow key), or whether the lines are equal (press the down arrow key). \n\nYou will see the lines for a total of 2 seconds (1 second each if they appear one after another), and you will have an unlimited amount of time to respond. You should try to respond as quickly and as accurately as possible. When both lines are presented simultaneously, you can respond as soon as the lines appear. If the lines are presented one after another, you can respond as soon as you see the second line.\n\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstructionResponse = keyboard.Keyboard()

# Initialize components for Routine "StartBlock"
StartBlockClock = core.Clock()
BlockText = visual.TextStim(win=win, name='BlockText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()



ISITimer = visual.TextStim(win=win, name='ISITimer',
    text='',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sequential_line1"
sequential_line1Clock = core.Clock()
FirstLineTimer = visual.TextStim(win=win, name='FirstLineTimer',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "sequential_gap"
sequential_gapClock = core.Clock()
GapTimer = visual.TextStim(win=win, name='GapTimer',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "sequential_line2"
sequential_line2Clock = core.Clock()
SeqResponse = keyboard.Keyboard()

# Initialize components for Routine "simultaneous"
simultaneousClock = core.Clock()
ResponseSimul = keyboard.Keyboard()

# Initialize components for Routine "save_data"
save_dataClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "GlobalDefs"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GlobalDefsComponents = []
for thisComponent in GlobalDefsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GlobalDefsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GlobalDefs"-------
while continueRoutine:
    # get current time
    t = GlobalDefsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GlobalDefsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GlobalDefsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GlobalDefs"-------
for thisComponent in GlobalDefsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "GlobalDefs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
InstructionResponse.keys = []
InstructionResponse.rt = []
_InstructionResponse_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionText, InstructionResponse]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionText* updates
    if InstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionText.frameNStart = frameN  # exact frame index
        InstructionText.tStart = t  # local t and not account for scr refresh
        InstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionText, 'tStartRefresh')  # time at next scr refresh
        InstructionText.setAutoDraw(True)
    
    # *InstructionResponse* updates
    waitOnFlip = False
    if InstructionResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionResponse.frameNStart = frameN  # exact frame index
        InstructionResponse.tStart = t  # local t and not account for scr refresh
        InstructionResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionResponse, 'tStartRefresh')  # time at next scr refresh
        InstructionResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstructionResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstructionResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstructionResponse.status == STARTED and not waitOnFlip:
        theseKeys = InstructionResponse.getKeys(keyList=['space'], waitRelease=False)
        _InstructionResponse_allKeys.extend(theseKeys)
        if len(_InstructionResponse_allKeys):
            InstructionResponse.keys = _InstructionResponse_allKeys[-1].name  # just the last key pressed
            InstructionResponse.rt = _InstructionResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionText.started', InstructionText.tStartRefresh)
thisExp.addData('InstructionText.stopped', InstructionText.tStopRefresh)
# check responses
if InstructionResponse.keys in ['', [], None]:  # No response was made
    InstructionResponse.keys = None
thisExp.addData('InstructionResponse.keys',InstructionResponse.keys)
if InstructionResponse.keys != None:  # we had a response
    thisExp.addData('InstructionResponse.rt', InstructionResponse.rt)
thisExp.addData('InstructionResponse.started', InstructionResponse.tStartRefresh)
thisExp.addData('InstructionResponse.stopped', InstructionResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "StartBlock"-------
    continueRoutine = True
    # update component parameters for each repeat
    ## update block count
    block_count += 1
    trial_count = 0
    
    if block_count == 1:
        current_block = first_block
    else:
        current_block = second_block
        
    ## fill width array
    line_widths = refresh_width_combinations(n_lines, max_width)
    BlockText.setText('You are about to start block ' + str(block_count) + ' of 2.\nEach block has 280 trials. Youll see a trial update after every 50 trials to help keep you sane.\nPress the space bar to continue.')
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    StartBlockComponents = [BlockText, key_resp_2]
    for thisComponent in StartBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StartBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StartBlock"-------
    while continueRoutine:
        # get current time
        t = StartBlockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StartBlockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BlockText* updates
        if BlockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BlockText.frameNStart = frameN  # exact frame index
            BlockText.tStart = t  # local t and not account for scr refresh
            BlockText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BlockText, 'tStartRefresh')  # time at next scr refresh
            BlockText.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StartBlock"-------
    for thisComponent in StartBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('BlockText.started', BlockText.tStartRefresh)
    blocks.addData('BlockText.stopped', BlockText.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    blocks.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        blocks.addData('key_resp_2.rt', key_resp_2.rt)
    blocks.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    blocks.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "StartBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=70.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        trial_count += 1
        
        start_left_line = RotationCondition[line_orientation][0][0]
        end_left_line = RotationCondition[line_orientation][0][1]
        start_right_line = RotationCondition[line_orientation][1][0]
        end_right_line = RotationCondition[line_orientation][1][1]
        
        ## choose combination
        try:
            choice = random.choice(line_widths)
        except:
            line_widths = refresh_width_combinations(n_lines, max_width)
            choice = random.choice(line_widths)
        line_widths.remove(choice)
        
        flip = np.random.uniform() > .5
        if flip:
            left_width = choice[0]
            right_width = choice[1]
        else:
            left_width = choice[1]
            right_width = choice[0]
            
        
        ISITimer.setText('trial {} / {}'.format(trial_count, 70*4) if not trial_count % 50 else ''
)
        # keep track of which components have finished
        ISIComponents = [ISITimer]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISITimer* updates
            if ISITimer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISITimer.frameNStart = frameN  # exact frame index
                ISITimer.tStart = t  # local t and not account for scr refresh
                ISITimer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISITimer, 'tStartRefresh')  # time at next scr refresh
                ISITimer.setAutoDraw(True)
            if ISITimer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISITimer.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ISITimer.tStop = t  # not accounting for scr refresh
                    ISITimer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISITimer, 'tStopRefresh')  # time at next scr refresh
                    ISITimer.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('ISITimer.started', ISITimer.tStartRefresh)
        trials.addData('ISITimer.stopped', ISITimer.tStopRefresh)
        
        # ------Prepare to start Routine "sequential_line1"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        
        if np.random.uniform() > .5:
            first_line_label = 'left'
            first_line = (start_left_line, end_left_line)
            first_line_width = left_width
            second_line_label = 'right'
            second_line = (start_right_line, end_right_line)
            second_line_width = right_width
        else:
            second_line = (start_left_line, end_left_line)
            second_line_width = left_width
            second_line_label = 'left'
            first_line = (start_right_line, end_right_line)
            first_line_width = right_width
            first_line_label = 'right'
        
        
        FirstLineTimer.setText('')
        if current_block == 'simultaneous':
            continueRoutine = False
        from datetime import datetime
        
        start = datetime.now()
        # keep track of which components have finished
        sequential_line1Components = [FirstLineTimer]
        for thisComponent in sequential_line1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sequential_line1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "sequential_line1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = sequential_line1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sequential_line1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            draw_line(first_line[0], first_line[1], first_line_width)
            
            
            # *FirstLineTimer* updates
            if FirstLineTimer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FirstLineTimer.frameNStart = frameN  # exact frame index
                FirstLineTimer.tStart = t  # local t and not account for scr refresh
                FirstLineTimer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FirstLineTimer, 'tStartRefresh')  # time at next scr refresh
                FirstLineTimer.setAutoDraw(True)
            if FirstLineTimer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FirstLineTimer.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FirstLineTimer.tStop = t  # not accounting for scr refresh
                    FirstLineTimer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FirstLineTimer, 'tStopRefresh')  # time at next scr refresh
                    FirstLineTimer.setAutoDraw(False)
            if (start - datetime.now()).total_seconds() >= 1:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sequential_line1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sequential_line1"-------
        for thisComponent in sequential_line1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('FirstLineTimer.started', FirstLineTimer.tStartRefresh)
        trials.addData('FirstLineTimer.stopped', FirstLineTimer.tStopRefresh)
        
        # ------Prepare to start Routine "sequential_gap"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if current_block == 'simultaneous':
            continueRoutine = False
        # keep track of which components have finished
        sequential_gapComponents = [GapTimer]
        for thisComponent in sequential_gapComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sequential_gapClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "sequential_gap"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = sequential_gapClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sequential_gapClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *GapTimer* updates
            if GapTimer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                GapTimer.frameNStart = frameN  # exact frame index
                GapTimer.tStart = t  # local t and not account for scr refresh
                GapTimer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GapTimer, 'tStartRefresh')  # time at next scr refresh
                GapTimer.setAutoDraw(True)
            if GapTimer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GapTimer.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    GapTimer.tStop = t  # not accounting for scr refresh
                    GapTimer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GapTimer, 'tStopRefresh')  # time at next scr refresh
                    GapTimer.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sequential_gapComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sequential_gap"-------
        for thisComponent in sequential_gapComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('GapTimer.started', GapTimer.tStartRefresh)
        trials.addData('GapTimer.stopped', GapTimer.tStopRefresh)
        
        # ------Prepare to start Routine "sequential_line2"-------
        continueRoutine = True
        # update component parameters for each repeat
        if current_block == 'simultaneous':
            continueRoutine = False
        SeqResponse.keys = []
        SeqResponse.rt = []
        _SeqResponse_allKeys = []
        # keep track of which components have finished
        sequential_line2Components = [SeqResponse]
        for thisComponent in sequential_line2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sequential_line2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "sequential_line2"-------
        while continueRoutine:
            # get current time
            t = sequential_line2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sequential_line2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if t <= 1.0:
                draw_line(second_line[0], second_line[1], second_line_width)
            
                
            
            
            
            
            # *SeqResponse* updates
            waitOnFlip = False
            if SeqResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SeqResponse.frameNStart = frameN  # exact frame index
                SeqResponse.tStart = t  # local t and not account for scr refresh
                SeqResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SeqResponse, 'tStartRefresh')  # time at next scr refresh
                SeqResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(SeqResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(SeqResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if SeqResponse.status == STARTED and not waitOnFlip:
                theseKeys = SeqResponse.getKeys(keyList=['left', 'right', 'down'], waitRelease=False)
                _SeqResponse_allKeys.extend(theseKeys)
                if len(_SeqResponse_allKeys):
                    SeqResponse.keys = _SeqResponse_allKeys[-1].name  # just the last key pressed
                    SeqResponse.rt = _SeqResponse_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sequential_line2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sequential_line2"-------
        for thisComponent in sequential_line2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if SeqResponse.keys in ['', [], None]:  # No response was made
            SeqResponse.keys = None
        trials.addData('SeqResponse.keys',SeqResponse.keys)
        if SeqResponse.keys != None:  # we had a response
            trials.addData('SeqResponse.rt', SeqResponse.rt)
        trials.addData('SeqResponse.started', SeqResponse.tStartRefresh)
        trials.addData('SeqResponse.stopped', SeqResponse.tStopRefresh)
        # the Routine "sequential_line2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "simultaneous"-------
        continueRoutine = True
        # update component parameters for each repeat
        if current_block == 'sequential':
            continueRoutine = False
        ResponseSimul.keys = []
        ResponseSimul.rt = []
        _ResponseSimul_allKeys = []
        # keep track of which components have finished
        simultaneousComponents = [ResponseSimul]
        for thisComponent in simultaneousComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        simultaneousClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "simultaneous"-------
        while continueRoutine:
            # get current time
            t = simultaneousClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=simultaneousClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            if t <= 2.0:
                draw_line(start_left_line, end_left_line, left_width)
                draw_line(start_right_line, end_right_line, right_width)
            
            
            # *ResponseSimul* updates
            waitOnFlip = False
            if ResponseSimul.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ResponseSimul.frameNStart = frameN  # exact frame index
                ResponseSimul.tStart = t  # local t and not account for scr refresh
                ResponseSimul.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ResponseSimul, 'tStartRefresh')  # time at next scr refresh
                ResponseSimul.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ResponseSimul.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ResponseSimul.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ResponseSimul.status == STARTED and not waitOnFlip:
                theseKeys = ResponseSimul.getKeys(keyList=['left', 'right', 'down'], waitRelease=False)
                _ResponseSimul_allKeys.extend(theseKeys)
                if len(_ResponseSimul_allKeys):
                    ResponseSimul.keys = _ResponseSimul_allKeys[-1].name  # just the last key pressed
                    ResponseSimul.rt = _ResponseSimul_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in simultaneousComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "simultaneous"-------
        for thisComponent in simultaneousComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if ResponseSimul.keys in ['', [], None]:  # No response was made
            ResponseSimul.keys = None
        trials.addData('ResponseSimul.keys',ResponseSimul.keys)
        if ResponseSimul.keys != None:  # we had a response
            trials.addData('ResponseSimul.rt', ResponseSimul.rt)
        trials.addData('ResponseSimul.started', ResponseSimul.tStartRefresh)
        trials.addData('ResponseSimul.stopped', ResponseSimul.tStopRefresh)
        # the Routine "simultaneous" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "save_data"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        save_dataComponents = []
        for thisComponent in save_dataComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        save_dataClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "save_data"-------
        while continueRoutine:
            # get current time
            t = save_dataClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=save_dataClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in save_dataComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "save_data"-------
        for thisComponent in save_dataComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('left_width', left_width)
        trials.addData('right_width', right_width)
        trials.addData('global_line_length', length)
        trials.addData('global_starting_point_left_x', starting_point_left_x)
        trials.addData('global_distance_between_lines', distance_between_lines)
        
        if current_block == 'sequential':
            trials.addData('first_line_label', first_line_label)
            trials.addData('second_line_label', second_line_label)
        else:
            trials.addData('first_line_label', np.nan)
            trials.addData('second_line_label', np.nan)
        # the Routine "save_data" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 70.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'blocks'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
