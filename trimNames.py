import sys
from Bio import SeqIO

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
			newDict[record.id[-10:]] = record.seq
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
