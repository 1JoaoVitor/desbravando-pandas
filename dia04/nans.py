# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%


df["idade"].isna().sum() # quantos NaN tem na coluna
# %%
df.isna()
# %%
df.isna().mean()
#como são valores entre 0 e 1 essa vai ser a proporção de NaN
# %%

df.fillna({"idade": df["idade"].mean(), "renda" : df["renda"].mean()})
# preencher NaN com o que eu quiser
# no caso de idade vai ser com media e de renda com a media 
# %%


df.dropna()
# se tiver qualquer NaN na linha ele remove a linha inteira
df.dropna(subset=["idade", "renda"], how='all', axis=0)
# aqui ele olha só as tabelas escritas e só se todas tiverem NaN
# %%
