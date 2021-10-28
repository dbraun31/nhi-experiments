#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Thu 28 Oct 2021 04:58:18 PM EDT
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
import pickle
import random
trial_count = -1

time_start_experiment = datetime.now()
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
    originPath='visual-search_exp3_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=1, 
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

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to the experiment:\n\nYou will be viewing a series of images designed to capture aspects of the materials that the microscopist would see. You will view a 4 x 4 display of hexagons. The important features are the boundaries between these hexagons. Your task is going to be to search the array and select three of the thinnest lines that you can find. These lines will always be in the interior of the array between two hexagons. Wait for the experimenter to proceed.',
    font='Open Sans',
    units='pix', pos=(0, 0), height=30.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WelcomeResponse = keyboard.Keyboard()

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
ExampleResponse = keyboard.Keyboard()
DemoText = visual.TextStim(win=win, name='DemoText',
    text='Press the space bar when you are ready to see the rest of the instructions.',
    font='Open Sans',
    units='pix', pos=(-700, 350), height=35.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionsText = visual.TextStim(win=win, name='InstructionsText',
    text='When the image first appears, you can search the display for as long as you like. Once you are ready to identify the lines that you think are three of the thinnest, press the spacebar. You can then use your mouse to select the lines you have chosen. You can click and unclick lines, if you change your mind. Once you are happy with your three selections you can press the submit button. Please work through each search array as quickly and accurately as possible. You will be able to take short breaks before starting each search task.\n\nYou will do one practice round before starting the real experiment.\n\nPlease press the space bar when you are ready to begin the practice.',
    font='Open Sans',
    units='pix', pos=(0, 0), height=30.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstructionsResponse = keyboard.Keyboard()

# Initialize components for Routine "Prompt"
PromptClock = core.Clock()
import psychopy
## this line is essential for mapping coordinates of mouse clicks to the coordinates of rectangles
win.units = 'pix'

## print_line_widths
## ^ flag for troubleshooting

## initialize data containers
subject_data = []
line_data = []
lines_rectangles_container = []

## anomaly stuff
anomaly_probability = .3
anomalies = [
['r0c1_bottom_right', 2],
['r0c2_bottom_left', 2],
['r0c2_bottom_right', 2],
['r1c0_bottom_right', 1],
['r1c0_right', 0],
['r1c1_bottom_left', 1],
['r1c1_bottom_right', 0],
['r1c1_right', 0],
['r1c2_bottom_left', 0],
['r1c2_bottom_right', 1],
['r2c1_bottom_right', 0],
['r2c1_right', 1],
['r2c2_bottom_left', 2],
['r2c2_bottom_right', 2],
['r2c2_right', 2]
]

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

            lines_rectangles_container.append({'line': line, 'line_id': 'r{}c{}_{}'.format(self.row, self.col, self.point_to_side[position]), 'is_exterior': is_exterior})
                
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

    all_line_widths = [x['line'].lineWidth for x in lines_rectangles_container if x['rect'] is not None and x['line'].lineWidth is not None]
    selected_line_widths = [x['line'].lineWidth for x in clicked_lines]

    top_three = sorted(all_line_widths)[:3]
    accuracy = 0    
    for selected_line_width in selected_line_widths:
        if selected_line_width in top_three:
            accuracy += 1
    return accuracy / 3
    
def compute_possible_thinnest_lines(lines_rectangles_container):
    all_line_widths = [x['line'].lineWidth for x in lines_rectangles_container if x['rect'] is not None and x['line'].lineWidth is not None]
    
    top_three = sorted(all_line_widths)[:3]
    return len([x for x in all_line_widths if x <= top_three[-1]])
    
    
def get_line_orientation(line):
    if line is None:
        return None
    top = line.start if line.start[1] > line.end[1] else line.end
    bottom= line.start if line.start[1] < line.end[1] else line.end
    if top[0] < bottom[0]:
        return 'back_slash'
    if top[0] > bottom[0]:
        return 'forward_slash'
    return 'vertical'
    
    
def save_data(pressed_object, line = None, line_id = None, selected_or_released = None):
    
    ## compute line top and bottom
    if line is not None:
        top = line.start if line.start[1] > line.end[1] else line.end
        bottom= line.start if line.start[1] < line.end[1] else line.end
    else:
        top = bottom = None
        
    anomaly_center = ''
    anomaly_mid_x = ''
    anomaly_mid_y = ''
    if is_anomaly_trial:
        anomaly_mid_x = (anomaly_line['line'].start[0] + anomaly_line['line'].end[0]) / 2
        anomaly_mid_y = (anomaly_line['line'].start[1] + anomaly_line['line'].end[1]) / 2
    
    selection_rt = datetime.now() - selection_start
    selection_rt_ms = selection_rt.seconds * 1000 + selection_rt.microseconds / 1000
    to_save = {
        'participant': expInfo['participant'],
        'date': expInfo['date'],
        'overall_time': datetime.now() - time_start_experiment,
        'trial_count': trial_count,
        'click_order': click_order,
        'prompt_rt_sec': PromptResponse.rt,
        'selection_rt_ms': selection_rt_ms,
        'pressed_object': pressed_object,
        'line_width': line.lineWidth if line else None,
        'top_x': top[0] if top is not None else None,
        'top_y': top[1] if top is not None else None,
        'bottom_x': bottom[0] if bottom is not None else None,
        'bottom_y': bottom[1] if bottom is not None else None,
        'line_id': line_id,
        'line_orientation': get_line_orientation(line),
        'selected_or_released': selected_or_released,
        'accuracy': compute_accuracy(lines_rectangles_container, clicked_lines) if line is None else None,
        'possible_thinnest_lines': compute_possible_thinnest_lines(lines_rectangles_container),
        'is_practice': is_practice,
        'is_anomaly_trial': is_anomaly_trial,
        'anomaly_mid_x': anomaly_mid_x,
        'anomaly_mid_y': anomaly_mid_y,
        'anomaly_line_id': anomaly_line['line_id'],
        'anomaly_group': anomaly_group
    }
    
    return to_save
    
    
def save_line_data(lines_rectangles_container, line_data):
    ## save out line parameters on each trial
    
    for entry in lines_rectangles_container:
        top = entry['line'].start if entry['line'].start[1] > entry['line'].end[1] else entry['line'].end
        bottom= entry['line'].start if entry['line'].start[1] < entry['line'].end[1] else entry['line'].end
            
        line_data.append({
            'participant': expInfo['participant'],
            'date': expInfo['date'],
            'trial_count': trial_count,
            'line_id': entry['line_id'],
            'line_width': entry['line'].lineWidth,
            'is_exterior': entry['is_exterior'],
            'top_x': top[0], 
            'top_y': top[1] ,
            'bottom_x': bottom[0],
            'bottom_y': bottom[1],
            })
       
    if not os.path.exists('line_data'):
        os.mkdir('line_data')
    with open('line_data/{}_{}_line.pickle'.format(expInfo['participant'], expInfo['date']), 'wb') as file:
        pickle.dump(line_data, file)
    file.close()
            
    
    
    
    

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
PromptToSelect = visual.TextStim(win=win, name='PromptToSelect',
    text='',
    font='Open Sans',
    units='pix', pos=(-700, 400), height=35.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
TimingText = visual.TextStim(win=win, name='TimingText',
    text='',
    font='Open Sans',
    units='pix', pos=(0, 0), height=30.0, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Ending"
EndingClock = core.Clock()
EndingText = visual.TextStim(win=win, name='EndingText',
    text='This concludes the experiment- thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=24.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeResponse.keys = []
WelcomeResponse.rt = []
_WelcomeResponse_allKeys = []
# keep track of which components have finished
WelcomeComponents = [WelcomeText, WelcomeResponse]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.tStart = t  # local t and not account for scr refresh
        WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeResponse* updates
    waitOnFlip = False
    if WelcomeResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeResponse.frameNStart = frameN  # exact frame index
        WelcomeResponse.tStart = t  # local t and not account for scr refresh
        WelcomeResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeResponse, 'tStartRefresh')  # time at next scr refresh
        WelcomeResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(WelcomeResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(WelcomeResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if WelcomeResponse.status == STARTED and not waitOnFlip:
        theseKeys = WelcomeResponse.getKeys(keyList=['q'], waitRelease=False)
        _WelcomeResponse_allKeys.extend(theseKeys)
        if len(_WelcomeResponse_allKeys):
            WelcomeResponse.keys = _WelcomeResponse_allKeys[-1].name  # just the last key pressed
            WelcomeResponse.rt = _WelcomeResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)
# check responses
if WelcomeResponse.keys in ['', [], None]:  # No response was made
    WelcomeResponse.keys = None
thisExp.addData('WelcomeResponse.keys',WelcomeResponse.keys)
if WelcomeResponse.keys != None:  # we had a response
    thisExp.addData('WelcomeResponse.rt', WelcomeResponse.rt)
thisExp.addData('WelcomeResponse.started', WelcomeResponse.tStartRefresh)
thisExp.addData('WelcomeResponse.stopped', WelcomeResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Example"-------
continueRoutine = True
# update component parameters for each repeat
ExampleResponse.keys = []
ExampleResponse.rt = []
_ExampleResponse_allKeys = []
dhg = DrawHexGrid([-400, 400])

dhg.make_grid()
# keep track of which components have finished
ExampleComponents = [ExampleResponse, DemoText]
for thisComponent in ExampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Example"-------
while continueRoutine:
    # get current time
    t = ExampleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExampleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExampleResponse* updates
    waitOnFlip = False
    if ExampleResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExampleResponse.frameNStart = frameN  # exact frame index
        ExampleResponse.tStart = t  # local t and not account for scr refresh
        ExampleResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExampleResponse, 'tStartRefresh')  # time at next scr refresh
        ExampleResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExampleResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExampleResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExampleResponse.status == STARTED and not waitOnFlip:
        theseKeys = ExampleResponse.getKeys(keyList=['space'], waitRelease=False)
        _ExampleResponse_allKeys.extend(theseKeys)
        if len(_ExampleResponse_allKeys):
            ExampleResponse.keys = _ExampleResponse_allKeys[-1].name  # just the last key pressed
            ExampleResponse.rt = _ExampleResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *DemoText* updates
    if DemoText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DemoText.frameNStart = frameN  # exact frame index
        DemoText.tStart = t  # local t and not account for scr refresh
        DemoText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DemoText, 'tStartRefresh')  # time at next scr refresh
        DemoText.setAutoDraw(True)
    
    for entry in lines_rectangles_container:
        entry['line'].draw()
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Example"-------
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ExampleResponse.keys in ['', [], None]:  # No response was made
    ExampleResponse.keys = None
thisExp.addData('ExampleResponse.keys',ExampleResponse.keys)
if ExampleResponse.keys != None:  # we had a response
    thisExp.addData('ExampleResponse.rt', ExampleResponse.rt)
thisExp.addData('ExampleResponse.started', ExampleResponse.tStartRefresh)
thisExp.addData('ExampleResponse.stopped', ExampleResponse.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('DemoText.started', DemoText.tStartRefresh)
thisExp.addData('DemoText.stopped', DemoText.tStopRefresh)
# the Routine "Example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
InstructionsResponse.keys = []
InstructionsResponse.rt = []
_InstructionsResponse_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsText, InstructionsResponse]
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
    
    # *InstructionsText* updates
    if InstructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText.frameNStart = frameN  # exact frame index
        InstructionsText.tStart = t  # local t and not account for scr refresh
        InstructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText, 'tStartRefresh')  # time at next scr refresh
        InstructionsText.setAutoDraw(True)
    
    # *InstructionsResponse* updates
    waitOnFlip = False
    if InstructionsResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsResponse.frameNStart = frameN  # exact frame index
        InstructionsResponse.tStart = t  # local t and not account for scr refresh
        InstructionsResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsResponse, 'tStartRefresh')  # time at next scr refresh
        InstructionsResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstructionsResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstructionsResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstructionsResponse.status == STARTED and not waitOnFlip:
        theseKeys = InstructionsResponse.getKeys(keyList=['space'], waitRelease=False)
        _InstructionsResponse_allKeys.extend(theseKeys)
        if len(_InstructionsResponse_allKeys):
            InstructionsResponse.keys = _InstructionsResponse_allKeys[-1].name  # just the last key pressed
            InstructionsResponse.rt = _InstructionsResponse_allKeys[-1].rt
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
thisExp.addData('InstructionsText.started', InstructionsText.tStartRefresh)
thisExp.addData('InstructionsText.stopped', InstructionsText.tStopRefresh)
# check responses
if InstructionsResponse.keys in ['', [], None]:  # No response was made
    InstructionsResponse.keys = None
thisExp.addData('InstructionsResponse.keys',InstructionsResponse.keys)
if InstructionsResponse.keys != None:  # we had a response
    thisExp.addData('InstructionsResponse.rt', InstructionsResponse.rt)
thisExp.addData('InstructionsResponse.started', InstructionsResponse.tStartRefresh)
thisExp.addData('InstructionsResponse.stopped', InstructionsResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "Prompt"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial_count += 1
    lines_rectangles_counter = 0
    click_order = 0
    if not trial_count:
        is_practice = True
    else:
        is_practice = False
    
    lines_rectangles_container = []
    
    dhg = DrawHexGrid([-400, 400])
    
    dhg.make_grid()
    
    
    if trial_count == 0:
        is_anomaly_trial  = False
    else:
        is_anomaly_trial = np.random.uniform() < anomaly_probability
        
    
    anomaly_line_id = ''
    anomaly_group = ''
    anomaly_line = {'line_id': ''}
    if is_anomaly_trial:
        anomaly_line_id, anomaly_group = random.sample(anomalies, 1)[0]
        anomaly_line = [x for x in lines_rectangles_container if x['line_id'] == anomaly_line_id][0]
        X = lines_rectangles_container.index([x for x in lines_rectangles_container if x['line_id'] == anomaly_line_id][0])
        lines_rectangles_container[X]['line'].lineWidth = None
    
    win.flip() 
    
    save_line_data(lines_rectangles_container, line_data)
    
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
        
        #rect1.draw()
        
        
        
        for entry in lines_rectangles_container:
            if entry['line_id'] != anomaly_line['line_id']:
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
    trials.addData('PromptResponse.keys',PromptResponse.keys)
    if PromptResponse.keys != None:  # we had a response
        trials.addData('PromptResponse.rt', PromptResponse.rt)
    trials.addData('PromptResponse.started', PromptResponse.tStartRefresh)
    trials.addData('PromptResponse.stopped', PromptResponse.tStopRefresh)
    trials.addData('PromptToContinue.started', PromptToContinue.tStartRefresh)
    trials.addData('PromptToContinue.stopped', PromptToContinue.tStopRefresh)
    # the Routine "Prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Selection"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    
        
                
                
                
                
                
                
        
        
        
        
        
        
        
        
        
    
    # keep track of which components have finished
    SelectionComponents = [PromptToSelect]
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
        import time
        
        ## check for hovering
        for entry in lines_rectangles_container:
            if entry['rect'] is not None and entry['line_id'] != anomaly_line['line_id']:
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
            
            if entry['line_id'] != anomaly_line['line_id']:
                entry['line'].draw()
            
            # people on the forums say you should timeout for 1ms on a loop like this to not hog all the computer's resources
            # but i find that even 0.5 ms timeout makes the display laggy
            #time.sleep(0.0005)
        
        ## react to mouse press
        if mouse.getPressed()[0]:
            mouse_pos = mouse.getPos()
            for entry in lines_rectangles_container:
                if entry['rect'] is not None and entry['rect'].contains(mouse_pos) and entry['line_id'] != anomaly_line['line_id']:
        
                    if entry['is_clicked'] == 'clicked':
                        click_order += 1
                        entry['is_clicked'] = 'not_clicked'
                        released_line = clicked_lines.pop(clicked_lines.index(entry))
                        subject_data.append(save_data('line', released_line['line'], released_line['line_id'], 'released'))
        
                    else:
                        if len(clicked_lines) < 3:
                            click_order += 1
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
                click_order += 1
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
    trials.addData('PromptToSelect.started', PromptToSelect.tStartRefresh)
    trials.addData('PromptToSelect.stopped', PromptToSelect.tStopRefresh)
    # the Routine "Selection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    # update component parameters for each repeat
    if is_practice:
        ISI_display_text = "You just finished the practice trial. Moving forward with the experiment you will be doing trials like this for about 20 minutes. If you would like more clarification before beginning, you can ask the experimenter any questions at this time. Otherwise, press spacebar to continue to the experiment."
    else:
        ISI_display_text = "Press the space bar to see the next display."
        
    
    TimingText.setText(ISI_display_text)
    import pickle
    
    if not os.path.exists('long_data'):
        os.mkdir('long_data')
    with open('long_data/{}_{}_long.pickle'.format(expInfo['participant'], expInfo['date']), 'wb') as file:
        pickle.dump(subject_data, file)
    file.close()
    
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    ISIComponents = [TimingText, key_resp_2]
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
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TimingText* updates
        if TimingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TimingText.frameNStart = frameN  # exact frame index
            TimingText.tStart = t  # local t and not account for scr refresh
            TimingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TimingText, 'tStartRefresh')  # time at next scr refresh
            TimingText.setAutoDraw(True)
        
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
    trials.addData('TimingText.started', TimingText.tStartRefresh)
    trials.addData('TimingText.stopped', TimingText.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100.0 repeats of 'trials'


# ------Prepare to start Routine "Ending"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndingComponents = [EndingText]
for thisComponent in EndingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ending"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndingText* updates
    if EndingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndingText.frameNStart = frameN  # exact frame index
        EndingText.tStart = t  # local t and not account for scr refresh
        EndingText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndingText, 'tStartRefresh')  # time at next scr refresh
        EndingText.setAutoDraw(True)
    if EndingText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndingText.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            EndingText.tStop = t  # not accounting for scr refresh
            EndingText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EndingText, 'tStopRefresh')  # time at next scr refresh
            EndingText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ending"-------
for thisComponent in EndingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndingText.started', EndingText.tStartRefresh)
thisExp.addData('EndingText.stopped', EndingText.tStopRefresh)

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
