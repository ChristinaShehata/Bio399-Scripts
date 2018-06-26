import sys
import json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import time

####################################################################################
##
## Files Needed:
## sys.argv[1] = path to jsonDictA (dictionary containing SNP data)
## sys.argv[2] = a list containing the individuals of interest separated by '\n'
## sys.argv[3] = path to directory for LociFolderA (output)
## sys.argv[4] = window (loci) number (to parallelize) -- use windowList.py first
##
####################################################################################

windowLength = 10000

def open_json(j):
	"""
	open_json opens json files with haploDict information
	input j = path to json file
	"""
	with open(j, "r") as f:
		data = json.loads(f.read())
	haploDictA = json.loads(data)
	return haploDictA

def idLst(indList):
	"""
	idList creates a list out of a text file containing individuals of interest
	input indList: a list containing the individuals of interest separated by '\n'
	"""
	with open(indList, "r") as f: 
		L = [line.strip() + 'A' for line in f.readlines()] #for haploDictA
	return L

def parseDict(n, id, haploDictA):
	""" parseDict parses through haploDictA
	input n: start position of window
	"""
	xList = []
	refList = ['A']*windowLength
	newSeq = ''
	tupList = []
	for position, id_snp in haploDictA.items():
		for i in range(len(refList)):
			if int(position)-n == i:
				refList[i] = id_snp[id]
				newSeq = "".join(refList)
	tupList.append((id, newSeq, n))
	return tupList

def main():
	haploDictA = open_json(sys.argv[1])
	idList = idLst(sys.argv[2])
	outFile = str(sys.argv[3]) + 'output_{}.fa'.format(str(sys.argv[4]) + '-' + str(int(sys.argv[4])+windowLength))
	L = []
	with open(outFile, 'w') as f:
		for i in range(len(idList)):
			print('Working on... ' + idList[i] + '\t' + str(i+1) + '/150') # check progress
			L.append(parseDict(int(sys.argv[4]), idList[i], haploDictA)) 
			f.write('>' + idList[i] + '\n' + L[i][0][1] + '\n')

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time)) # print runtime


