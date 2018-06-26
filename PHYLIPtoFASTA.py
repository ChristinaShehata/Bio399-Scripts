import sys
from Bio import AlignIO

######################################################################
## 
## Files needed:
## sys.argv[1] is input phylip file
## sys.argv[2] is output fasta file
##
######################################################################

def convert(phylip, fasta):
	""" converts a phylip file into a fasta file
	input fasta: input phylip file containing sequences of equal length
	input phylip: output fasta file
	"""
	with open(phylip, 'r') as f:
		with open(fasta, 'w') as q:
			sampleList = []
			seqList = []
			read = f.readlines()
			L = (read[1:])
			for i in range(len(L)):
				if i%2 == 0:
					sampleList.append(L[i].strip())
				else:
					seqList.append(L[i].strip())
			for i in range(len(sampleList)):
				q.write('>' + sampleList[i] + '\n' + seqList[i] + '\n')

convert(sys.argv[1], sys.argv[2])