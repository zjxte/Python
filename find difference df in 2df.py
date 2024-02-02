import pandas as pd
import numpy as np

df_cis = pd.read_csv(r'C:\Users\Li\Desktop\temp\Atlas One\data\df_cis.csv', dtype=object)
df_atlas = pd.read_csv(r'C:\Users\Li\Desktop\temp\Atlas One\data\df_atlas.csv', dtype=object)

# 在cis_df中，找出所有记录在df_atlas中不存在的记录
# 记录存在于cis_df种，但不存在与df_atlas中


df_new = df_cis[np.isin(df_cis['CONTACTID'], df_atlas['id'], invert=True)]

print(df_new)

