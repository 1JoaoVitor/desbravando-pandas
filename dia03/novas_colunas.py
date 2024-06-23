# %%
import pandas as pd
import numpy as np 

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df["Points_double"] = df["Points"] *2 
df
# %%

df["Points_ratio"] = df["Points_double"] / df["Points"]
df
# %%

df["Constante"] = 1
df
# %%

np.log(df["Points"])
# %%

df["Points_log"] = np.log(df["Points"]) 
# pode se passar uma lista de colunas, aplicando log em cada uma
df 
# %%

df["Name"].str.upper()

# %%

def get_first(nome: str):
    return nome.split("_")[0]

df["Name"].apply(get_first)
#o apply "aplica" determinada função passada em todos os valores daquela coluna
# %%

get_f = lambda nome: nome.split("_")[0]
get_f("Joao_Vitor")
# %%
df["Name"].apply(lambda nome: nome.split("_")[0])
# lambda é uma função pequena que vai ser usada uma vez só, em uma linha 
# %%


def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"
    
df["Faixa_pontos"] = df["Points"].apply(intervalo_pontos)
df
#intervalo de dados é aplicável assim
# %%

data = {
    "nome" : ["Teo", "Nah", "Maria", "Lara"],
    "recencia" : [1, 30, 10, 45 ],
    "valor" : [100, 2000, 15, 500],
    "frequencia" : [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)
df_crm
# %%

def rfv(row):
    nota = 0 
    if row['recencia'] <= 10:
        nota += 10
    elif row['recencia'] > 10 and row['recencia'] <= 30:
        nota += 5
    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5

    return nota

df_crm.apply(rfv, axis=1) 
# nesse caso, usando apply em um df (não mais numa serie)
# com isso rfv é uma série, uma linha inteira sendo mandada 
# (ao invés de cada valor na coluna), portanto precisa se modificar dentro da função
# para coisas como rfw["Name"]
# rfv = linha 1: 0	Teo	1	100	2, rfv["Name"] = Teo
# axis = eixo, ou seja, aplicando as as linhas para serem "avaliadas"

# %%
