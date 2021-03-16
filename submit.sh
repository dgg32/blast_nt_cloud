#!/bin/bash

#qsub -tc 30 -e /home/sih13/sge-log-files/ -o $1 -t 1-$(find $1 -maxdepth 1 -name "*.fasta_*"|wc -l) importer.sh $1

sbatch -c 14 -p long --mem=128G --error $1/error.txt --output $1/output.txt --array=1-$(find $1 -maxdepth 1 \( -name "*.fasta" -or -name "*.fa" \) |wc -l)%30 importer.sh $1 $2
#sbatch -c 1 -p long --mem=1G --error $1/error.txt --output $1/output.txt --array=1-$(find $1 -maxdepth 1 -name "*.fasta" -or -name "*.fa" |wc -l)%30 importer.sh $1 $2
