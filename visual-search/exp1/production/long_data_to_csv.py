import pandas as pd
import pickle






if __name__ == '__main__':
	with open('long_data/0.pickle', 'rb') as file:
		d = pickle.load(file)

	d = pd.DataFrame(d)
	d.to_csv('long_data/0.csv', index = False)