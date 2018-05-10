import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
mypath = '/artocarpus/lauren/Hybpiper/assemblies/'

def sampleList(indList): #sys.argv[2]
	"""
	sampleList creates a list out of a text file containing individuals of interest
	input indList: a list containing the individuals of interest separated by '\n'
	"""
	with open(indList, "r") as f: 
		L = [line.strip() for line in f.readlines()]
	return L

def get_genes(sampList, gene):
	geneDict = {}
	for ind in sampList:
		with open(mypath + "{}/{}/{}.contigs.fasta".format(ind,gene,gene)) as f:
			for record in SeqIO.parse(f, "fasta"):
				geneDict[ind] = (record.id, record.seq)
	print(geneDict)

def main():
	sampList = sampleList('/Users/ChristinaShehata/Desktop/artocarpus_samples.txt')
	get_genes(sampList, sys.argv[1])
	
main()