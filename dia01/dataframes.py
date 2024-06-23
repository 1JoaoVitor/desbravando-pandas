# %%
import pandas as pd
# %%

data = {
    "nome" : ["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade" : [31, 32, 31, 2]
}

data['idade'][0] 
# %%

# transformando em dataframe (df)

df = pd.DataFrame(data)
df
# %%

# iloc garante a posição do item

df["idade"].iloc[0]  # coluna

# %%
df.iloc[0]  # linha 
# %%

df.index
# %%
df.columns
# %%
df.info()
# %%
df.info(memory_usage='deep')
# %%

df.dtypes 
# %%

df.describe()




































# %%
