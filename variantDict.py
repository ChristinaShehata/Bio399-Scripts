import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

####################################################################################
##
## Files Needed:
## sys.argv[1] = output window list
## sys.argv[2] = list of all samples
## sys.argv[3] = path to filtered_variant.txt files
## sys.argv[4] = path to output fasta files (before concatenation)
## sys.argv[5] = n (from window list)
##
####################################################################################
windowLength = 10000
overlapLength = 5000
windowList = list(range(15000000, 25000000, overlapLength)) # region of interest

class Variant:

	def __init__(self, sample, chromosome, position, snp):
		""" the constructor for objects of type Variant """
		self.sample = sample
		self.chromosome = chromosome
		self.position = position
		self.snp = snp

def windowFile(outFile):
	""" makes file of window numbers to parallelize script """
	with open(outFile, 'w') as f:
		for n in windowList:
			f.write(str(n) + '\n')

def sampleL(inFile):
	""" makes list containing all 80 samples """
	with open(inFile, 'r') as f:
		sampleList = [line.strip() for line in f.readlines()]
	return sampleList

def chr1_list(inPath, n, ID): #no deletions
	""" isolates chromosome 1 SNPs """
	chr1List = []
	with open(inPath + '{}_filtered_variant.txt'.format(ID), 'r') as f:
		read = [line.strip().split('\t') for line in f.readlines()]
		for x in read:
			v = Variant(x[0], x[1], x[2], x[4])
			if v.chromosome == '1' and int(v.position) >= int(n) and int(v.position) < int(n) + windowLength: # only chromsome 1
				chr1List.append((v.sample, v.position, v.snp))
	return chr1List

def parse_dict(outPath, tupList, n, ID):
	""" writes output fasta files """
	refList = ['A'] * windowLength # set a default character
	newSeq = ''
	mutated_records = []
	for lst in tupList:
		for tup in lst:
			sample, position, snp = tup
			for i in range(len(refList)):
				if int(position) - int(n) == i:	# if there's a SNP, change the default character
					refList[i] = snp
					newSeq = "".join(refList)
	mutated_records.append(SeqRecord(Seq(newSeq), id = ID, description = n + '-' + str(int(n)+windowLength), name = 'arabidopsis_' + str(n) + '-' + str(int(n) + windowLength)))
	for record in mutated_records:
		if record.seq == '':
			record.seq = Seq('A' * windowLength) # fill in sequences with no SNPs in this window
		if record.name == 'arabidopsis_'  +str(n) + '-' + str(int(n) + windowLength):
			SeqIO.write(record, outPath + ID + '_arabidopsis_'  + n + '-' + str(int(n) + windowLength)+ ".fasta", "fasta") # concatenate later

def all_records(ID):
	tupList = []
	n = sys.argv[5]
	tupList.append(chr1_list(sys.argv[3], n, ID))
	parse_dict(outPath, tupList, n, ID)

def main():
	""" gets SNP information from all samples """
	#windowFile(sys.argv[1])
	allRecords = []
	sampleList = sampleL(sys.argv[2])
	for ID in sampleList:
		all_records(ID)

main()












