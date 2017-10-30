#!/usr/bin/env python

import sys

#from peak_parser import Bedfile
from peak_parser import Gff_file
from peak_parser import DE_genes

filename_gff = sys.argv[1]
filename_rnaseq = sys.argv[2]
# newfile = Bedfile(path=filename)

#chr1 = newfile.chromosomes['chr1']

#for peak in chr1.peaks:
#	print(peak.mean)
	
		
# chr_name_list = newfile.chromosomes.keys()  	
# print(chr_name_list)



##################
##gff file parse to list geneIDs and then report if there is sig DE genes for those ids in our DE expression file.
chr1_genes = list()
gff_file = Gff_file(path=filename_gff)
# print(gff_file)
# chr1_genes = gff_file.chromosomes["chr1"] #chr1 is now a chromosome object
# for gene in chr1_genes.genes:
# 	print(gene)
# 	chr1_genes.append(gene.ID)
# print(chr1_genes)
# print(chr1_genes) #check
	
# print(chr1_genes, type(chr1_genes), type(chr1_genes[0])) #checks for making list of strings
##################

#######Read in DE_gene object, takes out the dictionary, and create a list of all objects within that dictionary
de_genes = list()
DE_file = DE_genes(path=filename_rnaseq)
# print(DE_file) #check
de_genes = DE_file.expression_values_dict["gene"]

floats_list = list()
expression_list = list()
# for gene in de_genes.degenes:
#	print(gene.ID, type(gene), gene.foldchange[12]) #check if I am getting list of IDs and objects
print(expression_list)
#########

##### Query if geneID from chr1 list objects is present in our RNAseq data and then output
# for gene in de_genes.degenes:
# 	if gene.ID in chr1_genes:
# 		print(gene.ID, gene.foldchange[12])
