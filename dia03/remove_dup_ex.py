# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
# %%

df_last = df.sort_values(by= "DtTransaction", ascending= False)
df_last
# ordenando os consumidores e suas transações 
# %%
df_last = df_last.drop_duplicates(subset= "IdCustomer", keep="first")
df_last 
# deixando apenas as últimas transações de cada um
# %%

df_last["IdCustomer"].nunique()
# Confirmando que só tem valores únicos

# %%

condicao = df["IdCustomer"] == "f3a268f2-1788-47da-bc79-2680a1721}254"
df[condicao]
# Pegando todas as compras do df original 
# %%

df_last[df_last["IdCustomer"] == "f3a268f2-1788-47da-bc79-2680a1721254"]
# verificando que a compra do df_last é realmente a última para esse cliente
# %%
