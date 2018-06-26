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
	taxa = []
	red = []
	orange = []
	light_blue = []
	dark_blue = []
	purple = []
	yellow = []
	pink = []
	green = []
	with open(pops, 'w', encoding="utf-8") as output:
		with open(CSV, 'r', encoding="utf-8") as input:
			reader = csv.reader(input)
			for record in reader:
				taxa.append(record[0].replace('\ufeff', ''))
				red.append(record[1].replace('0', '00'))
				orange.append(record[2].replace('0', '00'))
				light_blue.append(record[3].replace('0', '00'))
				dark_blue.append(record[4].replace('0', '00'))
				purple.append(record[5].replace('0', '00'))
				yellow.append(record[6].replace('0', '00'))
				pink.append(record[7].replace('0', '00'))
				green.append(record[8].replace('0', '00'))
		output.write('\t'.join(taxa))
		output.write('\t\n')
		output.write('\t'.join(red))
		output.write('\t\n')
		output.write('\t'.join(orange))
		#output.write('\t\n')
		#output.write('\t'.join(light_blue))
		#output.write('\t\n')
		#output.write('\t'.join(dark_blue))
		#output.write('\t\n')
		#output.write('\t'.join(purple))
		#output.write('\t\n')
		#output.write('\t'.join(yellow))
		#output.write('\t\n')
		#output.write('\t'.join(pink))
		#output.write('\t\n')
		#output.write('\t'.join(green))

#make_population_file(sys.argv[1], sys.argv[2])		
#make_population_file('/Users/ChristinaShehata/Desktop/artocarpus.csv', '/Users/ChristinaShehata/Desktop/LSD/artocarpus.pops')





	


