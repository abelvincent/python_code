import plotly
import plotly.express as px
fig=px.choropleth(locationmode = "USA-states",color=[1],scope="usa")
fig.show()
