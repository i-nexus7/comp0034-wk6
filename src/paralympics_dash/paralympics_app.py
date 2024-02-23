from dash import Dash, html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.VAPOR]

meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
]

app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

app.layout = dbc.Container([
    html.H1('Hello World'),
    html.Div([
        html.P('This is a simple Dash web application.'),
        html.P('It is a single page with a title and a paragraph.'),
        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), style={'width': '100%'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
