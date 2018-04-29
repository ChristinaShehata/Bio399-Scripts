import vcf
mypath = "/Users/ChristinaShehata/Desktop/Wickett-Lab/Bio399-pyScripts/"

def idList():
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
	for position, d in subDict.items():
		for key in d:
			tListA.append((key+'A', d.get(key)[0]))
			tListB.append((key+'B', d.get(key)[2])) #doesn't work for ones with multiple snp variations
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
	
def fasta(L, haploTuple):
	haploDictA = haploTuple[0]
# make fasta windows

def main():
	L = idList()
	subDict = genotype(L)
	haploTuple = haplotype(L, subDict)
	fasta(L, haploTuple)
	
main()


