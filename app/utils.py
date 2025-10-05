import pandas as pd

# ===== Leitura e Limpeza do Arquivo ====== #
df = pd.read_csv("dataset.csv")
df_cru = df.copy()

# Mapeamento de meses para números para otimizar memória e processamento
month_map = {
    "Jan": 1,
    "Fev": 2,
    "Mar": 3,
    "Abr": 4,
    "Mai": 5,
    "Jun": 6,
    "Jul": 7,
    "Ago": 8,
    "Set": 9,
    "Out": 10,
    "Nov": 11,
    "Dez": 12,
}
df["Mês"] = df["Mês"].map(month_map)

# Limpeza e conversão de colunas
df["Valor Pago"] = df["Valor Pago"].str.replace("R$ ", "", regex=False).astype(float)
df["Status de Pagamento"] = df["Status de Pagamento"].apply(
    lambda x: 1 if x == "Pago" else 0
)

# Convertendo tipos de dados para otimização
for col in ["Chamadas Realizadas", "Dia", "Mês", "Status de Pagamento"]:
    df[col] = df[col].astype(int)

# Criando opções para os filtros
options_month = [{"label": "Ano todo", "value": 0}] + sorted(
    [
        {"label": month, "value": num}
        for month, num in zip(df_cru["Mês"].unique(), df["Mês"].unique())
    ],
    key=lambda x: x["value"],
)

options_team = [{"label": "Todas Equipes", "value": 0}] + [
    {"label": team, "value": team} for team in df["Equipe"].unique()
]


# ========= Funções dos Filtros ========= #
def filter_data(month, team):
    """Filtra o dataframe com base no mês e na equipe."""
    df_filtered = df.copy()
    if month != 0:
        df_filtered = df_filtered[df_filtered["Mês"] == month]
    if team != 0:
        df_filtered = df_filtered[df_filtered["Equipe"] == team]
    return df_filtered
