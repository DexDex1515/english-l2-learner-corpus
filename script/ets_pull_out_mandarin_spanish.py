import csv
import os 
from shutil import copy
from pdb import set_trace as bp

mandarin_ids = set()
spanish_ids = set()

with open("../text/index.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        file_name = row["Filename"]
        lang = row["Language"]
        if lang == "ZHO": #mandarin files
            mandarin_ids.add(file_name)
        elif lang == "SPA":
            spanish_ids.add(file_name)

ESSAY_DIR = '../data/ETS_Corpus_of_Non-Native_Written_English/text/responses/tokenized'
MANDARIN_DIR = '../data/ETS_Corpus_of_Non-Native_Written_English/text/responses/mandarin_only/'
mandarin_dict = {}

with os.scandir(ESSAY_DIR) as all_essays:
    for entry in all_essays:
        if entry.name in mandarin_ids:
            with open(os.path.join(ESSAY_DIR, entry.name)) as essay:
                mandarin_dict[entry.name] = essay.read()
                copy(os.path.join(ESSAY_DIR, entry.name), MANDARIN_DIR)

SPANISH_DIR = '../data/ETS_Corpus_of_Non-Native_Written_English/text/responses/spanish_only/'
spanish_dict = {}

with os.scandir(ESSAY_DIR) as all_essays:
    for entry in all_essays:
        if entry.name in spanish_ids:
            with open(os.path.join(ESSAY_DIR, entry.name)) as essay:
                spanish_dict[entry.name] = essay.read()
                copy(os.path.join(ESSAY_DIR, entry.name), SPANISH_DIR)
