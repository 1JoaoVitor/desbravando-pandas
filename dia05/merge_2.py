# %%
import pandas as pd

df_customer = pd.read_csv("../data/customers.csv", sep=";")
df_customer

# %%
df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions

# %%
df_transactions_product = pd.read_parquet("../data/transactions_cart.parquet", engine= "fastparquet")
df_transactions_product
# engine = fastparquet foi o único jeito que rodou, por algum motivo engine pyarrow ta com problema 
# %%

df_join = df_transactions.merge(df_customer, how="left", 
                    left_on= "IdCustomer",
                    right_on= "UUID",
                    suffixes= ["_transactions", "_cliente"] )
df_join
# %%

df_join.merge(df_transactions_product, how="inner",
            left_on= "UUID_transactions", 
            right_on="IdTransaction")
# da para encadear merge de uma vez:

# %%
df_join = (df_transactions.merge(df_customer, how="left", 
                    left_on= "IdCustomer",
                    right_on= "UUID",
                    suffixes= ["_transactions", "_cliente"] )
                    .merge(df_transactions_product, how="inner",
                    left_on= "UUID_transactions", 
                    right_on="IdTransaction"))
df_join
# %%

