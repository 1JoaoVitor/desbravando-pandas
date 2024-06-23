# %%
import pandas as pd 

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df = df.sort_values(by = "Points", ascending=False)
df = df.rename(columns={"Name" : "Nome", "Points" : "Pontos"}, inplace = True)
df
# Ordenação do df por uma coluna, ascendente ou não


# %% 

df.sort_values(by = ["Points", "Name"], ascending= [False, True])

# Uma ordenação de pontos e caso empate uma ordenação por nome passando listas 

# %%



# Pode ser feito assim também:
df = (df.sort_values(by = "Points", ascending=False).rename(columns={"Name" : "Nome", "Points" : "Pontos"}))

df
# %%
