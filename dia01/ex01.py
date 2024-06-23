# %%
import pandas as pd
# %%
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

serie = pd.Series(dados)
# %%

media = serie.mean()
dvp = serie.std()
valor_max = serie.max()

print(media, dvp, valor_max)
# %%
