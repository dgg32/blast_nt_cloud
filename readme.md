###blast nt

./submit.sh [fasta_folder] [blast_db]



###word cloud, top folder of the projects, not bins


./folder.sh [metagenome_folder]

python blast_wordcloud.py [metagenome_folder] > [output.tsv]
