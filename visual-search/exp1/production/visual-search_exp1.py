﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Wed 30 Jun 2021 01:16:04 PM EDT
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

import psychopy


class DrawHexGrid:
    '''
    Formula for calculating coordinates:
    xx = x + (d * cos(alpha))
    yy = y + (d * sin(alpha))
    '''
    def __init__(self, top_left_origin, edge_length = 100, x_count = 5, y_count = 5):
        self.top_left_origin = top_left_origin
        self.edge_length = edge_length
        self. x_count = x_count
        self.y_count = y_count
        self.point_list = ['top_left', 'bottom_left', 'bottom', 'bottom_right', 'top_right', 'top']
        self.point_dictionary = {
'top_left': '[start_coord[0], start_coord[1] - self.edge_length]',
'bottom_left': '[start_coord[0] + self.edge_length * cos(120), start_coord[1] - self.edge_length * sin(120)]',
'bottom': '[start_coord[0] + self.edge_length * cos(120), start_coord[1] + self.edge_length * sin(120)]',
'bottom_right': '[start_coord[0], start_coord[1] + self.edge_length]',
'top_right': '[start_coord[0] - self.edge_length * cos(120), start_coord[1] + self.edge_length * sin(120)]',
'top': '[start_coord[0] - self.edge_length * cos(120), start_coord[1] - self.edge_length * sin(120)]'
}
        
    def make_grid(self):
        for row in range(self.y_count):
            for col in range(self.x_count):
                ## if it's the first hex
                if not row and not col:
                    self._draw_hex('top_left', 'top_left', self.top_left_origin)
                    self.first_row_start_coord = self._coord_calculator(self.top_left_origin, 'top_left', 2)
                    self.new_hex_start_coord = self._coord_calculator(self.top_left_origin, 'top_left', 3)
                
                ## if it's the first row
                elif not row:
                    self._draw_hex('bottom_left', 'top_left', self.new_hex_start_coord)
                    self.new_hex_start_coord = self._coord_calculator(self.new_hex_start_coord, 'bottom_left', 2)
                    
                ## if it's the first column
                elif not col:
                    
                    ## conditional to account for the staggered pattern
                    if not row % 2:
                    ## if even
                        start_pos = 'top'
                        new_hex_n_turns = 4
                        first_row_n_turns = 3
                        
                    else:
                    ## if odd
                        start_pos = 'top_left'
                        new_hex_n_turns = 3
                        first_row_n_turns = 1
                        
                    self._draw_hex(start_pos, 'top_right', self.first_row_start_coord)
                    self.new_hex_start_coord = self._coord_calculator(self.first_row_start_coord, start_pos, new_hex_n_turns)
                    self.first_row_start_coord = self._coord_calculator(self.first_row_start_coord, start_pos, first_row_n_turns)
                    
                ## for all internal hex's
                else:
                    ## catch the last hex on odd rows
                    if col == self.x_count - 1 and row % 2:
                        end_pos = 'top'
                    else:
                        end_pos = 'top_right'

                    self._draw_hex('bottom_left', end_pos, self.new_hex_start_coord)
                    self.new_hex_start_coord = self._coord_calculator(self.new_hex_start_coord, 'bottom_left', 2)


                    
    def _coord_calculator(self, start_coord, start_pos, n_turns):
        ## takes in a starting coordinate, starting pos, and number of calcs to do
        ## returns ending coord as [x, y]
        ## this function will fail if you try to turn past top left, which i dont think ill need to do
        
        ## calc a slice out of point_list to iterate over what's appropriate
        new_point_list = self._rearrange_point_list(start_pos)
        
        for pos in new_point_list[:n_turns]:
            start_coord = eval(self.point_dictionary[pos])
        
        return start_coord
            
            
    
    def _draw_hex(self, start_pos, end_pos, start_coord):
        ## draws a line from start_pos to end_pos

        new_point_list = self._rearrange_point_list(start_pos)

        for position in new_point_list:
            if start_pos != end_pos and position == end_pos:
                break
            
            line = self._define_line_type()
            line.start = start_coord
            line.end = eval(self.point_dictionary[position])
            start_coord= line.end
            line.draw()

    def _rearrange_point_list(self, start_pos):
        ## outputs a list where the first element is start_pos and the last element is the one before start_pos in point_list

        if start_pos == 'top_left':
            return self.point_list

        return self.point_list[self.point_list.index(start_pos):] + self.point_list[:self.point_list.index(start_pos)-1]

    def _define_line_type(self):
        return psychopy.visual.Line(
            win = win,
            units='pix',
            lineColor=[-1, -1, -1]
            )



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'visual-search_exp1'  # from the Builder filename that created this script
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
    originPath='visual-search_exp1.py',
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

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
trial1Components = [key_resp_2]
for thisComponent in trial1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial1"-------
while continueRoutine:
    # get current time
    t = trial1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    dhg = DrawHexGrid([-400, 400])
    
    dhg.make_grid()
    
    
    
    
    
    
    
    
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
        theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
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
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial1"-------
for thisComponent in trial1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "trial1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
