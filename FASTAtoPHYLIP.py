import sys
from Bio import AlignIO

def convert(sys.argv[1], sys.argv[2]):
	""" converts a FASTA file into a PHYLIP file
	input sys.argv[1]: input fasta file containing sequences of equal length
	input sys.argv[2]: output phylip file
	"""
	fasta = sys.argv[1]
	phylip = sys.argv[2]
	input_handle = open(fasta, "rU")
	output_handle = open(phylip, "w")

	alignments = AlignIO.parse(input_handle, "fasta")
	AlignIO.write(alignments, output_handle, "phylip")

	output_handle.close()
	input_handle.close()