import sys
from Bio import SeqIO

####################################################################################
##
## Files Needed:
## sys.argv[1] = fasta file to correct
## sys.argv[2] = corrected fasta file
##
####################################################################################
	
def cut(fasta):
	""" Removes individuals with sequences trimmed too short
	input fasta: fasta file
	"""
	with open(fasta, 'r') as f:
		lenList = []
		newDict = {}
		records = list(SeqIO.parse(f, "fasta"))
		for record in records:
			lenList.append(len(record.seq))
			if len(record.seq) == max(lenList): #keep
				newDict[record.id] = record.seq
	return newDict
	
def rewrite(newDict, outFile):
	""" rewrites trim file
	input newDict: dictionary with the right ids and sequences
	input outFile: new fasta file
	"""
	with open(outFile, 'w') as f:
		for id, seq in newDict.items():
			f.write('>'+id+'\n')
			f.write(str(seq) + '\n')
			
def main():
	newDict = cut(sys.argv[1])
	rewrite(newDict, sys.argv[2])

main()
