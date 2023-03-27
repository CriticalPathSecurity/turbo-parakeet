# Quick Python script for changing the meta.do_notice flag

import os

input_folder = "/usr/local/zeek/share/zeek/site/Zeek-Intelligence-Feeds"
output_folder = "/usr/local/zeek/share/zeek/site/Zeek-Intelligence-Feeds-Modified"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".intel"):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        with open(input_file_path, "r") as infile, open(output_file_path, "w") as outfile:
            for line in infile:
                if line.startswith("#fields"):
                    outfile.write(line)
                else:
                    parts = line.strip().split("\t")
                    if len(parts) > 4:
                        parts[4] = "T"
                    modified_line = "\t".join(parts) + "\n"
                    outfile.write(modified_line)

print("Processing complete. Modified files can be found in", output_folder)
