import pandas
import plotly.express as px

def make_program_area_line_plot(program_area_totals):
    trace1 = px.line(program_area_totals, x="Year", y="PresBud",
                     color="Program Area", title="Budget by Program Area")

    fig = px.line(program_area_totals, x="Year", y="Actuals",
                  color="Program Area", title="Budget by Program Area")
    fig.update_traces(line = dict(dash='dot'))
    fig.add_trace(trace1.data[0])
    fig.add_trace(trace1.data[1])
    fig.add_trace(trace1.data[2])
    fig.add_trace(trace1.data[3])
    fig.add_trace(trace1.data[4])
    fig.add_trace(trace1.data[5])
    fig.add_trace(trace1.data[6])
    fig.add_trace(trace1.data[7])
    fig.add_trace(trace1.data[8])
    fig.add_trace(trace1.data[9])

    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.12, y=1.05,
                                  xanchor='center', yanchor='top',
                                  text='- - - -  FY-2 Actuals,   ____ Pres Budget',
                                  font=dict(family='Arial',
                                            size=12,
                                            color='rgb(150,150,150)'),
                                  showarrow=False))

    fig.update_layout(
        annotations=annotations,
        title="Budget by Program Area",
        xaxis_title="Year",
        yaxis_title="Amount",
        legend_title="Program Area",
        height=700,
        width=1250
    )


    fig.update_yaxes( # the y-axis is in dollars
        tickprefix="$", showgrid=True
    )

    return fig
