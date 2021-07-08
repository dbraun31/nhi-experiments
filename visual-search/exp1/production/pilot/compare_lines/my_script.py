import psychopy




def draw_line():

	psychopy.visual.Line(
				win = win,
				units='pix',
				lineColor=[-1, -1, -1]
				)

	line.start = [-200, 200]
	line.end = [-200, -200]
	line.draw()