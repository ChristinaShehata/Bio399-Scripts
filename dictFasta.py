#haploDictA = {60181: {'NA18861A': 'G', 'HG02493A': 'G', 'NA11918A': 'G'}, 60219: {'NA18861A': 'G', 'HG02493A': 'G', 'NA11918A': 'G'}, 60220: {'NA18861A': 'A', 'HG02493A': 'A', 'NA11918A': 'A'}, 60278: {'NA18861A': 'G', 'HG02493A': 'G', 'NA11918A': 'G'}, 60317: {'NA18861A': 'C', 'HG02493A': 'C', 'NA11918A': 'C'}}

def fasta(n):
	refList = ['-']*10000
	newSeq = ''
	tupList = []
	for position, id_snp in haploDictA.items():
		for i in range(len(refList)):
			if position - n == i:
				for id in id_snp.keys():
					newList = [refList]
					for rList in newList:
						rList[i] = id_snp[id]
						newSeq = "".join(list(rList))
						tup = (id, newSeq)
						tupList.append(tup)
	return tupList

def prep():
	windowList = list(range(55000, 105000, 5000))
	new_dict = {}
	fa = ""
	for n in windowList:
		L = [[fasta(n), n] for n in windowList] #makes all windows for one individual
	#print(L)
	for seq in L:
		if seq[0] != ():
			new_dict[(str(seq[1]) + "-" + str(seq[1]+10000))] = SeqRecord(Seq(seq[0][1]),id=seq[0][0])
	return new_dict


def write(new_dict):
	with open("/Users/ChristinaShehata/Desktop/{}.fa".format(id), "w") as f:
		for record in new_dict.keys():
			f.write("{}	{}\n".format(("> " + new_dict[record].id + ", Window: " + record), new_dict[record].seq))

write(prep())