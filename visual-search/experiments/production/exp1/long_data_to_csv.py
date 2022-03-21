import pandas as pd
import pickle
import sys






if __name__ == '__main__':

	f = sys.argv[1]

	if not f:
		print('point to the file to convert')
		sys.exit(1)

	with open(f, 'rb') as file:
		d = pickle.load(file)

	d = pd.DataFrame(d)
	d.to_csv('long_data/0.csv', index = False)