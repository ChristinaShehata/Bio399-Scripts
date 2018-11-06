import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#########################################
## fasta to relaxed phylip format
## sys.argv[1] is fasta file of aligned sequences
## sys.argv[2] is output phylip
#########################################

def convert():
	with open(sys.argv[2], 'w') as q:
		with open(sys.argv[1],'r') as f:
			trimmed_dict=SeqIO.to_dict(SeqIO.parse(f,"fasta"))
			trimmed_list=[key for key in trimmed_dict.keys()]
			sp1=trimmed_list[0]
			l=len(trimmed_dict[sp1].seq)
			l2=len(trimmed_list)
			q.write("  "+str(l2)+"  "+str(l)+"\n")	
		for record in trimmed_list:
			q.write("{}  {}\n".format(trimmed_dict[record].id, trimmed_dict[record].seq))

convert()

"""
parallel -j6 "python /data/cshehata/python/fasta_to_phylip_PAML.py /data/cshehata/Artocarpus/PAML/trimmed_inframe/{}.trimmed.FNA.short /data/cshehata/Artocarpus/PAML/trimmed_inframe/{}.trimmed.FNA.short.phy" :::: /data/cshehata/Artocarpus/artGeneList.txt
"""

def local():
	with open('/Users/ChristinaShehata/Downloads/gene001.single.trimmed.FNA.short.phy', 'w') as q:
		with open('/Users/ChristinaShehata/Downloads/gene001.single.trimmed.FNA.short', 'r') as f:
			trimmed_dict=SeqIO.to_dict(SeqIO.parse(f,"fasta"))
			trimmed_list=[key for key in trimmed_dict.keys()]
			sp1=trimmed_list[0]
			l=len(trimmed_dict[sp1].seq)
			l2=len(trimmed_list)
			q.write("  "+str(l2)+"  "+str(l)+"\n")	
		for record in trimmed_list:
			q.write("{}  {}\n".format(trimmed_dict[record].id, trimmed_dict[record].seq))

#local()