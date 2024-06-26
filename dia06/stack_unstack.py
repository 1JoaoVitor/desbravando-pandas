# %%

import pandas as pd

df = pd.read_csv("../data/bia_consolidado.csv", sep=";")
df

# %%

df = df.set_index(["cod", "nome", "período"])
# antes é preciso decidir as colunas que ficarão FIXAS

# %%
df_stack = df.stack().reset_index().rename(columns={"level_3":"Tipo Homicidio",
                                                    0:"Qtde"})
# "Juntar dados", empilhar, criando mais linhas, mas diminuindo as colunas, depois renomeando 

#%%
df_unstack = (df_stack.set_index(['cod','nome','período', 'Tipo Homicidio'])
                      .unstack() # tem que passar todos os indices menos o 'valor', pois queremos manter
                      .reset_index())
# fazendo o processo inverso, mas fica visualmente ruim
# %%

homicidios = df_unstack['Qtde'].columns.tolist()
#lista dos tipos de homicidios

df_unstack.columns = ["cod", "nome", "período"] + homicidios # "forçando" as colunas do df 
df_unstack

# pode ser feito com drop level:

"""indentificadores = df_unstack.columns.droplevel(1).tolist()[:3] 
df_unstack.columns = indentificadores + homicidios
df_unstack"""