import sys
from Bio import SeqIO

def window(fasta):
	""" window divides a fasta file into 10kb fragments with 5kb overlap
	input fasta: fasta file
	"""
	seqDict = {}
	fragment_length = 10000
	overlap_length = 5000
	for seq_record in SeqIO.parse(fasta, "fasta"):
		sequence = seq_record.seq
	fileNumber = int((len(sequence) / overlap_length))
	for x in range(fileNumber):
		n = x * overlap_length
		newFasta = sequence[n:n + fragment_length]
		seqDict[x] = newFasta 	# change
	return seqDict

def writeFasta(seqDict, fastaFolder):
	""" writeFasta writes each shorter sequence into a new fasta file
	input seqDict: dictionary containing loci ids and corresponding sequences
	input fastaFolder: directory to store new fasta files
	"""
	for id, seq in seqDict.items():
		f = open(mypath + "lociFolder/chrom12_{0}.fa".format(id), "w") # change
		f.write('> ' + str(id) + '\n')
		f.write(str(seq))
		f.close()

def writeID(seqDict, id_file):
	""" writeID creates a new file containing all the loci ids
	input seqDict: dictionary containing loci ids and corresponding sequences
	input id_file: path to new file containing all loci ids
	"""
	f = open(id_file, "w")
	for id in seqDict.keys():
		f.write(str(id) + '\n')
	f.close()
	
def main():
	seqDict = window(sys.argv[1])
	writeFasta(seqDict, sys.argv[2])
	writeID(seqDict, sys.argv[3])

main()

# edit ids for specific loci


