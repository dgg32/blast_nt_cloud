#!/bin/sh
#$ -S /bin/bash



STR=$(find $1 -maxdepth 1 \( -name "*.fasta" -or -name "*.fa" \) | head -n $SLURM_ARRAY_TASK_ID | tail -n 1)


#/home/sih13/tool/blast/blastp -db /home/sih13/database/md5nr/md5nr_no_hyphen -query $STR -num_threads 1 -max_target_seqs 10 -evalue 1e-10 -outfmt 6

#cat $STR  | /megx/home/shuang/SilmarilX2/Darkhorse_for_SGE_stdin_tab/Darkhorse_for_SGE -d -k -o $STR -p $2 -t $3
outfile=$STR"_blast_out.txt"

#blastn -max_target_seqs 1 -db /home/scratch/databases/blast/nt_20161019/nt -query $STR -num_threads 28 -outfmt '6 qseqid stitle pident length evalue staxids' -out $outfile



#######for megan
#blastn -max_target_seqs 1 -db $2 -query $STR -num_threads 28 -outfmt 7 -out $outfile


#blastn -max_target_seqs 20 -db $2 -query $STR -num_threads 4 -task 'blastn' -outfmt '6 qaccver saccver pident qcovs length mismatch gapopen qstart qend sstart send evalue bitscore' -out $outfile



######
blastn -max_target_seqs 20 -db $2 -query $STR -num_threads 14 -outfmt '6 qaccver saccver pident qcovs length mismatch gapopen qstart qend sstart send evalue bitscore stitle staxids' -out $outfile
