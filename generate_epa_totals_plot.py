import pandas as pd
import numpy as np
import plotly.graph_objects as go

def make_epa_totals_plot(epa_totals):
    #EPA Totals Graph
    title = 'EPA Budget'
    labels = ['FY-2 Actuals', 'Pres Budget']
    colors = ['rgb(49,130,189)', 'rgb(250,148,59)', 'rgb(67,67,67)', 'rgb(189,189,189)']

    mode_size = [8, 8]
    line_size = [2, 2]

    final_actuals = epa_totals['Actuals']
    final_presbud = epa_totals['PresBud']
    final_enacted = epa_totals['Enacted']
    final_annualized = epa_totals['Annualized_CR']

    x = epa_totals.Year.tolist()
    x_data = np.vstack((x,)*2)
    y_data = np.array([final_actuals.values, final_presbud.values])

    fig = go.Figure()

    for i in range(0, 2):
        fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
            name=labels[i],
            line=dict(color=colors[i], width=line_size[i]),
            connectgaps=False,
        ))

        # endpoints
        fig.add_trace(go.Scatter(
            x=[x_data[i][0], x_data[i][-1]],
            y=[y_data[i][0], y_data[i][-1]],
            mode='markers',
            marker=dict(color=colors[i], size=mode_size[i])
        ))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=False,
        plot_bgcolor='white',
        width=1000
    )

    annotations = []

    # Adding labels
    for y_trace, label, color in zip(y_data, labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[9],
                                      xanchor='right', yanchor='middle',
                                      text=label + '\n' + '{}B'.format(round(y_trace[9]/1e9, ndigits=2)),
                                      font=dict(family='Arial',
                                                size=16),
                                      showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[0],
                                      xanchor='left', yanchor='middle',
                                      text='{}B'.format(round(y_trace[0]/1e9, ndigits=2)),
                                      font=dict(family='Arial',
                                                size=16),
                                      showarrow=False))
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                  xanchor='left', yanchor='bottom',
                                  text=title,
                                  font=dict(family='Arial',
                                            size=30,
                                            color='rgb(37,37,37)'),
                                  showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                                  xanchor='center', yanchor='top',
                                  text='Source: epa.gov',
                                  font=dict(family='Arial',
                                            size=12,
                                            color='rgb(150,150,150)'),
                                  showarrow=False))

    fig.update_layout(annotations=annotations, autosize=False,
        width=1000,
        height=550,
        margin=dict(
            l=100,
            r=50,
            b=100,
            t=100,
            pad=4))

    return fig
