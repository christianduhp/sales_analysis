from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

from app import app
from app.styles import (
    PLOTLY_CONFIG,
    URL_THEME1,
    URL_THEME2,
)
from app.utils import options_month, options_team


# Componente da Barra Lateral (Sidebar)
sidebar = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Sales Analytics", className="text-primary"),
                html.Hr(),
                html.P(
                    "Análise de Vendas por Equipe e Consultor", className="text-info"
                ),
                # Controles de Filtro
                html.H5("Filtros"),
                dbc.Label("Mês:"),
                dbc.RadioItems(
                    id="radio-month",
                    options=options_month,
                    value=0,
                    labelCheckedClassName="text-success",
                    inputCheckedClassName="border border-success bg-success",
                ),
                html.Br(),
                dbc.Label("Equipe:"),
                dbc.RadioItems(
                    id="radio-team",
                    options=options_team,
                    value=0,
                    labelCheckedClassName="text-warning",
                    inputCheckedClassName="border border-warning bg-warning",
                ),
                html.Hr(),
                # Controles de Tema e Informações Adicionais
                ThemeSwitchAIO(aio_id="theme", themes=[URL_THEME1, URL_THEME2]),
            ]
        )
    ],
    style={"height": "100vh", "position": "fixed", "width": "18rem"},
)

# Conteúdo Principal do Dashboard
content = html.Div(
    [
        # Linha 1: Indicadores e Gráficos de Topo
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(id="graph5", config=PLOTLY_CONFIG)), md=4),
                dbc.Col(dbc.Card(dcc.Graph(id="graph6", config=PLOTLY_CONFIG)), md=4),
                dbc.Col(dbc.Card(dcc.Graph(id="graph11", config=PLOTLY_CONFIG)), md=4),
            ],
            className="g-2 my-auto",
        ),
        # Linha 2: Gráficos de Barras e Pizza
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Top Consultores por Equipe"),
                            dbc.CardBody(dcc.Graph(id="graph1", config=PLOTLY_CONFIG)),
                        ]
                    ),
                    md=8,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Performance dos Consultores"),
                            dbc.CardBody(dcc.Graph(id="graph2", config=PLOTLY_CONFIG)),
                        ]
                    ),
                    md=4,
                ),
            ],
            className="g-2 my-auto mt-2",
        ),
        # Linha 3: Gráficos de Linha e Distribuição
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(id="graph7", config=PLOTLY_CONFIG)), md=8),
                dbc.Col(dbc.Card(dcc.Graph(id="graph8", config=PLOTLY_CONFIG)), md=4),
            ],
            className="g-2 my-auto mt-2",
        ),
        # Linha 4: Gráficos de Propaganda
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Distribuição de Propaganda"),
                            dbc.CardBody(dcc.Graph(id="graph9", config=PLOTLY_CONFIG)),
                        ]
                    ),
                    md=4,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Valores de Propaganda por Mês"),
                            dbc.CardBody(dcc.Graph(id="graph10", config=PLOTLY_CONFIG)),
                        ]
                    ),
                    md=8,
                ),
            ],
            className="g-2 my-auto mt-2",
        ),
        # Linha 5: Gráficos de Chamadas
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(id="graph3", config=PLOTLY_CONFIG)), md=6),
                dbc.Col(dbc.Card(dcc.Graph(id="graph4", config=PLOTLY_CONFIG)), md=6),
            ],
            className="g-2 my-auto mt-2",
        ),
    ],
    style={"margin-left": "19rem", "padding": "1rem"},
)

app.layout = dbc.Container(
    [
        sidebar,
        content,
    ],
    fluid=True,
)
