import sys
import csv
from Bio import SeqIO
from Bio import Phylo

####################################################################################
##
## Files Needed:
## sys.argv[1] = list of all genes
## sys.argv[2] = csv containing tree information for population file
## sys.argv[3] = path to directory containing gene trees
## sys.argv[4] = path to directory containing output population files
## sys.argv[5] = number of branches to test
## sys.argv[6] = output n File (number of taxa per gene tree)
##
####################################################################################

def allGenes(geneFile):
	""" makes master gene List """
	with open(geneFile, 'r') as f:
		geneList = [line.rstrip() for line in f.readlines()]
	return geneList

def master_pop(inFile):
	""" makes dictionary of all population information for each individual """
	master_popDict = {}
	with open(inFile, 'r', encoding="utf-8") as input:
		reader = csv.reader(input)
		for record in reader:
			master_popDict[record[0].replace('\ufeff', '')] = record
	for value in master_popDict.values():
		for i in range(len(value)):
			if value[i] == '0': value[i] = '00'
	return master_popDict
	
def ind_geneDict_tree(gene, myPath):
	""" makes a dictionary containing the individuals represented in each gene file from
	gene trees
	"""
	ind_geneDict = {}
	recordList = []
	tree = Phylo.read(myPath + 'RAxML_bestTree.{}.tree'.format(gene), "newick")
	for ind in tree.get_terminals():
		recordList.append(ind.name)
	ind_geneDict[gene] = recordList
	return ind_geneDict
		
def write_popFile(master_popDict, indGeneDict, gene, branches, outFile):
	""" writes population file """
	with open(outFile, 'w') as f:
		for i in range(int(branches) + 1):
			for ind in master_popDict:
				if ind in indGeneDict[gene]:
					f.write(master_popDict[ind][i].replace('\ufeff', '') + '\t')
			f.write('\n')

def write_nFile(indGeneDict, outFile):
	with open(outFile, 'w') as f:
		for value in indGeneDict.values():
			f.write(str(len(value)) + '\n')

def main():
	branches = sys.argv[5]
	dictList = []
	geneList = allGenes(sys.argv[1])
	master_popDict = master_pop(sys.argv[2])
	for gene in geneList:
		dictList.append(ind_geneDict_tree(gene, sys.argv[3]))
	indGeneDict = {k: v for d in dictList for k, v in d.items()}
	for gene in geneList:
		write_popFile(master_popDict, indGeneDict, gene, branches, sys.argv[4]+'{}.pops'.format(gene))
	write_nFile(indGeneDict, sys.argv[6])
	
main()







			