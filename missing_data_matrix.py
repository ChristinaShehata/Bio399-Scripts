import sys
from Bio import SeqIO
import pandas as pd
import csv

####################################################################################
##
## Files Needed:
## sys.argv[1] = list of all samples
## sys.argv[2] = list of all genes
## sys.argv[3] = path to directory containing trimmed alignments
## sys.argv[4] = output csv file
##
####################################################################################

def allSamples(sampleFile):
	""" gets sample list """
	with open(sampleFile, 'r') as f:
		sampleList = [line.rstrip() for line in f.readlines()]
	return sampleList

def allGenes(geneFile):
	""" gets gene List """
	with open(geneFile, 'r') as f:
		geneList = [line.rstrip() for line in f.readlines()]
	return geneList

def make_matrixDict(directory, sampleList, gene):
	""" makes dictionary containing matrix info - whether a sample is represented in
	the gene sequences or not
	"""
	matrixDict = {}
	recordList = []
	matrixList = []
	fileList = []
	with open(directory + "{}.trimmed.FNA".format(gene), 'r') as f:
		for sample in sampleList:
			for record in SeqIO.parse(f, "fasta"):
				recordList.append(record.id)
			if sample in recordList:
				matrixList.append(1)
			else:
				matrixList.append(0)
	matrixDict[gene] = matrixList
	return matrixDict

def pandas_dataframe(matrixDict):
	""" makes pandas dataframe out of dictionary """
	df = pd.DataFrame(data=matrixDict)
	return df

def make_csv(df, outFile):
	""" writes pandas dataframe to csv """
	df.to_csv(outFile, sep=',', encoding='utf-8')

def main():
	matrixDict_list = []
	sampleList = allSamples(sys.argv[1])
	geneList = allGenes(geneFile)
	for gene in geneList:
		matrixDict = make_matrixDict(sys.argv[3], sampleList, gene)
		matrixDict_list.append(matrixDict)
	finalDict = {key:value for d in matrixDict_list for key, value in d.items()}
	df = pd.DataFrame(data=finalDict)
	df['Sample'] = sampleList
	make_csv(df, sys.argv[4])

main()
	


