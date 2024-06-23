
# %%
import pandas as pd
df = pd.read_csv("../data/products.csv", sep=";", header= None, names = ["Id", "Name", "Discription"])
df

# sem cabeçalho
# usa o "names para criar um
# %%

df = df.rename(columns={"Name" : "Nome", "Discription" : "Descrição"})
df



# %%

# Outro jeito 

df.rename(columns={"Name" : "Nome", "Discription" : "Descrição"}, inplace=True)
# %%
