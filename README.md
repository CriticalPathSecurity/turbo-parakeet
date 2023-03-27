# turbo-parakeet
Zeek Intelligence Feed Modifier

This Python script modifies the meta.do_notice field of all files ending in .intel in a given folder. It changes the value from "F" to "T" and saves the modified files in a separate output folder. This can be useful when working with Zeek intelligence feeds that need to have their notice behavior adjusted.

**Usage
Clone this repository or copy the zeek_intel_meta_modifier.py script to your local machine.

Make sure you have Python 3.x installed.

Update the input_folder and output_folder variables in the script to match your desired input and output directories:

<pre>
input_folder = "/path/to/your/input/folder"
output_folder = "/path/to/your/output/folder"
</pre>

**Run the script:
<pre>
python3 zeek_intel_meta_modifier.py
</pre>

The script will process all files with the .intel extension in the input folder, modify the meta.do_notice field to "T", and write the modified content to new files in the output folder.

**Disclaimer
Please ensure that the output folder is writable and the input folder contains the correct files. The script assumes that the files have the correct structure and will not perform extensive validation of the input data. Use at your own risk.