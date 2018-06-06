import plotly
plotly.tools.set_credentials_file(username=' ', api_key='')
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
		
red = {"x": geneList,
          "y": redList,
          "marker": {"color": "red", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Red",
          "type": "scatter"
}

orange = {"x": geneList,
          "y": orangeList,
          "marker": {"color": "orange", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Orange",
          "type": "scatter",
}

light_blue = {"x": geneList,
          "y": lBlueList,
          "marker": {"color": "rgb(135, 206, 250)", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Light Blue",
          "type": "scatter",
}

dark_blue = {"x": geneList,
          "y": dBlueList,
          "marker": {"color": "blue", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Dark Blue",
          "type": "scatter",
}

purple = {"x": geneList,
          "y": purpleList,
          "marker": {"color": "purple", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Purple",
          "type": "scatter",
}

yellow = {"x": geneList,
          "y": yellowList,
          "marker": {"color": "yellow", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Yellow",
          "type": "scatter",
}

pink = {"x": geneList,
          "y": pinkList,
          "marker": {"color": "pink", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Pink",
          "type": "scatter",
}

green = {"x": geneList,
          "y": greenList,
          "marker": {"color": "green", "size": 12},
          "mode": "markers",
          "text": geneList,
          "name": "Green",
          "type": "scatter",
}

data = [orange, light_blue, dark_blue, purple, yellow, pink, green]
layout = {"title": "LSD for Artocarpus Phylogenetic Markers",
          "xaxis": {"title": "Gene", },
          "yaxis": {"title": "LSDnorm"}}


fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='LSD_artocarpus')








fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='LSD_artocarpus')