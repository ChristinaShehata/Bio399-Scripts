import sys

######################################################################
## 
## Files needed:
## sys.argv[1] is output windowList text file
##
######################################################################

start = 111350000
end = 111460000
overlapLength = 5000

windowList = list(range(start, end, overlapLength))

def windowList(outFile):
	""" makes a list of loci windows
	input outFile: text list of loci
	"""
	with open(outFile, 'w') as f:
		for n in windowList:
			f.write(str(n) + '\n')
	
def main():
	windowList(sys.argv[1])

