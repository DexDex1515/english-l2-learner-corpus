import os 
from shutil import copy
from pdb import set_trace as bp

PLOS_DIR = "../OANC-GrAF/data/written_2/technical/plos"
PLOS_DIR_TXT = "../data/OANC-GrAF/written_2/technical/plos_txt"
with os.scandir(PLOS_DIR) as all_files:
    for entry in all_files:
        #extract only the txt files
        if str(entry.name).endswith(".txt"):
            copy(os.path.join(PLOS_DIR, entry.name), PLOS_DIR_TXT)