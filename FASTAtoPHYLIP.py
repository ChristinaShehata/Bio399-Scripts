from Bio import AlignIO

def convert(fasta, phylip):
	""" converts a FASTA file into a PHYLIP file
	input fasta: input fasta file containing sequences of equal length
	input phylip: output phylip file
	"""
	input_handle = open(fasta, "rU")
	output_handle = open(phylip, "w")

	alignments = AlignIO.parse(input_handle, "fasta")
	AlignIO.write(alignments, output_handle, "phylip")

	output_handle.close()
	input_handle.close()
