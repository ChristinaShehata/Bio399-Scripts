import vcf
mypath = "/Users/ChristinaShehata/Desktop/Wickett-Lab/Bio399-pyScripts/"

def idList(): #not necessary if you use vcf tools to only have vcf info from individuals of interest
	with open("/Users/ChristinaShehata/Desktop/150ind.txt", "r") as f: 
		L = [line.strip() for line in f.readlines()]
	return L

def positionList():
	posList = []
	vcf_reader = vcf.Reader(open('/Users/ChristinaShehata/Desktop/SMALLchr12Variants.vcf', 'r'))
	for record in vcf_reader:
		posList.append(record.POS)
	return posList
	
def both_chrom(L, posList):
	sampleList = []
	gtList = []
	genoDict = {}
	positions = []
	tupList = []
	subDict = {}
	vcf_reader = vcf.Reader(open('/Users/ChristinaShehata/Desktop/SMALLchr12Variants.vcf', 'r'))
	for record in vcf_reader:
		positions.append(record.POS)
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
		subDict[key] = dict(value) ##YAY
	return subDict
	
def main():
	L = idList()
	posList = positionList()
	both_chrom(L, posList)

main()