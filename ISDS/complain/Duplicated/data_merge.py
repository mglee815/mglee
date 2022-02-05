import pandas as pd
import numpy as np
import pickle as pkl

df1 = pd.read_csv("Duplicated/sample5data/sample_df1.csv")
df2 = pd.read_csv("Duplicated/sample5data/sample_df2.csv")
df3 = pd.read_csv("Duplicated/sample5data/sample_df3.csv")
df4 = pd.read_csv("Duplicated/sample5data/sample_df4.csv")

df_all = pd.concat([df1, df2, df3, df4])
print('Concat Finish')

df_all.to_pickle("Duplicated/sample5data/sample5_df.pkl")
print("Save as pkl")



