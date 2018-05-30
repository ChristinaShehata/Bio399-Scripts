import sys
import csv

######################################################################
## 
## Files needed:
## sys.argv[1] is CSV file containing population information
## sys.argv[2] is output populations file
##
######################################################################

def make_population_file(CSV, pops):
	""" makes tabulated populations file for LSD """
	with open(pops, 'w', encoding="utf-8") as output:
		with open(CSV, 'r', encoding="utf-8") as input:
			reader = csv.reader(input)
			for record in reader:
				output.write(record[0] + '\t')
				output.write('\n')
				output.write(record[1] + '\t')
				output.write('\n')
				output.write(record[2] + '\t')

make_population_file(sys.argv[1], sys.argv[2])		

