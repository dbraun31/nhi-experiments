#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Fri 10 Sep 2021 10:38:28 AM EDT
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

from datetime import datetime
trial_count = 0
import copy


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
    originPath='visual-search_exp1_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.75,0.75,0.75], colorSpace='rgb',
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

# Initialize components for Routine "Prompt"
PromptClock = core.Clock()
import psychopy
## this line is essential for mapping coordinates of mouse clicks to the coordinates of rectangles
win.units = 'pix'

## print_line_widths
## ^ flag for troubleshooting



class DrawHexGrid:
    '''
    The general idea here is to think, for any given hexagon I want to draw, what position (eg, top left) in the hex am i starting at, what position do i want to finish at, and what's the starting coordinate
    Given this information, we rely on the formulas below to draw however many lines are needed to connect the starting position to the ending position
    In the process, I save out starting coordinates that will be used for the next hexagon and for the first hexagon in a new row, as well as handling some other edge case things
    
    Formula for calculating coordinates:
    xx = x + (d * cos(alpha))
    yy = y + (d * sin(alpha))
    '''
    def __init__(self, top_left_origin, edge_length = 120, x_count = 4, y_count = 4):

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
        # for creating rectangles
        self.angle_dictionary = {
        'top_left': 0,
        'bottom_left': -55,
        'bottom': 55,
        'bottom_right': 0,
        'top_right': -55,
        'top': 55
        }
        
        # for creating line ids
        self.point_to_side = {
        'top_left': 'left',
        'bottom_left': 'bottom_left',
        'bottom': 'bottom_right',
        'bottom_right': 'right',
        'top_right': 'top_right',
        'top': 'top_left'
        }
        
    def make_grid(self):
        for row in range(self.y_count):
            for col in range(self.x_count):
                self.row = row
                self.col = col
                
                ## if it's the first hex
                if not row and not col:
              
                    ## reset the line width drawer
                    self.line_width_container_draw = copy.deepcopy(line_width_container_original)
                    
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
            ## are we dealing with an exterior line?
            is_exterior = self._determine_exterior(self.row, self.col, self.x_count, self.y_count, position)
            
            line = self._define_line_type(is_exterior)
            line.start = start_coord
            line.end = eval(self.point_dictionary[position])
            line.draw()

            lines_rectangles_container.append({'line': line, 'line_id': 'r{}c{}_{}'.format(self.row, self.col, self.point_to_side[position])})
                
            self._draw_rect(start_coord, line.end, position, is_exterior)
            
            start_coord= line.end


    def _draw_rect(self, line_start, line_end, position, is_exterior = False):

        edge_length = self.edge_length
        center = [(line_end[0] + line_start[0]) / 2, (line_end[1] + line_start[1]) / 2]
        rotation = self.angle_dictionary[position]
        if not is_exterior:
            rect =  psychopy.visual.Rect(
            win = win,
            pos = center,
            units = 'pix',
            width = 20,
            height = edge_length - 20,
            opacity = 0,
            ori = rotation
            )
            rect.draw()
            
            lines_rectangles_container[-1]['rect'] = rect
            lines_rectangles_container[-1]['is_clicked'] = 'not_clicked'
        else:
            lines_rectangles_container[-1]['rect'] = None
            lines_rectangles_container[-1]['is_clicked'] = None

    def _determine_exterior(self, row, col, x_count, y_count, position):
        ## i should write good comments here but not now lol
        ## basically just using position in the array to check relative line position to determine whether to draw rectangles
        if not row:
            if position in ['top_right', 'top']:
                return True
        if not col:
            if not row % 2:
                to_check = ['top_left', 'bottom_left', 'top']
            else:
                to_check = ['top_left']
            if position in to_check:
                return True
        if row == y_count - 1:
            if position in ['bottom_left', 'bottom']:
                return True
        if col == x_count - 1:
            if not row % 2:
                to_check = ['bottom_right']
            else:
                to_check = ['bottom', 'bottom_right', 'top_right']
            if position in to_check:
                return True

        return False

    def _rearrange_point_list(self, start_pos):
        ## outputs a list where the first element is start_pos and the last element is the one before start_pos in point_list
        if start_pos == 'top_left':
            return self.point_list

        return self.point_list[self.point_list.index(start_pos):] + self.point_list[:self.point_list.index(start_pos)-1]

    def _define_line_type(self, is_exterior):
        
        if is_exterior:
            lineWidth = 2.3333333
        else:
            ## this complexity might not be necessary anymore because this whole script is only running once
            if not self.line_width_container_draw:
                self.line_width_container_draw = copy.deepcopy(line_width_container_original)
            lineWidth = self.line_width_container_draw.pop(0)

        return psychopy.visual.Line(
            lineWidth = lineWidth,
            win = win,
            units='pix',
            lineColor=[-1, -1, -1]
            )

###############
## OTHER STUFF###
###############

def compute_accuracy(lines_rectangles_container, clicked_lines):

    all_line_widths = [x['line'].lineWidth for x in lines_rectangles_container if x['rect'] is not None]
    selected_line_widths = [x['line'].lineWidth for x in clicked_lines]

    top_three = sorted(all_line_widths)[:3]
    accuracy = 0    
    for selected_line_width in selected_line_widths:
        if selected_line_width in top_three:
            accuracy += 1
    return accuracy / 3

line_width_container = np.linspace(1, 4, 10)
line_width_container = [round(x, 4) for x in line_width_container]


range_to_width = {}

percentages = [.02, .07, .07] + [.17]*4 + [.07, .07, .02]

base_percentage = 0
for percentage, line_width in zip(percentages, line_width_container):
    range_to_width[(base_percentage, base_percentage+percentage)] = line_width
    base_percentage += percentage +.0000000001
    

def choose_line_width():
    ## draw random from uniform distribution, choose line width
    random_number  = round(np.random.uniform(), 3)
    for key in range_to_width:
        if random_number >= key[0]  and random_number <= key[1]:
            return range_to_width[key]


## initialize full container
line_width_container_original = []

for i in range(400):
    line_width_container_original.append(choose_line_width())
    


PromptResponse = keyboard.Keyboard()
PromptToContinue = visual.TextStim(win=win, name='PromptToContinue',
    text='Press the space bar when you are ready to select the three thinnest lines.',
    font='Open Sans',
    units='pix', pos=(-700, 400), height=35.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Selection"
SelectionClock = core.Clock()
SelectionResponse = keyboard.Keyboard()
PromptToSelect = visual.TextStim(win=win, name='PromptToSelect',
    text='',
    font='Open Sans',
    units='pix', pos=(-700, 400), height=35.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
subject_data = []

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    units='pix', pos=(0, 0), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Prompt"-------
continueRoutine = True
# update component parameters for each repeat
trial_count += 1
lines_rectangles_counter = 0
lines_rectangles_container = []

dhg = DrawHexGrid([-400, 400])

dhg.make_grid()

line_width_container_original = []

for i in range(400):
    line_width_container_original.append(choose_line_width())
    


PromptResponse.keys = []
PromptResponse.rt = []
_PromptResponse_allKeys = []
# keep track of which components have finished
PromptComponents = [PromptResponse, PromptToContinue]
for thisComponent in PromptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PromptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Prompt"-------
while continueRoutine:
    # get current time
    t = PromptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PromptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    for entry in lines_rectangles_container:
        entry['line'].draw()
        
    
    
    
    
    
    
    
    
    # *PromptResponse* updates
    waitOnFlip = False
    if PromptResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PromptResponse.frameNStart = frameN  # exact frame index
        PromptResponse.tStart = t  # local t and not account for scr refresh
        PromptResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PromptResponse, 'tStartRefresh')  # time at next scr refresh
        PromptResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PromptResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PromptResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PromptResponse.status == STARTED and not waitOnFlip:
        theseKeys = PromptResponse.getKeys(keyList=['space'], waitRelease=False)
        _PromptResponse_allKeys.extend(theseKeys)
        if len(_PromptResponse_allKeys):
            PromptResponse.keys = _PromptResponse_allKeys[-1].name  # just the last key pressed
            PromptResponse.rt = _PromptResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *PromptToContinue* updates
    if PromptToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PromptToContinue.frameNStart = frameN  # exact frame index
        PromptToContinue.tStart = t  # local t and not account for scr refresh
        PromptToContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PromptToContinue, 'tStartRefresh')  # time at next scr refresh
        PromptToContinue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PromptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prompt"-------
for thisComponent in PromptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if PromptResponse.keys in ['', [], None]:  # No response was made
    PromptResponse.keys = None
thisExp.addData('PromptResponse.keys',PromptResponse.keys)
if PromptResponse.keys != None:  # we had a response
    thisExp.addData('PromptResponse.rt', PromptResponse.rt)
thisExp.addData('PromptResponse.started', PromptResponse.tStartRefresh)
thisExp.addData('PromptResponse.stopped', PromptResponse.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('PromptToContinue.started', PromptToContinue.tStartRefresh)
thisExp.addData('PromptToContinue.stopped', PromptToContinue.tStopRefresh)
# the Routine "Prompt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Selection"-------
continueRoutine = True
# update component parameters for each repeat
SelectionResponse.keys = []
SelectionResponse.rt = []
_SelectionResponse_allKeys = []
mouse = psychopy.event.Mouse(win = win)

clicked_lines = []

show_text = 'Select three of the thinnest lines'
last_clicked = ''
too_many_timer = 0

submit_box = psychopy.visual.Rect(
win = win,
pos = [600, -400],
units = 'pix',
width = 200,
height = 100,
lineColor = 'black',
fillColor = 'green'
)

submit_text = visual.TextStim(win=win, name='SubmitText',
    text='SUBMIT',
    font='Open Sans',
    units='pix', pos=(600, -400), height=35.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
selection_start = datetime.now()

def save_data(pressed_object, line = None, line_id = None, selected_or_released = None):
    
    selection_rt = datetime.now() - selection_start
    selection_rt_ms = selection_rt.seconds * 1000 + selection_rt.microseconds / 1000
    to_save = {
        'participant': expInfo['participant'],
        'date': expInfo['date'],
        'trial_count': trial_count,
        'prompt_rt_sec': PromptResponse.rt,
        'selection_rt_ms': selection_rt_ms,
        'pressed_object': pressed_object,
        'line_width': line.lineWidth if line else None,
        'line_id': line_id,
        'selected_or_released': selected_or_released,
        'accuracy': compute_accuracy(lines_rectangles_container, clicked_lines) if line is None else None
    }
    
    return to_save
    
# keep track of which components have finished
SelectionComponents = [SelectionResponse, PromptToSelect]
for thisComponent in SelectionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SelectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Selection"-------
while continueRoutine:
    # get current time
    t = SelectionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SelectionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SelectionResponse* updates
    waitOnFlip = False
    if SelectionResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SelectionResponse.frameNStart = frameN  # exact frame index
        SelectionResponse.tStart = t  # local t and not account for scr refresh
        SelectionResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SelectionResponse, 'tStartRefresh')  # time at next scr refresh
        SelectionResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SelectionResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SelectionResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SelectionResponse.status == STARTED and not waitOnFlip:
        theseKeys = SelectionResponse.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _SelectionResponse_allKeys.extend(theseKeys)
        if len(_SelectionResponse_allKeys):
            SelectionResponse.keys = _SelectionResponse_allKeys[-1].name  # just the last key pressed
            SelectionResponse.rt = _SelectionResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    import time
    
    for entry in lines_rectangles_container:
        if entry['rect'] is not None:
            entry['rect'].draw()
            
            if entry['is_clicked'] == 'clicked':
                if entry['rect'].contains(mouse):
                    entry['line'].lineColor = [0,  1, 0]
                else:
                    entry['line'].lineColor = [-1, 1, -1]
            elif entry['rect'].contains(mouse):
                entry['line'].lineColor = [1, -1, -1]
            else:
                entry['line'].lineColor = [-1] * 3
        
        entry['line'].draw()
        
        # people on the forums say you should timeout for 1ms on a loop like this to not hog all the computer's resources
        # but i find that even 0.5 ms timeout makes the display laggy
        #time.sleep(0.0005)
    
    
    if mouse.getPressed()[0]:
        mouse_pos = mouse.getPos()
        for entry in lines_rectangles_container:
            if entry['rect'] is not None and entry['rect'].contains(mouse_pos):
    
                if entry['is_clicked'] == 'clicked':
                    entry['is_clicked'] = 'not_clicked'
                    released_line = clicked_lines.pop(clicked_lines.index(entry))
                    subject_data.append(save_data('line', released_line['line'], released_line['line_id'], 'released'))
    
                else:
                    if len(clicked_lines) < 3:
                        entry['is_clicked'] = 'clicked'
                        clicked_lines.append(entry)
                        subject_data.append(save_data('line', entry['line'], entry['line_id'], 'selected'))
                        
                    else:
                        show_text = "You've clicked three lines already!"
                        too_many_timer = datetime.now()
                    
                time.sleep(.1)
    
                break
    
                
                
    
    # *PromptToSelect* updates
    if PromptToSelect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PromptToSelect.frameNStart = frameN  # exact frame index
        PromptToSelect.tStart = t  # local t and not account for scr refresh
        PromptToSelect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PromptToSelect, 'tStartRefresh')  # time at next scr refresh
        PromptToSelect.setAutoDraw(True)
    if PromptToSelect.status == STARTED:  # only update if drawing
        PromptToSelect.setText(show_text)
    
    
    ## control instruction text
    if not too_many_timer:
        if len(clicked_lines) < 3:
            show_text = 'Select the three thinnest lines.'
        else:
            show_text = 'Press the submit button to confirm your selection and continue'
            submit_box.draw()
            submit_text.draw()
    
    else:
        if (datetime.now() - too_many_timer).seconds > 3:
            too_many_timer = 0
        elif len(clicked_lines) == 3:
            submit_box.draw()
            submit_text.draw()
    
    ## for submit button
    
    if mouse.getPressed()[0]:
        mouse_pos = mouse.getPos()
        if len(clicked_lines) == 3 and submit_box.contains(mouse_pos):
            subject_data.append(save_data('submit'))
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SelectionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Selection"-------
for thisComponent in SelectionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if SelectionResponse.keys in ['', [], None]:  # No response was made
    SelectionResponse.keys = None
thisExp.addData('SelectionResponse.keys',SelectionResponse.keys)
if SelectionResponse.keys != None:  # we had a response
    thisExp.addData('SelectionResponse.rt', SelectionResponse.rt)
thisExp.addData('SelectionResponse.started', SelectionResponse.tStartRefresh)
thisExp.addData('SelectionResponse.stopped', SelectionResponse.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('PromptToSelect.started', PromptToSelect.tStartRefresh)
thisExp.addData('PromptToSelect.stopped', PromptToSelect.tStopRefresh)
# the Routine "Selection" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
import pickle

with open('long_data/{}.pickle'.format(expInfo['participant']), 'wb') as file:
    pickle.dump(subject_data, file)
file.close()

# keep track of which components have finished
BlankComponents = [text]
for thisComponent in BlankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BlankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank"-------
for thisComponent in BlankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

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
