import sys
import csv
from Bio import SeqIO

######################################################################
## 
## Files needed:
## sys.argv[1] is baits file
## sys.argv[2] is output species list
##
######################################################################

def main(fasta, outFile):
	records = list(SeqIO.parse(fasta, "fasta"))
	with open(outFile, 'w') as f:
		for record in records:
			f.write(record.id + '\n')
		
	
main(sys.argv[1], sys.argv[2])

		
	