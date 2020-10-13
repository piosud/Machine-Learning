# -*- coding: utf-8 -*-
"""Set1/Task5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cXd1MDJrMISgFL9_mHlNbf9fdiS7f6B_
"""

import pandas as pd
import matplotlib.pyplot as plt

    survey_data = pd.read_csv(/content/survey_results_public.csv, usecols=['ConvertedComp', 'CompTotal', 'SocialMedia',index_col='SocialMedia'])

survey_data.dropna(inplace=True)
groups = survey_data.groupby('SocialMedia')
#Creating chart
for name, group in groups:
    plt.plot(group["ConvertedComp"], group["CompTotal"], marker="o", label=name, linestyle="")
plt.legend(title="SocialMedia?")
plt.show()