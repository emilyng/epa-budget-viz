import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_pickle('epa_budget.pkl')
program_area_totals = df.groupby(['Program Area', 'Year']).tail(1)[:-1]
program_areas = program_area_totals['Program Area'].unique()

def make_epa_total_pie(program_area_totals, year):
    df_year = program_area_totals[program_area_totals['Year'] == year]
    fig = px.pie(df_year, values='PresBud', names='Program Area', hole=0.3,
                  title=str(year) + ' Pres Budget Breakdown')
    fig.update_traces(textposition='auto', textfont_size=12,
                       texttemplate = "%{value:$,s} <br>(%{percent})")
    fig.update_layout(showlegend=True, height=650)
    #fig.show()
    #py.plot(fig1, filename=str(year)+' epa_presbud_brea.html', auto_open=False)
    return fig
