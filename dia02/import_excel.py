# %% 
import pandas as pd 

df = pd.read_excel("../data/transactions.xlsx")
df
# %%

df.shape
# %%

df.head(5)
# %%

colunas = df.columns.tolist()
colunas.sort()

df = df[colunas]
df 
# %%
