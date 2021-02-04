import pandas as pd
import plotly.express as px

def make_program_bar_chart(df, project, barmode):
    colors = px.colors.qualitative.Plotly + px.colors.qualitative.Set3

    if barmode == 'stack':
        prog_proj_subtotals = (df[df['Program Area'] == project]
                                .groupby(['Program Project', 'Year'])
                                .tail(1)[:-1])
    elif barmode == 'group':
        prog_proj_subtotals = (df[(df['Program Area'] == project) & (df['Year']!=2015)]
                                .groupby(['Program Project', 'Year'])
                                .tail(1)[:-1])

    t = prog_proj_subtotals.sort_values(by = ['Program Area', 'Program Project', 'Year'], ignore_index=True)
    fig = px.bar(t, x="Year", y="PresBud", color="Program Project", title=project + ' Budget Breakdown',
                 color_discrete_sequence=colors, barmode=barmode)

    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.1, y=-0.12,
                              xanchor='center', yanchor='top',
                              text='* 2015 Budget Breakdown Unavailable',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
    fig.update_layout(annotations=annotations,
                      yaxis_title="Amount",
                      xaxis = dict(
                        tickmode = 'linear',
                        tick0 = 2012,
                        dtick = 1),
                      height=700

    )

    fig.update_yaxes( # the y-axis is in dollars
            tickprefix="$", showgrid=True
    )
    return fig
