import sys

####################################################################################
##
## Files Needed:
## sys.argv[1] = population ID file
## sys.argv[2] = output file
##
####################################################################################

def comma(populationFile, outFile):
	"""
	makes a comma-separated d population list from a tab-delimited population file
	Used to identify samples for Data Slicer
	input populations: a tab-delimited text file containing population IDs
	input outFile: output text file
	"""
	with open(populationFile, 'r') as f:
		pops = f.read()
		popList1 = pops.replace('\t', ',')
		with open(outFile, 'w') as q:
			q.write(popList1)

def main():
	comma(sys.argv[1], sys.argv[2])

main()