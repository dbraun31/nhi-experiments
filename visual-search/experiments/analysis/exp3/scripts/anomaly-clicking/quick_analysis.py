import pandas as pd
import pickle
import sys







if __name__ == '__main__':

  trial_summary = pd.read_csv('trial_summary.csv')

  trial_summary_dict = trial_summary.to_dict('records')

  with open('contiguous_dict.pickle', 'rb') as file:
    contiguous_dict = pickle.load(file)



  trial_summary_start = [x for x in trial_summary_dict if x['is_anomaly_trial'] == 'True']
  trial_summary_end = []


  for trial in trial_summary_start:
    num_contiguous = 0
    for i in range(1,4):
      if trial['selected_line_{}'.format(i)] in contiguous_dict[trial['anomaly_line_id']]:
        num_contiguous += 1
    trial['num_contiguous'] = num_contiguous
    trial_summary_end.append(trial)

  trial_summary = pd.DataFrame(trial_summary_end)