# ENGETO_PYTHON_PROJECT_3
The third project within the Python Academy course by Engeto.
## Project assignment
### Description
The final project of the Python Academy course focused on creation of a program for extraction of the results of the 2017 parliamentary elections in the Czech Republic for a selected district. You can view the official source[here](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).
### Project procedure
1. Creation of virtual environment dedicated exclusively to this project
2. Installation of the necessary third-party libraries into the created environment using an IDE or the command line
3. Generation of a "requirements.txt" file that automatically records a list of all used libraries including their versions (the file is not to be written manually)
4. Running of the program using two command-line arguments – the first argument represents the URL of the target data source, the second is the name of the output file. The input() function is not to be used
5. Validation of the input arguments – if they are missing, in the wrong order or contain an invalid URL, the program should notify the user and terminate
6. Creation of a "readme.md" file that provides an overview of the project, instructions for installing dependencies from the "requirements.txt" file, how to run the program, and optionally a sample example with specific parameters and output.
### Project requirements
1. The code must contain a header with the contact details of the author of the project
2. A program file (script) with the .py extension, which requires 2 arguments to run properly
3. A file with list of only the relevant libraries and their versions for the project (requirements.txt)
4. Brief documentation(description, library installation, example) - "readme.md"
5. A file with the saved output (.csv)
6. Code organized into short and clear functions.
## Brief documentation
### Libraries installation
The libraries used in this project are listed in the attached requirements.txt file. For installation, it is recommended to create a new virtual environment and proceed in the console as follows using the installed package manager:

	Package manager version verification: pip --version
	Libraries installation: pip install -r requirements.txt	

### Running the project
To successfully run the "election_scraper.py" file, two required arguments must be entered into the console command line:

	Python election_scraper.py "territorial_unit_link" "output_file" 

Once executed, the script will download the election results and save them into a file with the .csv extension.
### Project example
Voting results for the Frýdek-Místek district:

	1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102
	2. argument: results_frýdek-místek.csv

Program execution:

	Python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102" "results_frýdek-místek.csv"

Download progress:

	Initiating data scraping from selected URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102
	Saving data into file: results_frýdek-místek.csv
	10% complete
	20% complete
	30% complete
	40% complete
	50% complete
	60% complete
	70% complete
	80% complete
	90% complete
	100% complete. Your file "results_frýdek-místek.csv" is ready for use.

Partial output:

	code;location;registered;envelopes;valid...
	598011;Baška;3 093;2 065;2 053;175;1;1;124;1;49;192;21;12;21;1;0;216;0;0;44;665;2;9;194;1;16;7;3;293;5
	598020;Bílá;285;178;178;19;0;0;14;0;10;21;3;1;0;1;0;12;1;0;3;52;0;0;15;0;3;0;0;23;0
	511633;Bocanovice;358;197;197;20;0;0;32;0;3;13;3;1;0;0;0;18;0;1;1;45;0;0;43;0;0;0;0;17;0...





