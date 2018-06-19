import sys
from Bio.Phylo.PAML import codeml

######################################################################
## 
## Files needed:
## sys.argv[1] is PAML output file
## sys.argv[2] is dN/dS output file
##
######################################################################

def omega(PAML, outFile):
	""" parses dN/dS value (omega) from PAML output file """
	with open(outFile, 'w') as f:
		results = codeml.read(PAML)
		f.write(results["NSsites"][0]["parameters"]["omega"] + '\n')
		
def main():
	omega(sys.argv[1], sys.argv[2])

main()