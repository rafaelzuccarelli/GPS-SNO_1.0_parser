#!/usr/bin/env python3
import sys
import os

wd = os.getcwd()
print('Reading dictionaries...')
input_directory = wd + '/Input'n

for currentpath, folders, files in os.walk(input_directory):
	for file in files:
		input_file_path = input_directory + '/' + file
		input_file = open(input_file_path, 'r', encoding = "utf-8")
		input_clean_2 = open(input_file_path, 'r', encoding = "utf-8")

		
		input_file_name = input_file_path.split('/')
		#print(input_file_name[-1])

		input_fasta = wd
                + '/Output/'
                + input_file_name[-1]
                + "_output_clean.txt"
		
		output_clean = wd
                + '/Output/'
                + input_file_name[-1]
                + "_output_clean.txt"
                
		output_txt = open(output_clean, 'w')
		
		output_clean_table = wd
                + '/Output/'
                + input_file_name[-1]
                + '_output_clean_table.csv'
                
		output_csv = open(output_clean_table, 'w')

		output_fasta_header = wd
                + '/Output/'
                + input_file_name[-1]
                + '_output_fasta_header.txt'
                
		output_header = open(output_fasta_header, 'w')

		output_ID_path = wd
                + '/Output/'
                + input_file_name[-1]
                + '_output_ID.txt'
                
		output_ID = open(output_ID_path, 'w')

		current_seq = ''
		current_header = ''
		for line in input_file:
			if line.startswith('>'):
				if current_seq != '':
					output_txt.write(current_header + current_seq)
					#print(current_header + current_seq, end="")
					current_header = line
					current_seq = ''
			else:
				current_seq += line
		if current_seq != '':
			output_txt.write(current_header + current_seq)


		input_fasta_file = wd
                + '/Output/'
                + input_file_name[-1]
                + "_output_clean.txt"
                
		input_fasta = open(input_fasta_file, 'r', encodifng = "utf-8")
		header = ''

		#create a file with only the Solycs for header only file
		#create a file with only the Solyc number

		ID = []
		for line in input_fasta:
			if line.startswith('>'):
				ID_list = line.split(' ')
				Solyc = ID_list[0].lstrip('>')
				print(Solyc)
				output_ID.write(Solyc + '\n')
				output_header.write(line.lstrip('>'))
		

		#creates a .csv file of the cleaned output file
		gene_ID = ''
		results = ''
		position = ''
		peptide = ''
		score = ''
		cutoff = ''
		cluster = ''
		results_line_output = ''
                
		for line in input_clean_2:
			if line.startswith('>'):
				output_csv.write(results_line_output)
				#print(results_line_output)
				gene_ID = str(line[1:19])
				position = ''
				peptide = ''
				score = ''
				cutoff = ''
				cluster = ''
			elif not line.startswith('>') and not line.startswith('Position'):
				results = line.split('\t')
				position += '|' + results[0]
				peptide += '|' + results[1]
				score += '|' + results[2]
				cutoff += '|' + results[3]
				cluster += '|' + results[4].rstrip('\n').replace('Cluster ', '')
				results_line_output = (gene_ID +'\t'
                                               + position +'|\t'
                                               + peptide + '|\t'
                                               + score + '|\t'
                                               + cutoff + '|\t'
                                               + cluster + '|\n')
			else:
				output_csv.write('Gene' + '\t'
                                        + 'Position' + '\t'
                                        + 'Pepitide' + '\t'
                                        + 'Score' + '\t'
                                        + 'Cutoff' + '\t'
                                        + 'Cluster' + '\n')
