# Sales Analytics Dashboard

Este é um dashboard interativo para análise de performance de vendas, desenvolvido com Dash e Plotly. A aplicação permite visualizar métricas de vendas, filtrar dados por equipe e por período, e analisar o desempenho de consultores e o retorno de diferentes meios de propaganda.

---

## ✨ Funcionalidades

-   **Visualização Interativa:** Gráficos que se atualizam dinamicamente com base nos filtros selecionados.
-   **Filtros Dinâmicos:** Filtre os dados por Mês ou por Equipe para análises específicas.
-   **Análise de Performance:** Indicadores de topo para o melhor consultor e a melhor equipe.
-   **Análise de Vendas:** Acompanhe o total de vendas, distribuição por propaganda e performance mensal.
-   **Tema Claro/Escuro:** Alterne entre os temas para melhor conforto visual.
-   **Design Responsivo:** O layout se adapta a diferentes tamanhos de tela.

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

-   **Python:** Linguagem de programação principal.
-   **Dash:** Framework para a construção da aplicação web.
-   **Dash Bootstrap Components:** Para criar layouts responsivos e utilizar componentes de Bootstrap.
-   **Plotly Express:** Para a criação dos gráficos interativos.
-   **Pandas:** Para manipulação e análise dos dados.

---

## 📦 Como Executar o Projeto

Siga os passos abaixo para executar a aplicação localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/christianduhp/sales-analysis.git](https://github.com/christianduhp/sales-analysis.git)
    cd sales_analysis
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    *Crie um arquivo `requirements.txt` com o conteúdo abaixo e execute o comando:*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

5.  Acesse o dashboard no seu navegador através do endereço: `http://127.0.0.1:8050/`

**Arquivo `requirements.txt`:**
```txt
dash
dash-bootstrap-components
dash-bootstrap-templates
plotly
pandas
```

---

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
├── app/
│   ├── __init__.py      # Inicialização da aplicação Dash.
│   ├── layouts.py       # Define a estrutura visual e o layout do dashboard.
│   └── callbacks.py     # Contém a lógica de interatividade dos componentes.
├── .gitignore           # Especifica os arquivos a serem ignorados pelo Git.
├── dataset.csv          # Conjunto de dados utilizado na análise.
├── main.py              # Ponto de entrada para executar a aplicação.
├── README.md            # Documentação do projeto.
├── requirements.txt     # Lista de dependências Python.
└── styles.py            # Variáveis de estilo e configurações dos gráficos.
```

