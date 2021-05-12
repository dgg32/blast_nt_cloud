###blast nt

./submit.sh [fasta_folder] [blast_db]



###word cloud, top folder of the projects, not bins


find [metagenome_folder] \( -name "*_maxbin" -o -name "*_metabat" -o -name "*_concoct" -o -name "*_das" \)  -type d  -printf "\n\n%f\n" -exec python blast_wordcloud.py {} \;
python blast_wordcloud.py [fasta_folder] > [output.tsv]
