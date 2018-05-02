from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

haploDictA = {60181: {'NA18861A': 'G', 'HG02493A': 'G', 'NA11918A': 'G'}, 60219: {'NA18861A': 'G', 'HG02493A': 'G', 'NA11918A': 'G'}, 60220: {'NA18861A': 'A', 'HG02493A': 'A', 'NA11918A': 'A'}, 60278: {'NA18861A': 'G', 'HG02493A': 'G', 'NA11918A': 'G'}, 60317: {'NA18861A': 'C', 'HG02493A': 'C', 'NA11918A': 'C'}}

windowList = list(range(55000, 105000, 5000))

def parseDict(n):
	refList = ['-']*10000
	newSeq = ''
	tupList = []
	for position, id_snp in haploDictA.items():
		for i in range(len(refList)):
			if position - n == i:
				for id in id_snp.keys():
					refList[i] = id_snp[id]
					newSeq = "".join(refList)
					tup = (id, newSeq)
					tupList.append(tup)
	return tupList[-3:] #3 = number of individuals -- contains all the snps in one window

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
        
def prep():
	new_dict = {}
	recordList = []
	for n in windowList:
		for x in parseDict(n):
			if x[1] != ():
				recordList.append(SeqRecord(Seq(x[1]),id=x[0],name=str(n)))
	rList = list(chunks(recordList, 3)) #individuals
	for r in rList:
		for record in r:
			new_dict[record.name] = r
	return new_dict

def write(new_dict):
	for record, seqList in new_dict.items():
		with open("/Users/ChristinaShehata/Desktop/ouput{}.fa".format(record + '-' + str(int(record)+10000)), "w") as f:
			for ind_seq in seqList:
				f.write("{}	{}\n".format(("> " + ind_seq.id), ind_seq.seq))

def main():
	dictPrep = prep()
	write(dictPrep)

main()


