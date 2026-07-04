import pandas as pd
import os

def carregar_dados(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".csv")]
    
    dfs = []
    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        

        df = pd.read_csv(caminho, sep=";")
        
        df = filtrar_cafe(df)
        df = filtrar_santos(df)
        df = converter_sacas(df)
        
        dfs.append(df)
        

    return pd.concat(dfs, ignore_index=True)

def filtrar_cafe(df):
    ncm_str = df["CO_NCM"].astype(str).str.strip()
    condicao_zero = ncm_str.str.startswith("0901")
    condicao_sem_zero = ncm_str.str.startswith("901") & (ncm_str.str.len() == 7)
    return df[condicao_zero | condicao_sem_zero]


def converter_sacas(df):
    df = df.copy()
    df["Sacas"] = df["KG_LIQUIDO"] / 60
    return df

def filtrar_santos(df):
    df["CO_URF"] = df["CO_URF"].astype(str).str.strip()
    return df[df["CO_URF"].isin(["0817800", "817800"])]