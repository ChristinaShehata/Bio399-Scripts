import sys

######################################################################
## 
## Files needed:
## sys.argv[1] is text file containing gene list
## sys.argv[2] is path to directory containing output PAML files
## sys.argv[3] is output file
##
######################################################################

def geneList(geneText):
	""" makes a list of genes """
	with open(geneText, 'r') as f:
		genes = [line.strip() for line in f.readlines()]
		return genes

def parsePAML(genes, paml_results_directory):
	""" parses through PAML output to get omega
	input genes: list of genes
	"""
	omega_list = []
	for gene in genes:
		with open(paml_results_directory + '{}.paml'.format(gene)) as f:
			read = f.readlines()
			for line in read:
				if line.startswith('Model'):
					x = line.split(' ')
					omega_list.append((gene, x[-2]))
	return omega_list

def write(omega_list, outFile):
	""" write results to a text file """
	with open(outFile, 'w') as f:
		for x in omega_list:
			f.write(x[0] + '\t' + x[1])
			f.write('\n')

def main():
	genes = geneList(sys.argv[1])
	omega_list = parsePAML(genes, sys.argv[2])
	write(omega_list, sys.argv[3])

main() #works with ModelA1 files
			

