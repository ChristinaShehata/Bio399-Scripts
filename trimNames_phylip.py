import sys
from Bio import SeqIO

####################################################################################
##
## Files Needed:
## sys.argv[1] = phylip with full names
## sys.argv[2] = phylip with abbreviated names
##
####################################################################################

def trimName(phylip):
	""" cuts down sample names to convert into phylip format
	input fasta: fasta file of trimmed alignments
	"""
	newDict = {}
	L = []
	with open(phylip, 'r') as f:
		read = f.readlines()
		for x in read[1:]:
			L.append(x.split())
	for i in range(len(L)):
		if 'A_altilisx' in L[i][0]:
			L[i][0] = 'A_altxA_mar' + L[i][0][-15:]
		newDict[L[i][0]] = L[i][1]
	return newDict

def write(newDict, phylip, cutPhylip):
	""" writes trimmed names and sequences """
	with open(phylip, 'r') as f:
		read = f.readlines()
		l = read[0].split()
		ind = l[0]
		len = l[1]
		with open(cutPhylip, 'w') as q:
			q.write("	" + ind + "	" + len + '\n')
			for id, seq in newDict.items():
				q.write("{}  {}\n".format(id, seq))

def main():
	newDict = trimName(sys.argv[1])
	write(newDict, sys.argv[1], sys.argv[2])
	
main()

"""
parallel -j6 "python /data/cshehata/python/trimNames_phylip.py /data/cshehata/Artocarpus/PAML/trimmed_inframe/{}.trimmed.FNA.short /data/cshehata/Artocarpus/PAML/trimmed_inframe/{}.trimmed.FNA.short.phy" :::: /data/cshehata/Artocarpus/artGeneList.txt
"""

def local():
	newDict = trimName('/Users/ChristinaShehata/Downloads/gene002.p0.trimmed.FNA.reduced')
	write(newDict, '/Users/ChristinaShehata/Downloads/gene002.p0.trimmed.FNA.reduced', '/Users/ChristinaShehata/Downloads/gene002.p0.trimmed.FNA.reduced.short')

#local()





			