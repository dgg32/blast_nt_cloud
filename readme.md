###blast nt

./submit.sh [fasta_folder] [blast_db]



###word cloud, top folder of the projects, not bins


./folder.sh [metagenome_folder] [database]


find [metagenome_folder] \( -name "*_maxbin" -o -name "*_metabat" -o -name "*_concoct" -o -name "*_das" \)  -type d  -printf "\n\n%f\n" -exec python blast_wordcloud.py {} \;  > [metagenome_folder]/blast_cloud.txt


python report.py [metagenome_folder]  >  [metagenome_folder]/bin_report.tsv