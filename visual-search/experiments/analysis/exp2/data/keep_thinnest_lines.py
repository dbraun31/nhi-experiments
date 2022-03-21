import sys
import pandas as pd
import numpy as np


def main(d):

	out = []

	for participant in d['participant'].unique():
		for trial in range(100):
			sub_d = d[(d['participant'] == participant) & (d['trial_count'] == trial)]
			dict_d = sub_d.to_dict('records')

			line_widths = sorted([[x['line_width'], x['line_id'], x['line_orientation']] for x in dict_d], key = lambda x: x[0])

			thinnest_lines = line_widths[:3]

			other_thinnest = [x for x in line_widths[3:] if x[0] == thinnest_lines[-1][0]]

			if other_thinnest:
				thinnest_lines += other_thinnest

			for line in thinnest_lines:
				out.append({'participant': participant, 'trial_count': trial, 'line_width': line[0],\
					'line_id': line[1], 'line_orientation': line[2]})

	return out





if __name__ == '__main__':

	file = sys.argv[1:]
	if not file:
		print('Point to line data')
		sys.exit(1)

	d = pd.read_csv(file[0])

	out = pd.DataFrame(main(d))

	out.to_csv('thinnest_lines_raw.csv', index = False)
