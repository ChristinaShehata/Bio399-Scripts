import vcf
mypath = "/Users/ChristinaShehata/Desktop/Wickett-Lab/Bio399-pyScripts/"

def idList(): #not necessary if you use vcf tools to only have vcf info from individuals of interest
	"""
	idList creates a list out of a text file containing individuals of interest
	"""
	with open("/Users/ChristinaShehata/Desktop/150ind.txt", "r") as f: 
		L = [line.strip() for line in f.readlines()]
	return L
	
def genotype(L):
	"""
	genotype creates a dictionary with all SNP positions as the keys and dictionaries 
	of individual IDs and genotype information as the values
	input L: list of individuals (samples) of interest
	"""
	posList = []
	sampleList = []
	gtList = []
	genoDict = {}
	tupList = []
	subDict = {}
	vcf_reader = vcf.Reader(open('/Users/ChristinaShehata/Desktop/SMALLchr12Variants.vcf', 'r'))
	for record in vcf_reader:
		posList.append(record.POS)
		for id in L:
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
	positions = subDict.keys()
	tListA = []
	tListB = []
	finalDict = {}
	for position, d in subDict.items():
		for key in d:
			tListA.append((key+'A', d.get(key)[0]))
			tListB.append((key+'B', d.get(key)[2])) #doesn't work for ones with multiple snp variations
	n = len(L) #150
	LLA = [tListA[i:i + n] for i in range(0, len(tListA), n)]
	LLB = [tListB[i:i + n] for i in range(0, len(tListB), n)] 
	haploDictA = dict(zip(positions, LLA))
	haploDictB = dict(zip(positions, LLB))
	for key, value in haploDictA.items():
		haploDictA[key] = dict(value)
	for key, value in haploDictB.items():
		haploDictB[key] = dict(value)
	return (haploDictA, haploDictB)
	
def fasta(L, haploTuple):
	headerList = []
	haploDictA = haploTuple[0]
	positionsA = list(haploDictA.keys())
# make fasta windows

def main():
	L = idList()
	subDict = genotype(L)
	haploTuple = haplotype(L, subDict)
	fasta(L, haploTuple)
	

main()


"""
Yes, based on the positions - like that screenshot says it's 
chromosome 12, position 60219. So if you're overlapping the windows, 
that snp would be in position 719 for the window from 59500-60500, and 
in position 219 for the window from 60000-61000.
"""