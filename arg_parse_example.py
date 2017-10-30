#! /usr/bin/env python3

from peak_parser import Bedfile
from peak_parser import Gff_file
from peak_parser import DE_genes
import argparse

parser = argparse.ArgumentParser(description="parses bedfiles.")
parser.add_argument("-c","--chromosome",
					help="chromosome name", required=False) #False is default
parser.add_argument("-d", "--DE_genes", help="differential expression files with logfold change. Consistent format required",
					required=False)
parser.add_argument("-f", "--files",
					help="the actual bedfile", required=False,
					nargs='+') #nargs means number of agruments = 1 or more. You can only have one parameter of one or more
parser.add_argument("-g", "--gff", help="gff file path",
					required=False)
parser.add_argument("-p", "--peaks",
					help="number of peaks in selected chromosome", required=False,
					default=1, type=int)
parser.add_argument("-x", "--expression", required=False,
					help="returns list of genes from selected chromosome with >2 Log2foldchange")
					#choices=lambda x:x if float(x) >= 1 else raise argparse.ArgumentTypeError("expression must be greater than 1"))
parser.add_argument("-l", "--list", help="gene list text file for expression parsing",
					required=False)
args=parser.parse_args()

#read in bedfile by looping through arg.files list and returning each file, so path=file
# for file in args.files:
# 	bedfile = Bedfile(path=file)
# 
# 	chr1 = bedfile.chromosomes[args.chromosome]
# 	#print every peak object in our list of objects
# 	bedfile_gene_list = list()
# 	for peak in chr1.peaks[0:args.peaks]:
#		print(peak)
# 		bedfile_gene_list.append(peak.signal)


# gff_file = Gff_file(args.gff)
# gff_gene_list = list()
# gff_gene_list = gff_file.chromosomes["chr1"]
# for gene in gff_gene_list.genes:
# 	print(gene.ID)

genes_for_comparison = list()
with open(args.list) as gene_list:
	for line in gene_list:
		fields = line.rstrip()
		genes_for_comparison.append(fields)
# print(genes_for_comparison)
	
de_file = DE_genes(path=args.DE_genes)
de_genes_list = list()
de_genes_list = de_file.expression_values_dict["gene"]

#print out all expression values that match IDs between files
for gene in de_genes_list.degenes:
# 	print(gene.ID, type(gene.ID))
	if gene.ID in genes_for_comparison:
		print(gene.ID, "\t", gene.foldchange)
	
	
	
	
	
	
	
	
	
	