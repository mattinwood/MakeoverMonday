import pandas as pd
import plotly.graph_objects as go

#%%
# Create Growth Metric
df = pd.read_csv('2021-W08/ceocomp.csv')
df['lag'] = df['realized'].shift(periods=1)
df['realized_growth'] = (df['realized'] - df['lag']) / df['lag']

#%%
# Import Inflation Data
inf = pd.read_csv('2021-W08/inflation.csv')
inf['Annual'] = inf['Annual'] / 100
# Add Recessions
inf['recession'] = 0
recession_years = [1970, 1974, 1980, 1982, 1990, 2001, 2008, 2009]  #1969, 1973-75, 1981, 1991, 2007
inf.loc[inf['Year'].isin(recession_years), 'recession'] = 1

#%%
# Charting
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['year'],
    y=df['realized_growth'],
    name='CEO Comp Growth'
))

fig.add_trace(go.Scatter(
    line={'shape': 'spline'},
    x=inf['Year'],
    y=inf['Annual'],
    name='US Inflation'
))

fig.update_layout(
    template='plotly_dark',
    yaxis_tickformat='%',
    title='Growth in CEO Compensation (relative to worker pay) vs Inflation'
)

fig.update_yaxes(tickvals=[
    -0.5, -0.4, -0.3, -0.2, -0.1, 0,
    0.05, 0.1, 0.2, 0.3, 0.4, 0.5])

fig.show()
