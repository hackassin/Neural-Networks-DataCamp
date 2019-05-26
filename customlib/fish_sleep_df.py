import pandas as pd
import numpy as np

def fish_data_extract(args):
    df = pd.read_csv(r"C:\Users\amlan\Documents\Git Repos\Machine Learning\Neural-Networks-DataCamp\customlib\datasets\gandhi_et_al_bouts.csv")
    # print(df.head())
    bout_wt = df[df['genotype'] == 'wt']
    bout_lengths_wt = np.array(bout_wt['bout_length'])
    bout_mut = df[df['genotype'] == 'mut']
    bout_lengths_mut = np.array(bout_mut['bout_length'])
    bout_het = df[df['genotype'] == 'mut']
    bout_lengths_het = np.array(bout_het['bout_length'])

    if(args == 'wt'):
        return bout_lengths_wt
    elif(args == 'mut'):
        return bout_lengths_mut
    elif(args == 'het'):
        return bout_lengths_het
    else:
        return ("Invalid argument")

#fish_data_extract('wt')