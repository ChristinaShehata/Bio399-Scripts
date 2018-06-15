import sys

paml_results_directory = '/Users/ChristinaShehata/Desktop/PAML_results_modelA1/'
omega_list = []

def geneList():
	with open('/Users/ChristinaShehata/Desktop/artGeneList.txt', 'r') as f:
		genes = [line.strip() for line in f.readlines()]
		return genes

def parsePAML(genes):
	for gene in genes:
		with open(paml_results_directory + '{}.paml'.format(gene)) as f:
			read = f.readlines()
			for line in read:
				if line.startswith('Model'):
					x = line.split(' ')
					omega_list.append(x[-2])

def main():
	genes = geneList()
	parsePAML(genes)
	print(omega_list)

main() #works with ModelA1 files
			

