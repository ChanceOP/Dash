from dash import Dash, html
import pandas as pd

from . import bar_chart, pie_chart, year_dropdown, month_dropdown, category_dropdown
from ..data. source import DataSource

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, source),
                    month_dropdown.render(app, source),
                    category_dropdown.render(app, source),
                ],
            ),
            bar_chart.render(app, source),
            pie_chart.render(app, source),
        ],
    )
