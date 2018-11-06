import sys
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PAML.chi2 import cdf_chi2

######################################################################
## 
## Files needed:
## sys.argv[1] is gene list file
## sys.argv[2] is directory with PAML results files
## sys.argv[3] is output file
##
######################################################################

def omega(PAML, outFile):
	""" parses dN/dS value (omega) from PAML output file """
	with open(outFile, 'w') as f:
		results = codeml.read(PAML)
		f.write(results["NSsites"][0]["parameters"]["omega"] + '\n')

def allGenes(geneL):
	""" makes master gene List """
	with open(geneL, 'r') as f:
		geneList = [line.rstrip() for line in f.readlines()]
	return geneList

def LRT(PAML, gene):
	""" calculates LRT statistic for each gene """
	LRT_dict = {}
	df = 2
	results = codeml.read(PAML)
	M1_lnL = results['NSsites'][1]['lnL']
	M2_lnL = results['NSsites'][2]['lnL']
	LRT_stat = 2 * (M2_lnL - M1_lnL)
	if LRT_stat < 0: #redo
		LRT_dict[gene] = cdf_chi2(df, 0)
	else:
		LRT_dict[gene] = cdf_chi2(df, LRT_stat)
	return LRT_dict

def passed_LRT(LRT_dict, outFile):
	with open(outFile, 'w') as q:
		for gene, p_value in LRT_dict.items():
			if p_value < 0.05:
				q.write(gene)

def BEB(PAML, gene):
	L = []
	sig_count = 0
	with open(PAML, 'r') as f:
		for line in f:
			if "Bayes Empirical Bayes (BEB) analysis" in line:
				break
		for line in f:
			if "The grid" in line:
				break
			L.append(line)
	for site in L[3:]:
		if '*' in site:
			sig_count += 1
	return sig_count

def main():
	pass_list = []
	geneList =  allGenes(sys.argv[1])
	with open(sys.argv[3], 'w') as q:
		for gene in geneList:
			sig_count = BEB(sys.argv[2] + gene + '_sites_M1M2.paml', gene)
			if sig_count > 0:
				q.write(gene + '\n')

def sites():
	pass_list = []
	geneList =  allGenes('/Users/ChristinaShehata/Desktop/Artocarpus_LSD/artGeneList.txt')
	with open('/Users/ChristinaShehata/Downloads/passed_M1M2_geneList.txt', 'w') as q:
		for gene in geneList:
			sig_count = BEB('/Users/ChristinaShehata/Downloads/output_M1M2/' + gene + '_sites_M1M2.paml', gene)
			if sig_count > 0:
				q.write(gene + '\n')

sites()
