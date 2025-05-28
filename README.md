# ☕ Limpeza e Pré-processamento de Dados de Vendas de Café

Este projeto tem como objetivo automatizar a limpeza, padronização e transformação de um conjunto de dados de vendas de café, permitindo sua posterior análise ou armazenamento em banco de dados. O script processa os dados brutos e os exporta para um novo arquivo `.csv` e para um banco SQLite.

---

## 📂 Estrutura do Projeto

```
├── coffee_sales.csv        # Arquivo de entrada
├── sales_cleaned.csv       # Arquivo limpo gerado após o processamento
├── vendas.db               # Banco de dados SQLite com a tabela limpa (opcional)
├── etl_sales.py            # Script principal de pré-processamento
└── README.md               # Este arquivo
```

---

## ⚙️ Funcionalidades

- ✅ Carregamento de dados CSV
- 🔁 Remoção de duplicatas
- 🚫 Substituição de valores inválidos
- 🔢 Conversão de colunas para tipos apropriados (datetime, float)
- 🧹 Eliminação de linhas incompletas
- 🧽 Padronização de texto (strip + title case)
- 📆 Criação de colunas temporais: mês e dia da semana
- 💾 Exportação para CSV e banco de dados SQLite

---

## 🚀 Como Usar

### 1. Instale as dependências:
```bash
pip install pandas numpy
```

### 2. Execute o script:
```bash
python etl_sales.py
```

O script irá gerar:
- `sales_cleaned.csv`: dados limpos
- `vendas.db`: banco SQLite com a tabela `vendas_limpo`
---

## 📊 Exemplo de análise futura

Após o pré-processamento, os dados estão prontos para serem usados em dashboards, relatórios, ou análises com ferramentas como Power BI, Tableau, Jupyter Notebooks etc.

---


## 👤 Autor

Desenvolvido por Yuri Encarnação 👋
