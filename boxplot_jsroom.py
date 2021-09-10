#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

username ='yashkaransingh'
api_key='sTvu3qg24uYodX2dC47M'
#set credentials to import to plotly
chart_studio.tools.set_credentials_file(username= username, api_key= api_key)
chart_studio.tools.set_config_file(sharing='public')




# In[2]:


jsrweather=pd.read_csv("jsrdata.csv")


# In[3]:


jsrweather.columns
jsrweather.head


# In[4]:


light = jsrweather.field1
humidity = jsrweather.field2
temp = jsrweather.field3


# In[5]:


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


# In[8]:


data = [trace0,trace1,trace2]
layout = go.Layout(title = 'ambient status')
fig = go.Figure(data = data,layout = layout)


# In[9]:


py.plot(fig, filename='boxplot1')


# In[ ]:




