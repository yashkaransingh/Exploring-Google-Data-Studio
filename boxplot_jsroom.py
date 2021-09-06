
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly as pyo
import plotly.graph_objects as go
import plotly.express as px
import json
from flask import Flask,request,render_template,Response

jsrweather=pd.read_csv("jsrdata.csv")

plt.boxplot(jsrweather.field3)

plt.boxplot(jsrweather.field2)

app = Flask(__name__)

light = jsrweather.field1
humidity = jsrweather.field2
temp = jsrweather.field3

trace0 = go.Box(
    y = light,
    name = 'Light intensity indoors'
)
trace1 =go.Box(
    y = humidity,
    name = 'Humidity(rH)'
)
trace2=go.Box(
    y= temp,
    name = 'Temp(C)'
)
data = [trace0,trace1,trace2]
layout = go.Layout(title = 'ambient status')
fig = go.Figure(data = data,layout = layout)
#graphJSON = json.dumps(fig, cls-plotly.utils.PlotlyJSONEncoder)
#return render_template('index.html',graphJSON=graphJSON)

