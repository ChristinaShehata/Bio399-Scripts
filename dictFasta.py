import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# insert haploDict

windowLength = 10000
overlapLength = 5000
windowList = list(range(55000, 105000, overlapLength)) # change for more windows
newL = []

def idLst(indList):
	"""
	idList creates a list out of a text file containing individuals of interest
	input indList: a list containing the individuals of interest separated by '\n'
	"""
	with open(indList, "r") as f: 
		L = [line.strip() + 'A' for line in f.readlines()] #for haploDictA
	return L

def parseDict(n, id):
	""" parseDict parses through haploDictsA and B
	input n: start position of window
	"""
	refList = ['-']*windowLength
	newSeq = ''
	tupList = []
	for position, id_snp in haploDictA.items():
		for i in range(len(refList)):
			if position - n == i:
				refList[i] = id_snp[id]
				newSeq = "".join(refList)
	tupList.append((id, newSeq, n))
	return tupList

def chunks(l, n):
	""" chunks separates a list into even-sized parts """
	for i in range(0, len(l), n):
		yield l[i:i+n]
        
def prep(idList):
	""" prep makes sequence dictionary
	input idList: list of samples
	"""
	new_dict = {}
	recordList = []
	for x in newL:
		for record in x:
			if record[1] != (''):
				recordList.append(SeqRecord(Seq(record[1]),id=record[0],name=str(record[2])))
	rList = list(chunks(recordList, len(idList))) #individuals
	for r in rList:
		for record in r:
			new_dict[record.name] = r
	return new_dict

def write(new_dict, output):
	""" writes sequences to 10kb fasta files
	input output: path to directory to hold fasta files
	"""
	for record, seqList in new_dict.items():
		with open(output + "ouput{}.fa".format(record + '-' + str(int(record)+windowLength)), "w") as f:
			for ind_seq in seqList:
				f.write("{}	{}\n".format(("> " + ind_seq.id), ind_seq.seq))

def main():
	idList = idLst(sys.argv[1])
	for n in windowList:
		for id in idList:
			newL.append(parseDict(n,id)) #works
	new_dict = prep(idList)
	write(new_dict, sys.argv[2])

main()


