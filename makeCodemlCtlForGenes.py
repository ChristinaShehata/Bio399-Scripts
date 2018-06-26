#!/usr/bin/python
import sys

#####################################
##Creates codonml .ctl file for each gene with correct input and output file names
##argv[1] is gene name
##argv[2] is original codonml file
##argv[3] is directory to output files
#####################################

def makectl(outFile):
	with open(outFile + "codonml_{}.ctl".format(sys.argv[1]), 'w') as f:
		example1=open(sys.argv[2],"r")
		example=example1.readlines()
		for line in example:
			new=line.replace("uniquegenename",sys.argv[1])
			f.write(new)
		example1.close()

makectl(sys.argv[3])