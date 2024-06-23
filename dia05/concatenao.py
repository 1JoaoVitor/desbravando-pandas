# %%
import pandas as pd
import os #biblioteca pra mexer nas pastas (operating system)

def import_etl(path:str): # cria uma função para ler todos os arquivos

    name = path.split("/")[-1].split(".")[0] #pega o endereço do arquivo e retira só o nome principal

    df = (pd.read_csv(path, sep=';') 
            .rename(columns={"valor":name})  #renomeia a coluna de valor para o nome principal que foi pego
            .set_index(["cod","nome","período"])) # coloca essas colunas como index (para concatenar de boa)
    
    return df # retorna o df

# %%

path = "../data/ipea/" # essa é a pasta que vai pegar os arquivos
files = os.listdir(path) # lista todos os aquivos na pasta path

dfs = []
for i in files:
    dfs.append(import_etl(path+i)) #caminho total, pasta + nome do arquivo
#pega todos os arquivos, usa a função que criamos para 
#retornar os df prontos de cada arquivo, colocando todos dentro da lista dfs
df_consolidado = pd.concat(dfs, axis=1).reset_index()
# faz o concat numa lista de df, no caso a lista dfs
df_consolidado.to_csv("../data/bia_consolidado.csv", sep=";", index=False)
#transforma o df em arquivo csv 