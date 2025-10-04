import dash_bootstrap_components as dbc

# ========== Estilos Globais ============ #
PLOTLY_CONFIG = {"displayModeBar": False, "showTips": False}
TEMPLATE_THEME1 = "flatly"
TEMPLATE_THEME2 = "darkly"
URL_THEME1 = dbc.themes.FLATLY
URL_THEME2 = dbc.themes.DARKLY

# Estilo para os cards do dashboard
TAB_CARD_STYLE = {"height": "100%"}

# Configuração base para os gráficos
MAIN_GRAPH_CONFIG = {
    "hovermode": "x unified",
    "legend": {
        "yanchor": "top",
        "y": 0.9,
        "xanchor": "left",
        "x": 0.1,
        "title": {"text": None},
        "font": {"color": "white"},
        "bgcolor": "rgba(0,0,0,0.5)",
    },
    "margin": {"l": 10, "r": 10, "t": 10, "b": 10},
}
