import json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

windowList = list(range(55000, 105000, 5000))
newL = []

def open_json():
	"""
	open_json opens json files with haploDict information
	input j = path to json file
	"""
	with open('/Users/ChristinaShehata/Desktop/jsonA.json', "r") as f:
		data = json.loads(f.read())
	haploDictA = json.loads(data)
	return haploDictA

def idLst():
	"""
	idList creates a list out of a text file containing individuals of interest
	"""
	with open("/Users/ChristinaShehata/Desktop/150ind.txt", "r") as f: 
		L = [line.strip() + 'A' for line in f.readlines()]
	return L
	
def parseDict(n, id, haploDictA):
	refList = ['-']*10000
	newSeq = ''
	tupList = []
	for position, id_snp in haploDictA.items():
		for i in range(len(refList)):
			if int(position) - n == i:
				refList[i] = id_snp[id]
				newSeq = "".join(refList)
	tupList.append((id, newSeq, n))
	return tupList

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def prep(idList):
	new_dict = {}
	recordList = []
	for x in newL:
		for record in x:
			if record[1] != (''):
				recordList.append(SeqRecord(Seq(record[1]),id=record[0],name=str(record[2]))) #find a way to tack on position
	rList = list(chunks(recordList, len(idList))) #individuals
	for r in rList:
		for record in r:
			new_dict[record.name] = r
	#print(new_dict)
	return new_dict

def write(new_dict):
	for record, seqList in new_dict.items():
		with open("/Users/ChristinaShehata/Desktop/HumanLociA/output{}.fa".format(record + '-' + str(int(record)+10000)), "w") as f:
			for ind_seq in seqList:
				f.write("{}	{}\n".format(("> " + ind_seq.id), ind_seq.seq))

def main():
	haploDictA = open_json()
	idList = idLst()
	for n in windowList:
		for id in idList:
			newL.append(parseDict(n,id,haploDictA)) #works
	new_dict = prep(idList)
	write(new_dict)



main()
	

