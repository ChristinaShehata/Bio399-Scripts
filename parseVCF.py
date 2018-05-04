import sys
import vcf
import json
from Bio import SeqIO

####################################################################################
##
## Files Needed:
## sys.argv[1] = a list containing the individuals of interest separated by '\n'
## sys.argv[2] = vcf file containing variant information
##
####################################################################################

def idList(indList):
	"""
	idList creates a list out of a text file containing individuals of interest
	input indList: a list containing the individuals of interest separated by '\n'
	"""
	with open(indList, "r") as f: 
		L = [line.strip() for line in f.readlines()]
	return L
	
def genotype(L, variants):
	"""
	genotype creates a dictionary with all SNP positions as the keys and dictionaries 
	of individual IDs and genotype information as the values
	input L: list of individuals (samples) of interest
	input variants: vcf file containing variant information
	"""
	posList = []
	sampleList = []
	gtList = []
	genoDict = {}
	tupList = []
	subDict = {}
	vcf_reader = vcf.Reader(open(variants, 'r'))
	for record in vcf_reader:
		posList.append(record.POS)
		for id in L: # filter step
			call = record.genotype(id)
			sampleList.append(call.sample)
			gtList.append(call.gt_bases)
	for sample, gt in zip(sampleList, gtList):
		genoDict.setdefault(sample, []).append(gt) #id: [list of all snps for that individual]
	for x in range(len(posList)):
		for samp, geno in genoDict.items():
			tupList.append((samp,geno[x])) # 612 tuples for each id
	n = len(L) #150
	LL = [tupList[i:i + n] for i in range(0, len(tupList), n)]
	subDict = dict(zip(posList, LL))
	for key, value in subDict.items():
		subDict[key] = dict(value)
	return subDict

def haplotype(L, subDict):
	""" haplotype turns a genotype dictionary into a haplotype dictionary
	input L: list of samples
	input subDict: genotype dictionary
	"""
	positions = subDict.keys()
	tListA = []
	tListB = []
	for position, d in subDict.items():
		for key in d:
			tListA.append((key+'A', d.get(key).split('|')[0])) # works for indels, but multiple alleles?
			tListB.append((key+'B', d.get(key).split('|')[1])) 
	n = len(L) #150
	A = [tListA[i:i + n] for i in range(0, len(tListA), n)]
	B = [tListB[i:i + n] for i in range(0, len(tListB), n)] 
	haploDictA = dict(zip(positions, A))
	haploDictB = dict(zip(positions, B))
	for key, value in haploDictA.items():
		haploDictA[key] = dict(value)
	for key, value in haploDictB.items():
		haploDictB[key] = dict(value)
	return (haploDictA, haploDictB)

def main():
	L = idList(sys.argv[1])
	subDict = genotype(L, sys.argv[2])
	haploTuple = haplotype(L, subDict)
	jsonA = json.dumps(haploTuple[0])
	jsonB = json.dumps(haploTuple[1])
	with open(sys.argv[3] + 'jsonA.json', 'w') as a:
		json.dump(jsonA, a)
	with open(sys.argv[4] + 'jsonB.json', 'w') as b:
		json.dump(jsonB, b)
	
main()


