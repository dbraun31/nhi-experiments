from psychopy import visual
import numpy as np

Screen = 0
FullScreen = False

# Monitor settings
Monitor = 'S22C150'
if Monitor == 'S22C150':
    screenRes = [1920,1080]
    screenX = 51.18
    screenY = 31.08
    pixDeg = screenRes[0]/screenX

#Setup window
win = visual.Window(screenRes, color="grey", units='pix', allowGUI=False, fullscr=FullScreen, screen = Screen, monitor = Monitor)

# Create RDK and mask
dots = visual.DotStim(win, nDots = 500, coherence = 1, fieldPos=(0.0, 0.0), fieldSize= 14.7 * pixDeg, 
    fieldShape = 'circle', dotSize = 0.1 * pixDeg, dotLife = 5, dir=180, speed = 13.0/60 * pixDeg, color = 'white', 
    units = 'pix', opacity = 1.0, contrast = 1.0, depth = 0, signalDots = 'same', noiseDots = 'walk')
    
#maskParams
visibleArea = (14.7/2) * pixDeg
zeroOpacArea = (4.9 + 0.5) * pixDeg
shadedArea = (visibleArea - zeroOpacArea)/visibleArea

# Create a raisedCosine mask array and assign it to a Grating stimulus (grey outside, transparent inside)
raisedCosTexture = visual.filters.makeMask(14.7 * pixDeg, shape= 'raisedCosine', fringeWidth= shadedArea, radius = [1.0, 1.0])
invRaisedCosTexture = -raisedCosTexture # inverts mask to blur edges instead of center
dotsMask = visual.GratingStim(win, mask = invRaisedCosTexture, tex=None, contrast= 1.0, size=(15.2 * pixDeg, 15.2 * pixDeg), color = 'grey')


f = 0
while f < 240:
    dots.draw()
    #dotsMask.draw()
    win.flip()
    f += 1