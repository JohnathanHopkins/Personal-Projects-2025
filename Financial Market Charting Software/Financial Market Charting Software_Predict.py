import yfinance
import plotly.graph_objects as go
from plotly.subplots import make_subplots


tsla = yfinance.Ticker('TSLA')
history = tsla.history(period='1y')

#print(history.head())


#fig = go.Figure(data=go.Scatter(x=history.index,y=history['Close'], mode='lines'))
#fig.show()


################################# Line chart

fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=history.index,y=history['Close'],name='Price'),secondary_y=False)
fig2.add_trace(go.Bar(x=history.index,y=history['Volume'],name='Volume'),secondary_y=True)


fig2.update_yaxes(range=[0,7000000000],secondary_y=True)
fig2.update_yaxes(visible=False, secondary_y=True)

#fig2.show()


################################# Candlestick chart

fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Candlestick(x=history.index,
                              open=history['Open'],
                              high=history['High'],
                              low=history['Low'],
                              close=history['Close'],
                             ))


# Volume
fig3.add_trace(go.Bar(x=history.index, y=history['Volume'], name='Volume'),secondary_y=True)
fig3.update_layout(xaxis_rangeslider_visible=False)

#Scale volume so it's not blocking price
#fig3.update_yaxes(range=[0,7000000000],secondary_y=True)
#fig3.update_yaxes(visible=False, secondary_y=True)

#fig3.show()

# Indicators

fig3.add_trace(go.Scatter(x=history.index,y=history['Close'].rolling(window=20).mean(),marker_color='blue',name='20 Day MA'))
fig3.add_trace(go.Bar(x=history.index, y=history['Volume'], name='Volume'),secondary_y=True)
fig3.update_layout(title={'text':'TSLA', 'x':0.5})
fig3.update_yaxes(range=[0,1000000000],secondary_y=True)
fig3.update_yaxes(visible=False, secondary_y=True)
fig3.update_layout(xaxis_rangeslider_visible=False)  #hide range slider

# Color based on price
history['diff'] = history['Close'] - history['Open']
history.loc[history['diff']>=0, 'color'] = 'green'
history.loc[history['diff']<0, 'color'] = 'red'

x = (history.loc[history['diff']>=0], 'color')
y = (history.loc[history['diff']<0], 'color')

#print(x)
#print((history.loc[history['diff']>=0]))
# Green
diff_more_than_zero = [history['diff']>=0]
# Red
diff_less_than_zero = [history['diff']<0]
print(diff_more_than_zero)
print(diff_less_than_zero)

# if just_diff >= 0:
#    print('Greater than 0')

# if x >= y:
#    print('greater than')
# elif x <= y:
#    print('less than')

# print(history.loc[history['diff']])
# if history.loc[history['color'] == 'red']:
#     print('red')


# fig3.update_layout(
#     updatemenus=[
#         dict(
#             type = "buttons",
#             direction = "left",
#             buttons=list([
#                 dict(
#                     args=["type", "surface"],
#                     label="Button 1",
#                     method="restyle"
#                 ),
#                 dict(
#                     args=["type", "heatmap"],
#                     label="Button 2",
#                     method="restyle"
#                 )
#             ]),
#             pad={"r": 10, "t": 10},
#             showactive=True,
#             x=0.11,
#             xanchor="left",
#             y=1.1,
#             yanchor="top"
#         ),
#     ]
# )


my_button=list(
    [
        
        dict(args=['type', 'line'], label = 'Line', method = 'restyle'),
        dict(args=['type', 'candlestick'], label = 'Candlestick', method = 'restyle')
        #dict[args=['type', 'line'],label='LinePlot', method='restyle'],
        #dict[args=['type', 'Candlestick'],label='CandleStickPlot', method='restyle']
    ]
    )

fig3.update_layout(
    updatemenus=[dict(type='buttons', buttons = my_button,direction='left')]
    )


#Scale volume so it's not blocking price
fig3.update_yaxes(range=[0,7000000000],secondary_y=True)
fig3.update_yaxes(visible=False, secondary_y=True)

fig3.update_xaxes(rangebreaks = [
                       dict(bounds=['sat','mon']), # hide weekends
                       #dict(bounds=[16, 9.5], pattern='hour'), # for hourly chart, hide non-trading hours (24hr format)
                       dict(values=["2021-12-25","2022-01-01"]) #hide Xmas and New Year
                                ])

fig3.show()