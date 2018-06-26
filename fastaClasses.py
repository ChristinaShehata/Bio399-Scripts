import sys
import json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

windowLength = 10000
overlapLength = 5000
windowList = list(range(55000,110000, overlapLength))
#windowList = list(range(110905000, 112104000, overlapLength)) # change for more windows
newL = []
dList = [] #each element is all the variants for one individual

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

class Sample:
	def __init__(self, id, snp):
		""" the constructor for objects of type Sample
		Each sample has the following attributes:
		
		id: name of sample
		snp: variation in genome
		"""
		self.id = id
		self.snp = snp
		
def parse(id, haploDictA):
	d = {}
	positionList = haploDictA.keys()
	sampleList = [Sample(id, id_snp[id]) for position, id_snp in haploDictA.items()]
	d = dict(zip(positionList, sampleList))
	return d
	
def midstep(idList, n, haploDictA):
	refList = ['-']*windowLength
	newSeq = ''
	for id in idList:
		d = parse(id, haploDictA)
		for pos, sample in d.items():
			for i in range(len(refList)):
				if int(pos) - n == i:
					refList[i] = sample.snp
					newSeq = "".join(refList)
	return newSeq


def main():
	dList = [] #each element is all the variants for one individual
	string = ''
	haploDictA = open_json('/Users/ChristinaShehata/Desktop/jsonA_test.json') #for haploDictA
	idList = idLst('/Users/ChristinaShehata/Desktop/150ind.txt')
	for n in windowList:
		print(midstep(idList,n, haploDictA))
	"""
	tupList = []
	for position, id_snp in haploDictA.items():
		for i in range(len(refList)):
			if int(position) - n == i:
				refList[i] = id_snp[id]
				newSeq = "".join(refList)
	tupList.append((id, newSeq, n))
	return tupList
	"""
		#dList.append(d)
	#for samp in d.values():
		#for x in samp.seq:
			#samp.seq[x] = samp.snp
		#print(samp.seq)
		#string = string + samp.snp
	#print(len(string))
	#print(len(haploDictA))
	#for position, sample in d.items():

#make list of lists of positions in each window?
	
main()