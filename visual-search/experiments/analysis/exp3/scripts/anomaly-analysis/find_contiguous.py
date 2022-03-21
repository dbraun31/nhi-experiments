import pandas as pd
import random
import math
import sys
import pickle


def find_distance(point1, point2):
	return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def format_next_line(winner, top_or_bottom):
	## flip top and bottom for next line to forward to next position
	if top_or_bottom == 'top':
		next_line = {'next_line_id': winner['line_id'], 
		'next_starting_point': (winner['bottom_x'], winner['bottom_y'])}
	elif top_or_bottom == 'bottom':
		next_line = {'next_line_id': winner['line_id'], 
		'next_starting_point': (winner['top_x'], winner['top_y'])}

	return next_line


def find_next(prev_line, anomaly, all_lines, is_first):
	'''
	prev_line
		{'prev_line_id': ..., 'prev_starting_point': (x, y)}
	given a previous point, find the two other lines that intersect with that point
	if it's the first iteration, choose one randomly
	otherwise, minimize the distance between center points
	'''

	candidates = []

	## drop previous line from consideration set
	all_lines = [x for x in all_lines if x['line_id'] != prev_line['prev_line_id']]

	for line in all_lines:
		if (line['top_x'], line['top_y']) == prev_line['prev_starting_point']:
			candidates.append({'line': line, 'top_or_bottom': 'top'})
		elif (line['bottom_x'], line['bottom_y']) == prev_line['prev_starting_point']:
			candidates.append({'line': line, 'top_or_bottom': 'bottom'})
		if len(candidates) == 2:
			break

	'''
	print('prev_line: {}'.format(prev_line))
	print('\n')
	print(candidates)
	print('\n\n')
	'''


	if is_first:
		winner = random.sample(candidates, 1)[0]
		next_line = format_next_line(winner['line'], winner['top_or_bottom'])
		return next_line, all_lines


	if len(candidates) == 1:
		return format_next_line(candidates[0]['line'], candidates[0]['top_or_bottom']), all_lines

	elif len(candidates) == 2:
		## find the candidate line with the smaller distance

		d0 = find_distance((candidates[0]['line']['line_mid_x'], candidates[0]['line']['line_mid_y']), \
			(anomaly['line_mid_x'], anomaly['line_mid_y']))
		d1 = find_distance((candidates[1]['line']['line_mid_x'], candidates[1]['line']['line_mid_y']), \
			(anomaly['line_mid_x'], anomaly['line_mid_y']))

		winner = candidates[0] if d0 < d1 else candidates[1]

		next_line = format_next_line(winner['line'], winner['top_or_bottom'])

		return next_line, all_lines

	else:
		print('PROBLEM')
		sys.exit(1)



def find_contiguous(anomaly, all_lines):
	'''
	inputs:
	anomalies
		{anomaly_line_id: ..., anomaly_mid_x: ..., anomaly_mid_y: ...}
	all_lines
		[{line_id: ..., top_x: ..., top_y: ..., 'bottom_x': ..., 'bottom_y': ...}, ...]

	output:
		list of line_ids for contiguous lines
	'''

	## get more detail about the anomaly 
	anomaly = [x for x in all_lines if x['line_id'] == anomaly['anomaly_line_id']][0]

	contiguous = []

	original_starting_point = (anomaly['bottom_x'], anomaly['bottom_y'])
	prev_line = {'prev_line_id': anomaly['line_id'], 'prev_starting_point': original_starting_point}
	next_line = {'next_starting_point': ()}
	is_first = True

	while next_line['next_starting_point'] != original_starting_point:
		## THE CYCLING OF PREV AND NEXT LINES IS ALL MESSED UP
		next_line, all_lines = find_next(prev_line, anomaly, all_lines, is_first = is_first)
		contiguous.append(next_line['next_line_id'])
		if is_first:
			is_first = False
		prev_line = {'prev_line_id': next_line['next_line_id'], 
		'prev_starting_point': next_line['next_starting_point']}




	return contiguous


'''
def find_contiguous_simple(anomaly, all_lines):
	## THIS APPROACH DOESNT WORK
	distances = []

	pop_index = all_lines.index([x for x in all_lines if x['line_id'] == anomaly['anomaly_line_id']][0])
	_ = all_lines.pop(pop_index)

	for line in all_lines:
		distance = math.sqrt((anomaly['anomaly_mid_x'] - line['line_mid_x'])**2 + \
			(anomaly['anomaly_mid_y'] - line['line_mid_y'])**2)

		distances.append({'line_id': line['line_id'], 'distance': distance})

	return sorted(distances, key = lambda x: x['distance'])[:10]
'''

if __name__ == '__main__':

	verbose = False

	anomalies = pd.read_csv('anomalies.csv').to_dict('records')
	all_lines = pd.read_csv('../../data/exp3_line_data.csv')
	all_lines = all_lines[(all_lines['participant'] == 59) & (all_lines['trial_count'] == 0)]
	all_lines_pre = all_lines[['line_id', 'top_x', 'top_y', 'bottom_x', 'bottom_y']].to_dict('records')

	all_lines = []

	for line in all_lines_pre:
		line['line_mid_x'] = (line['top_x'] + line['bottom_x']) / 2
		line['line_mid_y'] = (line['top_y'] + line['bottom_y']) / 2
		all_lines.append(line)
	

	#anomaly = random.sample(anomalies, 1)[0]

	#print(anomaly)
	#print('\n\n')

	output = {}

	for anomaly in anomalies:

		contiguous = find_contiguous(anomaly, all_lines)

		output[anomaly['anomaly_line_id']] = contiguous

	with open('contiguous_dict.pickle', 'wb') as file:
		pickle.dump(output, file)
	file.close()
	print('All good')



	if verbose:
		print('\n\n')
		print('Anomaly: {}'.format(anomaly['anomaly_line_id']))
		print('\n\n')
		print('Contiguous\n')
		print(*contiguous, sep = '\n')

		print('\n\n')

		input('press any key to continue\nW')