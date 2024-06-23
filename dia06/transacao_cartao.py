# %%
import pandas as pd
import numpy as np

data = {
    "idTransaction" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "idCliente" : [1, 2, 3, 3, 3, 2, 2, 1, 1, 2],
    "dtTransaction" : ["10/01/2024", "18/01/2024", "04/02/2024", "22/02/2024", "05/03/2024",
                       "20/02/2024", "10/03/2024", "14/01/2024", "06/03/2024", "19/03/2024"],
    "Valor" : [250, 300, 450, 230, 35, 12, 467, 1200, 670, 324],
    "Parcelas" : [2, 3, 3, 2, 1, 1, 3, 5, 3, 2]
}

df = pd.DataFrame(data)
df

# %%

df['dtTransaction'] = pd.to_datetime(df['dtTransaction'],
                                     format='%d/%m/%Y')

df
# %%

def fatia_parcelas(row):
    return [row["Valor"]/ row["Parcelas"] for i in range(row["Parcelas"])]

df['ValorParcela'] = df.apply(fatia_parcelas, axis=1)
# Criando uma lista de cada parcela na tabela ValorParcela
df

# %%

df_fatura = df.explode("ValorParcela")
df_fatura
# faz o que precisavamos, de separar as parcelas por linhas 
# precisamos agora alterar as datas 

# %%

df_fatura = df_fatura.drop(['Valor','Parcelas'],
                           axis=1)
# Primeiro podemos remover essas colunas
df_fatura

# %%

df_fatura["Months_add"] = (df_fatura.groupby("idTransaction")["dtTransaction"]
                                    .rank('first')
                                    .astype(int))   
# Criando uma tabela com a resposta de "Quantos meses precioso adicionar?"
df_fatura
# %%

# Pandas não suporta mais o timedelta64 com mês, então tive que usar outra função
def add_months(row):
    new_date = row["dtTransaction"] + pd.DateOffset(months = row["Months_add"])
    dt_str = new_date.strftime("%Y-%m")
    return dt_str

df_fatura["DtFatura"] = df_fatura.apply(add_months, axis=1)
df_fatura
# %%

df_fatura_mes = (df_fatura.groupby(['idCliente', 'DtFatura'])["ValorParcela"]
                          .sum()
                          .reset_index())
df_fatura_mes
# Cada cliente pode ter feito mais de uma compra, assim junta os valores das faturas
# em uma só, o quanto o cliente vai ter que pagar cada mês 
# %%
df_fatura_mes_final = (df_fatura_mes.pivot_table(columns="DtFatura",
                                          index="idCliente",
                                          values="ValorParcela")
                              .fillna(0)
                              #.reset_index() achei que ficou melhor sem 
                              )
df_fatura_mes_final
# colocar as datas em colunas, para ficar de uma visualização diferente (para o mkt)
# %%
df_fatura_mes_final.to_excel("Fatura_detalhada.xlsx")
# transforma o df em arquivo excel
# %%
