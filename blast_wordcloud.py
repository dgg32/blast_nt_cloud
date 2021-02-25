import os, sys, re, json
import pandas as pd
from collections import Counter

extension = "_blast_out.txt"

def isRomanNumeric(s):
    roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]

    for n in roman_numerals:
        s = s.replace(n, "")

    if s == "":
        return True
    else:
        return False

taboo = ["complete", "genome", "dna", "sequence", "sp.", "strain", "assembly", "taxon", "subsp.", "gene", "genomes"]

top_folder = sys.argv[1]

#qaccver saccver pident qcovs length mismatch gapopen qstart qend sstart send evalue bitscore stitle staxids
headers = ["qaccver", "saccver", "pident", "qcovs", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "stitle", "staxids"]

container = []

#print ("bin\t" + "\t".join(headers))

binname_sentence = {}

for (head, dirs, files) in os.walk(top_folder):
    for file in files:
        if file.endswith(extension):
            current_file_path = os.path.abspath(os.path.dirname(os.path.join(head, file)))
            with_name = current_file_path + "/"+ file

            binname = re.sub(r'\S+/', r'', head) + "_" + re.sub(r'(maxbin\.\d+\.fasta)\S+', r'\1', file)

            sentence = []
            #print (binname)

            df = pd.read_csv(with_name, sep = "\t", names=headers)

            for row in df[(df["evalue"] < 1e-10) & (df["pident"] > 90)]["stitle"].values:
                #print(row)
                sentence += [x for x in row.replace(",", "").replace(":", "").split(" ") if x != "" and not x.isdigit() and not isRomanNumeric(x) and x.lower() not in taboo]

            #print (sentence)
            if binname not in binname_sentence:
                binname_sentence[binname] = []

            binname_sentence[binname] += sentence



#print (binname_sentence)

for binname in binname_sentence:
    print (binname + "\t" + str([x for x in Counter(binname_sentence[binname]).most_common(20)]))
    

    #print (binname + "\t" + str([x for x in Counter(binname_sentence[binname]).most_common(20)]))
    
            
                

                    