import sys
from Bio import SeqIO

####################################################################################
##
## sys.argv[1] = baits file
## sys.argv[2] = output file
##
####################################################################################

def get_genes(baits_file, outFile):
	""" makes geneList from baits file """
	with open(outFile, 'w') as f:
		records = list(SeqIO.parse(baits_file, 'fasta'))
		for record in records:
			f.write(record.id[11:]+'\n')

get_genes('/Users/ChristinaShehata/Desktop/newref_camansi.fna', '/Users/ChristinaShehata/Desktop/artGeneList.txt')


