import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash import dcc
from dash import html
import pandas as pd
import dash_auth


VALID_USERNAME_PASSWORD_PAIRS = {
    'Mundia': '1234'
}
df = pd.read_csv("5000000 BT Records.csv")

df[' index'] = range(1, len(df) + 1)

app = dash.Dash(__name__)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

PAGE_SIZE = 10
app.layout = dash_table.DataTable(
    id='datatable-paging',
    columns=[
        {"name": i, "id": i} for i in sorted(df.columns)
    ],
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom'
)

@app.callback(
    Output('datatable-paging', 'data'),
    Input('datatable-paging', "page_current"),
    Input('datatable-paging', "page_size"))

def update_table(page_current,page_size):
    return df.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)


