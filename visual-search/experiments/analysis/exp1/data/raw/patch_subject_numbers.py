import pandas as pd
import pickle
import sys
import glob




def main(file, subject_counter):
	with open('line_data/unnamed/' + file, 'rb') as f:
		line_data = pickle.load(f)
	with open('long_data/unnamed/' + file, 'rb') as f:
		long_data = pickle.load(f)

	line_data = pd.DataFrame(line_data)
	line_data['participant'] = subject_counter
	long_data = pd.DataFrame(long_data)
	long_data['participant'] = subject_counter

	line_data = line_data.to_dict('records')
	long_data = long_data.to_dict('records')

	with open('line_data/' + str(subject_counter) + file, 'wb') as f:
		pickle.dump(line_data, f)
	with open('long_data/' + str(subject_counter) + file, 'wb') as f:
		pickle.dump(long_data, f)



def sort(rel_files):
	files_and_times = []

	for file in rel_files:
		time = int(file.split('_')[-1].split('.')[0])
		files_and_times.append([file, time])

	files_and_times = sorted(files_and_times, key = lambda x: x[1])
	return [x[0] for x in files_and_times]
	



if __name__ == '__main__':

	files = glob.glob('line_data/unnamed/_2021*')
	files = [x.split('/')[-1] for x in files]

	months = ['Sep', 'Oct']
	subject_counter = 2

	for month in months:
		
		rel_files = [x for x in files if month in x]
		
		rel_files = sort(rel_files)


		for file in rel_files:
			subject_counter += 1
			
			main(file, subject_counter)