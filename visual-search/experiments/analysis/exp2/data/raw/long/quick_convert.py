import sys
import pickle
import pandas as pd








if __name__ == '__main__':

	files = sys.argv[1:]
	if not files:
		print('point to pickle files')
		sys.exit(1)

	d_list = []

	for file in files:
		with open(file, 'rb') as f:
			d_list.append(pickle.load(f))
		f.close()

	d = pd.concat([pd.DataFrame(x) for x in d_list], axis = 0)

	d.to_csv('../../exp1_long_data_raw.csv', index = False)