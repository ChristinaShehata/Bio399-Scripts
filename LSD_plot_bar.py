import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv

geneList = []
redList = []
orangeList = []
lBlueList = []
dBlueList = []
purpleList = []
yellowList = []
pinkList = []
greenList = []

with open('/Users/ChristinaShehata/Desktop/artocarpus_LSD(060418).csv', 'rt', encoding="utf-8") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		geneList.append(row['\ufeffGene'])
		redList.append(row['Red'])
		orangeList.append(row['Orange'])
		lBlueList.append(row['Light Blue'])
		dBlueList.append(row['Dark Blue'])
		purpleList.append(row['Purple'])
		yellowList.append(row['Yellow'])
		pinkList.append(row['Pink'])
		greenList.append(row['Green'])

orange = go.Bar(x=geneList, y=orangeList, text=geneList, marker=dict(color='orange', line = dict(color= 'orange', width=1.5)),opacity=0.6)
lBlue = go.Bar(x=geneList, y=lBlueList, text=geneList, marker=dict(color='rgb(135, 206, 250)', line = dict(color= 'rgb(135, 206, 250)', width=1.5)),opacity=0.6)
dBlue = go.Bar(x=geneList, y=dBlueList, text=geneList, marker=dict(color='blue', line = dict(color= 'blue', width=1.5)),opacity=0.6)
purple = go.Bar(x=geneList, y=purpleList, text=geneList, marker=dict(color='purple', line = dict(color= 'purple', width=1.5)),opacity=0.6)
yellow = go.Bar(x=geneList, y=yellowList, text=geneList, marker=dict(color='yellow', line = dict(color= 'yellow', width=1.5)),opacity=0.6)
pink = go.Bar(x=geneList, y=pinkList, text=geneList, marker=dict(color='pink', line = dict(color= 'pink', width=1.5)),opacity=0.6)
green = go.Bar(x=geneList, y=greenList, text=geneList, marker=dict(color='green', line = dict(color= 'green', width=1.5)),opacity=0.6)

data = [orange, lBlue, dBlue, purple, yellow, pink, green]
layout = {"title": "LSD for Artocarpus Phylogenetic Markers",
          "xaxis": {"title": "Gene", },
          "yaxis": {"title": "LSDnorm"}}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='LSD_artocarpus_bar')
