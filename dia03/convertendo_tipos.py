# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%

df.dtypes
# que tipos são aquelas colunas?
# %%

df["Points"].astype(str)
# converte coluna para str
# %%
