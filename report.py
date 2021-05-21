import sys, re, json, os

top_folder = sys.argv[1]

folder_bin_info = {}

tools = set()

cleaning = [".fa_blast_out.txt", "final.contigs.fa.metabat-bins1500_", "o_DASTool_bins_", "bin_", ".fasta", ".fa"]

for (head, dirs, files) in os.walk(top_folder):
    for file in files:
        current_file_path = os.path.abspath(os.path.dirname(os.path.join(head, file)))
        with_name = current_file_path + "/"+ file
        if file.endswith("blast_cloud.txt"):

            folder_name = ""
            tool = ""
            for line in open(with_name, 'r'):
                line = line.strip()

                if line != "":
                    if "\t" not in line:
                        folder_name = line
                        tool = folder_name.split("_")[-1]

                        tools.add(tool)
                    else:
                        fields = line.split("\t")

                        bin = fields[0].replace(folder_name + "_", "")

                        for c in cleaning:
                            bin = bin.replace(c, "")

                        info = fields[1]

                        if tool not in folder_bin_info:
                            folder_bin_info[tool] = {}
                        
                        if bin not in folder_bin_info[tool]:
                            folder_bin_info[tool][bin] = {}
                        folder_bin_info[tool][bin]["blast_cloud"] = info

        
        elif file.endswith("checkm_summary.txt"):
            is_header = False
            tool = ""
            for line in open(with_name, 'r'):
                line = line.strip()

                if line != "":
                    if "\t" not in line:
                        tool = line.replace("_checkm", "").split("_")[-1]

                    else:
                        if is_header == False:
                            is_header = True
                        else:
                            fields = line.split("\t")

                            bin = fields[0]
                            info = fields[1:]

                            if tool not in folder_bin_info:
                                folder_bin_info[tool] = {}
                            if bin not in folder_bin_info[tool]:
                                folder_bin_info[tool][bin] = {}
                            
                            folder_bin_info[tool][bin]["checkm"] = info
                else:
                    is_header = False
        
        elif file.endswith("_coverage.txt"):
            tool = file.replace("_coverage.txt", "").lower()

            for line in open(with_name, 'r'):
                line = line.strip()

                if line != "":
                    fields = line.split("\t")
                    bin = fields[0]

                    for c in cleaning:
                        bin = bin.replace(c, "")

                    info = fields[1]

                    if tool not in folder_bin_info:
                        folder_bin_info[tool] = {}
                        
                    if bin not in folder_bin_info[tool]:
                        folder_bin_info[tool][bin] = {}
                           
                    folder_bin_info[tool][bin]["coverage"] = info

#print (folder_bin_info["maxbin"])
#print (folder_bin_info["concoct"])
#print (folder_bin_info["metabat"])
#print (folder_bin_info["das"])

print ("\t".join(["tool", "bin", "marker lineage", "Completeness", "Contamination", "Mean contig length", "N50 (contigs)", "Coding density", "# contigs", "Genome size", "GC", "coverage", "blast_cloud"]))

for tool in tools:
    

    
    for bin in folder_bin_info[tool]:
        content = f"{tool}\t"
        content += bin + "\t"
       
        content += "\t".join(folder_bin_info[tool][bin]["checkm"])

        content += "\t" + folder_bin_info[tool][bin]["coverage"]

        #if folder_bin_info[tool][bin]["blast_cloud"] != "[]":
        content += "\t" + folder_bin_info[tool][bin]["blast_cloud"]

        print (content)

