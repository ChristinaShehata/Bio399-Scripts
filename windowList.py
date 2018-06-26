import sys

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
	windowList('/Users/ChristinaShehata/Desktop/windowList.txt')

