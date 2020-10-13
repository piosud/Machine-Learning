# -*- coding: utf-8 -*-
"""Set1/Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ialC9kQk7t_u_c4StNf1KBu_4BHPz0MC
"""

import pandas as pd
import numpy as np

with open('train.tsv', 'rb') as my_data:
    df = pd.read_csv(my_data, names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
 #calculating price per meter
    meter = df['A']/df['C']

    df['meter'] = meter
 #calculating mean for price per meter
    mean_meter = np.mean(df['meter'])
    print(mean_meter)
#selecting rows where number of rooms > 2 and price < mean_meter
    conditions = (df[(df['B'] >=3) & (df['meter'] < mean_meter)])
 #saving result to output file
    conditions.to_csv('out1.csv', columns=['B', 'A', 'meter'], header=False, sep='\t')