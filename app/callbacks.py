from dash import Input, Output, html
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.express as px
import plotly.graph_objects as go

from app import app
from utils import filter_data, convert_to_text
from styles import TEMPLATE_THEME1, TEMPLATE_THEME2, MAIN_GRAPH_CONFIG

# ======== Callbacks ========== #


@app.callback(
    [
        Output("graph1", "figure"),
        Output("graph2", "figure"),
        Output("graph5", "figure"),
        Output("graph6", "figure"),
        Output("graph8", "figure"),
        Output("graph9", "figure"),
        Output("graph11", "figure"),
    ],
    [
        Input("radio-month", "value"),
        Input("radio-team", "value"),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    ],
)
def update_graphs_by_month_and_team(month, team, toggle):
    template = TEMPLATE_THEME1 if toggle else TEMPLATE_THEME2
    df_filtered = filter_data(month, team)

    # Graph 1 e 2
    df_1 = (
        df_filtered.groupby(["Equipe", "Consultor"])["Valor Pago"].sum().reset_index()
    )
    df_1 = df_1.sort_values(by="Valor Pago", ascending=False).groupby("Equipe").head(1)

    fig1 = px.bar(
        df_1,
        x="Consultor",
        y="Valor Pago",
        text="Valor Pago",
        title="Top Consultores por Equipe",
    )
    fig2 = px.pie(
        df_1,
        values="Valor Pago",
        names="Consultor",
        hole=0.6,
        title="Participação por Consultor",
    )

    # Graph 5 e 6
    df_5 = (
        df_filtered.groupby(["Consultor", "Equipe"])["Valor Pago"]
        .sum()
        .reset_index()
        .sort_values("Valor Pago", ascending=False)
    )
    df_6 = (
        df_filtered.groupby("Equipe")["Valor Pago"]
        .sum()
        .reset_index()
        .sort_values("Valor Pago", ascending=False)
    )

    fig5 = go.Figure(
        go.Indicator(
            mode="number+delta",
            title={
                "text": f"Top Consultant<br><span style='font-size:70%'>{df_5['Consultor'].iloc[0]}</span>"
            },
            value=df_5["Valor Pago"].iloc[0],
            number={"prefix": "R$"},
            delta={
                "relative": True,
                "valueformat": ".1%",
                "reference": df_5["Valor Pago"].mean(),
            },
        )
    )

    fig6 = go.Figure(
        go.Indicator(
            mode="number+delta",
            title={
                "text": f"Top Team<br><span style='font-size:70%'>{df_6['Equipe'].iloc[0]}</span>"
            },
            value=df_6["Valor Pago"].iloc[0],
            number={"prefix": "R$"},
            delta={
                "relative": True,
                "valueformat": ".1%",
                "reference": df_6["Valor Pago"].mean(),
            },
        )
    )

    # Graph 8
    df_8 = df_filtered.groupby("Equipe")["Valor Pago"].sum().reset_index()
    fig8 = px.bar(
        df_8, x="Valor Pago", y="Equipe", orientation="h", title="Vendas por Equipe"
    )

    # Graph 9
    df_9 = df_filtered.groupby("Meio de Propaganda")["Valor Pago"].sum().reset_index()
    fig9 = px.pie(df_9, values="Valor Pago", names="Meio de Propaganda", hole=0.7)

    # Graph 11
    fig11 = go.Figure(
        go.Indicator(
            mode="number",
            title={
                "text": "Valor Total<br><span style='font-size:70%'>Em Reais</span>"
            },
            value=df_filtered["Valor Pago"].sum(),
            number={"prefix": "R$"},
        )
    )

    for fig in [fig1, fig2, fig5, fig6, fig8, fig9, fig11]:
        fig.update_layout(MAIN_GRAPH_CONFIG, template=template)

    return fig1, fig2, fig5, fig6, fig8, fig9, fig11


@app.callback(
    [
        Output("graph3", "figure"),
        Output("graph4", "figure"),
        Output("graph10", "figure"),
    ],
    [
        Input("radio-team", "value"),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    ],
)
def update_graphs_by_team(team, toggle):
    template = TEMPLATE_THEME1 if toggle else TEMPLATE_THEME2
    df_filtered = filter_data(0, team)  # Usa 0 para mês para pegar o ano todo

    # Graph 3
    df_3 = df_filtered.groupby("Dia")["Chamadas Realizadas"].sum().reset_index()
    fig3 = px.line(df_3, x="Dia", y="Chamadas Realizadas", title="Chamadas por Dia")
    fig3.add_scatter(
        x=df_3["Dia"],
        y=[df_3["Chamadas Realizadas"].mean()] * len(df_3["Dia"]),
        name="Média",
        line=dict(dash="dash"),
    )

    # Graph 4
    df_4 = df_filtered.groupby("Mês")["Chamadas Realizadas"].sum().reset_index()
    fig4 = px.line(df_4, x="Mês", y="Chamadas Realizadas", title="Chamadas por Mês")
    fig4.add_scatter(
        x=df_4["Mês"],
        y=[df_4["Chamadas Realizadas"].mean()] * len(df_4["Mês"]),
        name="Média",
        line=dict(dash="dash"),
    )

    # Graph 10
    df_10 = (
        df_filtered.groupby(["Meio de Propaganda", "Mês"])["Valor Pago"]
        .sum()
        .reset_index()
    )
    fig10 = px.line(
        df_10,
        x="Mês",
        y="Valor Pago",
        color="Meio de Propaganda",
        title="Vendas por Propaganda ao longo do Mês",
    )

    for fig in [fig3, fig4, fig10]:
        fig.update_layout(MAIN_GRAPH_CONFIG, template=template)

    return fig3, fig4, fig10


# Callback para o gráfico 7, que não depende de filtros
@app.callback(
    Output("graph7", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph7(toggle):
    template = TEMPLATE_THEME1 if toggle else TEMPLATE_THEME2
    df_filtered = filter_data(0, 0)  # Sem filtros
    df_7 = df_filtered.groupby(["Mês", "Equipe"])["Valor Pago"].sum().reset_index()
    df_7_total = df_filtered.groupby("Mês")["Valor Pago"].sum().reset_index()

    fig7 = px.line(
        df_7, x="Mês", y="Valor Pago", color="Equipe", title="Vendas Mensais por Equipe"
    )
    fig7.add_scatter(
        x=df_7_total["Mês"],
        y=df_7_total["Valor Pago"],
        name="Total de Vendas",
        mode="lines+markers",
        line=dict(color="royalblue", dash="dash"),
    )
    fig7.update_layout(MAIN_GRAPH_CONFIG, template=template)

    return fig7
