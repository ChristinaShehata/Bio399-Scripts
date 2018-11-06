import sys
from Bio import SeqIO
from Bio import Phylo

####################################################################################
##
## Files Needed:
## sys.argv[1] = fasta with full names
## sys.argv[2] = fasta with abbreviated names
##
####################################################################################

def trimName(fasta):
	""" cuts down sample names to convert into phylip format
	input fasta: fasta file of trimmed alignments
	"""
	newDict = {}
	with open(fasta, 'r') as f:
		records = list(SeqIO.parse(f, "fasta"))
		for record in records:
			if 'A_altilisx' in record.id:
				newDict['A_altxA_mar'+record.id[-15:]] = record.seq
			else:
				newDict[record.id] = record.seq	
	return newDict

def write(newDict, cutFasta):
	""" writes trimmed names and sequences """
	with open(cutFasta, 'w') as f:
		for id, seq in newDict.items():
			f.write('>'+id+'\n')
			f.write(str(seq) + '\n')

def main():
	newDict = trimName(sys.argv[1])
	write(newDict, sys.argv[2])
	
main()

"""
parallel -j6 "python /data/cshehata/python/trimNames_fasta.py /data/cshehata/Artocarpus/PAML/trimmed_inframe/{}.trimmed.FNA /data/cshehata/Artocarpus/PAML/trimmed_inframe/{}.trimmed.FNA.short" :::: /data/cshehata/Artocarpus/artGeneList.txt
"""

def local():
	treeList = if_in_tree('/Users/ChristinaShehata/Downloads/RAxML_bestTree.gene001.single.tree')
	newDict = trimName('/Users/ChristinaShehata/Downloads/gene001.single.trimmed.FNA', treeList)
	#write(newDict, '/Users/ChristinaShehata/Downloads/gene001.single.trimmed.FNA.short')

#local()
