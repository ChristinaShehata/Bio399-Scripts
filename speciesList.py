import sys
import csv
from Bio import SeqIO

def main(fasta):
	recordList = []
	records = list(SeqIO.parse(fasta, "fasta"))
	print(str(sys.argv[1]), len(records))

#main(sys.argv[1])

"""
with open('/Users/ChristinaShehata/Desktop/output.file', "r") as f:
	L = []
	read = f.readlines()
	for x in read:
		#L.append(int(x[-5:-2]))
		if int(x[-5:-2]) == 315:
			print(x)
	#print(max(L))
"""

def main(fasta):
	records = list(SeqIO.parse(fasta, "fasta"))
	with open('/Users/ChristinaShehata/Desktop/artSpecies.txt', 'w') as f:
		for record in records:
			f.write(record.id + '\n')
		
	
#main('/Users/ChristinaShehata/Desktop/gene133.single.FNA')

		
	