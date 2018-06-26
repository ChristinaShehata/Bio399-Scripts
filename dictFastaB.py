import sys
import json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

####################################################################################
##
## Files Needed:
## sys.argv[1] = path to jsonDictB
## sys.argv[2] = a list containing the individuals of interest separated by '\n'
## sys.argv[3] = path to directory for LociFolder B
##
####################################################################################

windowLength = 10000
overlapLength = 5000
#windowList = list(range(55000,110000, overlapLength))
windowList = list(range(110905000, 112104000, overlapLength)) # change for more windows
newL = []

def open_json(j):
	"""
	open_json opens json files with haploDict information
	input j = path to json file
	"""
	with open(j, "r") as f:
		data = json.loads(f.read())
	haploDictB = json.loads(data)
	return haploDictB

def idLst(indList):
	"""
	idList creates a list out of a text file containing individuals of interest
	input indList: a list containing the individuals of interest separated by '\n'
	"""
	with open(indList, "r") as f: 
		L = [line.strip() + 'B' for line in f.readlines()] #for haploDictA
	return L

def parseDict(n, id, haploDictB):
	""" parseDict parses through haploDictsA and B
	input n: start position of window
	"""
	refList = ['A']*windowLength
	newSeq = ''
	tupList = []
	for position, id_snp in haploDictB.items():
		for i in range(len(refList)):
			if int(position) - n == i:
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
	rList = list(chunks(recordList, len(idList))) 
	for r in rList:
		for record in r:
			new_dict[record.name] = r
	return new_dict

def write(new_dict, output):
	""" writes sequences to 10kb fasta files
	input output: path to directory to hold fasta files
	"""
	for record, seqList in new_dict.items():
		with open(output + "output{}.fa".format(record + '-' + str(int(record)+windowLength)), "w") as f:
			for ind_seq in seqList:
				f.write("{}	{}\n".format(("> " + ind_seq.id), ind_seq.seq))

def main():
	haploDictB = open_json(sys.argv[1]) #for haploDictB
	idList = idLst(sys.argv[2])
	for n in windowList:
		for id in idList:
			newL.append(parseDict(n,id, haploDictB)) 
	new_dict = prep(idList)
	write(new_dict, sys.argv[3])

main()


