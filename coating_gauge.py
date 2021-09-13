#!/usr/bin/env python
# coding: utf-8

# In[17]:


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


# In[18]:


cg= pd.read_csv("cgl2-edited.csv")
cg.columns
cg.head


# In[19]:


length =cg.LENGTH
tcg=cg.T_CG_COAT
bcg=cg.B_CG_COAT


# In[20]:


trace0 = go.Box(
    y= length,
    name= 'length'
)
trace1 =go.Box(
    y= tcg,
    name= 'coating weight-top'
)
trace2 =go.Box(
    y= bcg,
    name= 'Coating weight-bottom'
)


# In[21]:


data = [trace0,trace1,trace2]
layout = go.Layout(title = 'COATING GAUGE')


# In[24]:


fig = go.Figure(data = data,layout = layout)


# In[ ]:





# In[25]:


py.plot(fig, filename='boxplot2')


# In[ ]:




