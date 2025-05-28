# ☕ Limpeza e Pré-processamento de Dados de Vendas de Café

Este projeto tem como objetivo automatizar a limpeza, padronização e transformação de um conjunto de dados de vendas de café, permitindo sua posterior análise ou armazenamento em banco de dados. O script processa os dados brutos e os exporta para um novo arquivo `.csv` e para um banco SQLite.

---

## 📂 Estrutura do Projeto

```
├── coffee_sales.csv        # Arquivo de entrada (não incluído no repositório)
├── sales_cleaned.csv               # Arquivo limpo gerado após o processamento
├── vendas.db               # Banco de dados SQLite com a tabela limpa (opcional)
├── etl_sales.py        # Script principal de pré-processamento
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
- 📆 Extração de colunas temporais: mês e dia da semana
- 💾 Exportação para CSV e banco de dados SQLite

---

## 🚀 Como Usar

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as dependências:
```bash
pip install pandas numpy
```

### 3. Adicione o arquivo `coffee_sales.csv` ao diretório raiz do projeto.

### 4. Execute o script:
```bash
python processamento.py
```

O script irá gerar:
- `saida.csv`: dados limpos
- `vendas.db`: banco SQLite com a tabela `vendas_limpo`

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- pandas
- numpy
- sqlite3 (biblioteca padrão do Python)

---

## 📊 Exemplo de análise futura

Após o pré-processamento, os dados estão prontos para serem usados em dashboards, relatórios, ou análises com ferramentas como Power BI, Tableau, Jupyter Notebooks etc.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

Desenvolvido por [Seu Nome](https://github.com/seu-usuario) 👋
