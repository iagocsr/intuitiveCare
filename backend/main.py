import os
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

# Permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho correto para carregar o CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório do backend
CSV_PATH = os.path.join(BASE_DIR, "../Relatorio_cadop.csv")  # Volta um nível e pega o CSV

# Verifica se o arquivo existe antes de carregar
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Arquivo não encontrado: {CSV_PATH}")

df = pd.read_csv(CSV_PATH, delimiter=';', dtype=str)

def tratar_nan(df):
    """ Substitui valores NaN por None em todo o DataFrame. """
    return df.where(pd.notna(df), None)

def buscar_operadoras(query: str):
    """ Filtra as operadoras que contêm o termo de busca no nome. """
    resultado = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
    
    # Trata os NaN no resultado
    resultado = tratar_nan(resultado)
    
    return resultado.to_dict(orient="records")

@app.get("/buscar")
def buscar_operadora(nome: str = Query(..., description="Nome da operadora")):
    resultados = buscar_operadoras(nome)
    return {"resultados": resultados}

#print(buscar_operadoras("elias"))
