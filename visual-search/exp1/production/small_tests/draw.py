import sys
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)


line_container = []

for i in range(10):

    line_container.append(psychopy.visual.Line(
        win = win,
        units = 'pix',
        lineWidth = 4,
        lineColor = [-1, -1, -1],
        autoDraw = True
    ))

print(line_container)
sys.exit(1)

text = psychopy.visual.TextStim(
    win=win,
    text="Hello, world!",
    color=[-1, -1, -1]
)

# text is black
text.draw()

# change text to green
text.color = [-1, 0, -1]

# draw text again
text.draw()

win.flip()

psychopy.event.waitKeys()

win.close()