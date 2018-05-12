# coding: utf-8
import sys
from Bio import SeqIO
mypath = '/Users/ChristinaShehata/Desktop/assemblies/' #path to assemblies
#mypath = '/artocarpus/lauren/Hybpiper/assemblies/'

def sampleList(indList):
	"""
	sampleList creates a list out of a text file containing individuals of interest
	input indList: a list containing the individuals of interest separated by '\n'
	"""
	with open(indList, "r") as f: 
		L = [line.strip() for line in f.readlines()]
	return L

def get_genes(sampList, gene):
	""" get_genes opens up folders for individuals of interest and parses for
	a particular gene of interest
	input sampList: list of individuals of interest
	input gene: gene of interest
	"""
	geneDict = {}
	for ind in sampList:
		with open(mypath + "{}/{}/{}_contigs.fasta".format(ind,gene,gene), 'r') as f:
			records = list(SeqIO.parse(f, "fasta"))
			geneDict[ind] = ('> ' + ind, records[0].seq) #assuming 1st node?
	return geneDict

def write(geneDict, outFile):
	""" writes gene sequences for each individual into one fasta file
	input geneDict: dictionary of each individual's sequence for a particular gene
	input outFile: output fasta file
	"""
	with open(outFile, 'w') as f:
		for id, seq in geneDict.items():
			f.write(seq[0] +'\n')
			f.write(str(seq[1]) + '\n')

def main():
	sampList = sampleList(sys.argv[2])
	geneDict = get_genes(sampList, sys.argv[1])
	write(geneDict, sys.argv[3])
	
main()