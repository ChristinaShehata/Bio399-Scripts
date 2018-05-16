import sys
from Bio import SeqIO

def trimName(fasta):
	newDict = {}
	with open(fasta, 'r') as f:
		records = list(SeqIO.parse(f, "fasta"))
		for record in records:
			newDict[record.id[-10:]] = record.seq
	return newDict

def write(newDict, cutFasta):
	with open(cutFasta, 'w') as f:
		for id, seq in newDict.items():
			f.write('>'+id+'\n')
			f.write(str(seq) + '\n')

def main():
	newDict = trimName(sys.argv[1])
	write(newDict, sys.argv[2])
	
main()
