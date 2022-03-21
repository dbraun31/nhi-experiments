import glob
import pandas as pd




if __name__ == '__main__':
	files = glob.glob('../data/*.csv')

	data_list = []

	for file in files:
		data_list.append(pd.read_csv(file))

	d = pd.concat(data_list, axis = 0)

	d.to_csv('../data/compare_lines.csv', index = False)