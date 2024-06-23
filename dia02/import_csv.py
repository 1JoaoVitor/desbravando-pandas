# %% 
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep = ";")
df_customers
# %%


df_customers.info(memory_usage='deep')
# %%

df_customers.columns
# %%
df_customers["Points"].describe()
# %%

condicao = df_customers["Points"] == df_customers["Points"].max()
#comparação no pandas, assim que se faz uma filtragem
df_customers[condicao]['Name'].iloc[0]
# %%

df_1 = df_customers[(1000 <= df_customers["Points"]) & (df_customers["Points"] <= 2000)]
df_2 = df_1.copy() 
df_2

# %%
df_2["Points"] = df_2["Points"] + 1000
df_2
# %%


df_customers[["UUID", "Name"]]
#Data frame com duas ou mais colunas se faz assim
# %%

df_customers.columns.tolist()

# %%
colunas = df_customers.columns.tolist()
colunas.sort()


df_customers = df_customers[colunas] #data frame ordenado
#ordenação de colunas do data frame
df_customers
# %%


df_customers.rename(columns= {"Name" : "Nome", "Points" : "Pontos"})
#Renomeando colunas, nome antigo: nome novo
#traz um df NOVO não uma referencia ao antigo como outros métodos   

# %%
