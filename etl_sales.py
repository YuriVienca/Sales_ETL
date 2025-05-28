# -*- coding: utf-8 -*-
"""
Script para limpeza e pré-processamento de dados de vendas

"""

import pandas as pd
import numpy as np
import sqlite3

def main():
    
    caminho_entrada = "coffee_sales.csv"
    caminho_saida = "sales_cleaned.csv"
    
    df = carrega_dados(caminho_entrada)
    df = remove_duplicatas(df)
    df = substitui_invalidos(df, ["UNKNOWN", "ERROR"])
    df = converte_dados(df)
    df = remove_linhas_invalidas(df, ['Item', 'Quantity', 'Price Per Unit', 'Transaction Date'])
    df = padroniza_texto(df, ['Item', 'Payment Method', 'Location'])
    df = adiciona_colunas_temporais(df)
    salva_dados(df, caminho_saida, caminho_banco="vendas.db", nome_tabela="vendas_limpo")
    
    print("Limpeza concluída")

def carrega_dados(caminho_arquivo): 
    """Carrega os dados a partir de um arquivo CSV, tratando strings nulas como NaN."""
    
    df = pd.read_csv(caminho_arquivo, na_values=['', 'NaN', 'nan'])
    return df


def remove_duplicatas(df):
    """ Remove linhas duplicadas exatas do DataFrame."""
    
    df_limpo = df.drop_duplicates()
    return df_limpo


def substitui_invalidos(df, valores_invalidos):
    """Substitui valores inválidos especificados por NaN."""

    df_corrigido = df.replace(valores_invalidos, np.nan)
    return df_corrigido


def converte_dados(df):
    """
    Converte colunas específicas para os tipos corretos:
    - 'Transaction Date' para datetime
    - Colunas numéricas para float
    """
    
    if 'Transaction Date' in df.columns:
        df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

    colunas_numericas = ['Quantity', 'Price Per Unit', 'Total Spent']
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def remove_linhas_invalidas(df, colunas_essenciais):
    """ Remove linhas com valores nulos em colunas essenciais."""
    
    colunas_presentes = [col for col in colunas_essenciais if col in df.columns]
    df_sem_nan = df.dropna(subset=colunas_presentes)
    return df_sem_nan


def padroniza_texto(df, colunas):
    """Padroniza o texto das colunas, aplicando strip e title case."""
    
    for coluna in colunas:
        if coluna in df.columns:
            df[coluna] = df[coluna].astype(str).str.strip().str.title()
    return df

def adiciona_colunas_temporais(df):
    """Adiciona as colunas de mês e dia da semana para facilitar as análises"""
    
    if 'Transaction Date' in df.columns:
        df['Month'] = df['Transaction Date'].dt.month_name()
        df['Day of The Week'] = df['Transaction Date'].dt.day_name()
    return df

def salva_dados(df, caminho_saida_csv, caminho_banco="vendas.db", nome_tabela="vendas_limpo"):
    """
    Salva o DataFrame limpo em um arquivo CSV e em um banco SQLite.
    """
    
    df.to_csv(caminho_saida_csv, index=False)
    
    
    conn = sqlite3.connect(caminho_banco)
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
    conn.close()
    
    
main()
