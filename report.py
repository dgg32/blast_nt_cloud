import sys, re, json, os

top_folder = sys.argv[1]

project_tool_bin_info = {}

tools = set()

cleaning = [".fa_blast_out.txt", "final.contigs.fa.metabat-bins1500_", "o_DASTool_bins_", "bin_", ".fasta", ".fa"]

for (head, dirs, files) in os.walk(top_folder):
    for file in files:
        current_file_path = os.path.abspath(os.path.dirname(os.path.join(head, file)))
        with_name = current_file_path + "/"+ file
        if file.endswith("blast_cloud.txt"):

            project = ""
            tool = ""
            for line in open(with_name, 'r'):
                line = line.strip()

                if line != "":
                    if "\t" not in line:
                        folder_name = line
                        tool = folder_name.split("_")[-1]
                        project = folder_name.replace("_" + tool, "")

                        tools.add(tool)
                    else:
                        fields = line.split("\t")

                        bin = fields[0].replace(folder_name + "_", "")

                        for c in cleaning:
                            bin = bin.replace(c, "")

                        info = fields[1]

                        if project not in project_tool_bin_info:
                            project_tool_bin_info[project] = {}

                        if tool not in project_tool_bin_info[project]:
                            project_tool_bin_info[project][tool] = {}
                        
                        if bin not in project_tool_bin_info[project][tool]:
                            project_tool_bin_info[project][tool][bin] = {}
                        project_tool_bin_info[project][tool][bin]["blast_cloud"] = info

        
        elif file.endswith("checkm_summary.txt"):
            is_header = False
            project = ""
            tool = ""
            for line in open(with_name, 'r'):
                line = line.strip()

                if line != "":
                    
                    if "\t" not in line:
                        tool = line.replace("_checkm", "").split("_")[-1]
                        project = line.replace("_checkm", "").replace("_" + tool, "")

                    else:
                        if is_header == False:
                            is_header = True
                        else:
                            fields = line.split("\t")

                            bin = fields[0]
                            info = fields[1:]

                            if project not in project_tool_bin_info:
                                project_tool_bin_info[project] = {}

                            if tool not in project_tool_bin_info[project]:
                                project_tool_bin_info[project][tool] = {}
                            if bin not in project_tool_bin_info[project][tool]:
                                project_tool_bin_info[project][tool][bin] = {}
                            
                            project_tool_bin_info[project][tool][bin]["checkm"] = info
                else:
                    is_header = False
        
        elif file.endswith("_coverage.txt"):
            tool = file.replace("_coverage.txt", "").split("_")[-1]
            project = file.replace("_coverage.txt", "").replace("_" + tool, "")

            for line in open(with_name, 'r'):
                line = line.strip()

                if line != "":
                    fields = line.split("\t")
                    bin = fields[0]

                    for c in cleaning:
                        bin = bin.replace(c, "")

                    info = fields[1]

                    if project not in project_tool_bin_info:
                        project_tool_bin_info[project] = {}

                    if tool not in project_tool_bin_info[project]:
                        project_tool_bin_info[project][tool] = {}
                        
                    if bin not in project_tool_bin_info[project][tool]:
                        project_tool_bin_info[project][tool][bin] = {}
                           
                    project_tool_bin_info[project][tool][bin]["coverage"] = info

#print (project_tool_bin_info["maxbin"])
#print (project_tool_bin_info["concoct"])
#print (project_tool_bin_info["1e-3_b_s6__001"]["metabat"])
#print (project_tool_bin_info["1e-10_a_s19__001"])

print ("\t".join(["project", "tool", "bin", "marker lineage", "Completeness", "Contamination", "Mean contig length", "N50 (contigs)", "Coding density", "# contigs", "Genome size", "GC", "coverage", "blast_cloud"]))

for project in sorted(project_tool_bin_info):
    for tool in sorted(project_tool_bin_info[project]):
        
        for bin in sorted(project_tool_bin_info[project][tool]):
            content = f"{project}\t{tool}\t"
            content += bin + "\t"

            #print (project, tool)

            if "checkm" in project_tool_bin_info[project][tool][bin]:
                content += "\t".join(project_tool_bin_info[project][tool][bin]["checkm"])
            else:
                content += "\t".join([" "] * 9)

            if "coverage" in project_tool_bin_info[project][tool][bin]:
                content += "\t" + project_tool_bin_info[project][tool][bin]["coverage"]
            else:
                content += "\t".join([" "] * 1)

            if "blast_cloud" in project_tool_bin_info[project][tool][bin]:
                content += "\t" + project_tool_bin_info[project][tool][bin]["blast_cloud"]
            else:
                content += "\t".join([" "] * 1)

            print (content)

