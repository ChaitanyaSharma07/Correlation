import pandas
import plotly.express as px
import csv

#example 1 for summer
data = pandas.read_csv("summer.csv")

fig = px.scatter(data, x="Temperature", y="Ice-cream Sales( ₹ )", color="Ice-cream Sales( ₹ )")
fig.show()

data2 = pandas.read_csv("sleep.csv")

fig2 = px.scatter(data2, x="Coffee in ml", y="sleep in hours", color="sleep in hours")
fig2.show()


#formula for correlation co-efficient

