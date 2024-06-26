# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user
# %%
df_user["Points"].sum()
# %%


df_summary = df.groupby(["IdCustomer"])["Points"].sum().sort_values(ascending= False)
# agrupa os dados por determinada coluna considerando determinada outra coluna 
# no caso agrupa os clientes pela pontos usando a soma 
# depois disso ordena a coluna da soma 
# %%

df_summary.reset_index()
#transforma em df de volta pois o groupby transforma numa serie
# %%

(df.groupby(["IdCustomer"])
 .agg({
    "Points" : "sum", 
    "UUID" : "count",
    "DtTransaction" : "max"
    }).reset_index().rename(columns= { #transforma em df de volta pois o groupby transforma numa serie
        "Points" : "Valor",
        "IdCustomer" : "Cliente",
        "UUID" : "Frequencia",
        "DtTransaction" : "UltimaData"
    }))
# agrupando mais de uma coisa com diferentes funções ao mesmo tempo com agg
# coluna : funcao 
# %%

# da para criar funções personalizadas e passar dentro do dicionario do agg

def tempo_de_compras(x):
        tempo = df["DtTransaction"].max() - df["DtTransaction"].min()
        return tempo.days

(df.groupby(["IdCustomer"])
 .agg({
    "Points" : "sum", 
    "UUID" : "count",
    "DtTransaction" : ["max", tempo_de_compras] # funcao personalizada
    }).reset_index().rename(columns= { # dps de tudo renomeia as colunas 
        "Points" : "Valor",
        "IdCustomer" : "Cliente",
        "UUID" : "Frequencia",
        "DtTransaction" : "Tempo entre compras"
    }))
# %%
