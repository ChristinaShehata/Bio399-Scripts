import sys
import csv

######################################################################
## 
## Files needed:
## sys.argv[1] is CSV file containing population information
## sys.argv[2] is output populations file
##
######################################################################

def make_population_file(CSV):
	""" makes tabulated populations file for LSD """
	recordList = []
	L = []
	with open(CSV, 'r', encoding="utf-8") as input:
		reader = csv.reader(input)
		for record in reader:
			recordList.append(record)
	for rec in recordList:
		for i in range(len(rec)):
			if rec[i] == '0':
				rec[i] = '00'
			if '\ufeff' in rec[i]:
				rec[i] = rec[i][1:]
		L.append(rec)
	return L

def write_popFile(L, pops):
	""" writes population file """
	with open(pops, 'w', encoding="utf-8") as output:
		for i in range(len(L[0])):
			for rec in L: output.write(rec[i] + '\t')
			output.write('\n')

def main():
	L = make_population_file(sys.argv[1])
	write_popFile(L, sys.argv[2])

main()




	


