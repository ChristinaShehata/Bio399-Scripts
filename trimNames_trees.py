import sys
from Bio import Phylo

####################################################################################
##
## Files Needed:
## sys.argv[1] = gene list
## sys.argv[2] = directory of trees with full names (also output directory)
##
####################################################################################

def allGenes(geneL):
	""" makes master gene List """
	with open(geneL, 'r') as f:
		geneList = [line.rstrip() for line in f.readlines()]
	return geneList

def sample_dict(gene, input):
	sampleDict = {}
	recordList = []
	tree = Phylo.read(input + 'RAxML_bestTree.{}.tree'.format(gene), "newick")
	for ind in tree.get_terminals():
		if ind.name == "A_altilisxA_marianennsis_15":
			sampleDict[ind.name] = 'A_altxA_marmarianennsis_15'
		elif len(ind.name) >= 30:
			sampleDict[ind.name] = 'A_altxA_mar' + ind.name[-15:]
		else:
			sampleDict[ind.name] = ind.name
	return sampleDict

def rename(sampleDict, gene, input):
	with open(input + 'RAxML_bestTree.{}.tree'.format(gene), 'r') as f:
		with open(input + 'RAxML_bestTree.{}.tree.short'.format(gene), 'w') as q:
			read = f.read()
			for long, short in sampleDict.items():
				if long in read:
					read = read.replace(long, short)
			q.write(read)

def main():
	geneList = allGenes(sys.argv[1])	
	for gene in geneList:
		sampleDict = sample_dict(gene, sys.argv[2])
		rename(sampleDict, gene, sys.argv[2])

main()

"""
python /data/cshehata/python/trimNames_trees.py /data/cshehata/Artocarpus/artGeneList.txt /data/cshehata/Artocarpus/PAML/bestTree/
"""

def local():
	geneList = allGenes('/Users/ChristinaShehata/Desktop/Artocarpus_LSD/artGeneList.txt')
	for gene in geneList:
		sampleDict = sample_dict(gene, '/Users/ChristinaShehata/Downloads/bestTree/')
		rename(sampleDict, gene, '/Users/ChristinaShehata/Downloads/bestTree/')

#local()