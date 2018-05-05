import sys

####################################################################################
##
## Files Needed:
## sys.argv[1] = population ID file
## sys.argv[2] = output file
##
####################################################################################

def make_popList(populationFile, outFile):
	"""
	makes a \n-spaced population list from a tab-delimited population file
	input populations: a tab-delimited text file containing population IDs
	input outFile: output text file
	"""
	outgroup_id = 'ANC'
	popList1 = []
	popList2 = []
	finalList = []
	with open(populationFile, 'r') as f:
		pops = f.read()
		popList1 = pops.split('\t')
		for ind in popList1:
			popList2.append(ind[0:-1])
	finalList = list(set(popList2))
	with open(outFile, 'w') as f:
		for i in finalList:
			if i != outgroup_id:
				f.write(i + '\n')

def main():
	make_popList(sys.argv[1], sys.argv[2])

main()