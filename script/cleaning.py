import os
import pandas as pd

# Data paths
ZHO_path = 'data/mandarin_only/'
SPA_path = 'data/spanish_only/'

# Split dataframe for Mandarin L1 and Spanish L1
index = pd.read_csv('data/ETS_Corpus_of_Non-Native_Written_English/data/text/index.csv')
mandarin_L1 = index.loc[index['Language'] == 'ZHO']
spanish_L1 = index.loc[index['Language'] == 'SPA']

# File names as lists
ZHO_file = mandarin_L1['Filename'].to_list()
SPA_file = spanish_L1['Filename'].to_list()
corpus_ZHO = []
corpus_SPA = []
ZHO_length = [] # lengths of essays
SPA_length = []
ZHO_num_sentences = [] # number of sentences
SPA_num_sentences = []

'''Read in both corpora'''
puncs = [',', '.', '!', '?', ':', ';', '(', ')', "'", '"']
for f in ZHO_file:
    f_name = ZHO_path + f
    temp = open(f_name, 'r')
    essay = []
    num_sentence = 0
    for line in temp:
        arr = line.strip().split()
        essay += arr
        if not len(arr) == 0:
            num_sentence += 1
    temp.close()
    essay = [x for x in essay if x not in puncs] # leave out punctuations
    corpus_ZHO.append(essay)
    ZHO_length.append(len(essay))
    ZHO_num_sentences.append(num_sentence)
mandarin_L1['essay_len'] = ZHO_length
mandarin_L1['num_sentence'] = ZHO_num_sentences
for f in SPA_file:
    f_name = SPA_path + f
    temp = open(f_name, 'r')
    essay = []
    num_sentence = 0
    for line in temp:
        arr = line.strip().split()
        essay += arr
        if not len(arr) == 0:
            num_sentence += 1
    temp.close()
    essay = [x for x in essay if x not in puncs] # leave out punctuations
    corpus_SPA.append(essay)
    SPA_length.append(len(essay))
    SPA_num_sentences.append(num_sentence)
spanish_L1['essay_len'] = SPA_length
spanish_L1['num_sentence'] = SPA_num_sentences

'''Counts and frequencies'''
# ZHO L1
ZHO_the_count = []
ZHO_the_freq = []
ZHO_aan_count = []
ZHO_aan_freq = []
ZHO_demo_sing_count = [] # demonstratives singular
ZHO_demo_sing_freq = []
ZHO_demo_pl_count = [] # demonstratives plural
ZHO_demo_pl_freq = []

# SPA L1
SPA_the_count = []
SPA_the_freq = []
SPA_aan_count = []
SPA_aan_freq = []
SPA_demo_sing_count = [] # demonstratives singular
SPA_demo_sing_freq = []
SPA_demo_pl_count = [] # demonstratives plural
SPA_demo_pl_freq = []

for i in range(len(corpus_ZHO)):
    # the
    num_the = corpus_ZHO[i].count('the')
    ZHO_the_count.append(num_the)
    ZHO_the_freq.append(float(num_the / ZHO_length[i]))

    # a, an
    num_ind = corpus_ZHO[i].count('a') + corpus_ZHO[i].count('an')
    ZHO_aan_count.append(num_ind)
    ZHO_aan_freq.append(float(num_ind / ZHO_length[i]))

    # demonstratives
    num_dem_sing = corpus_ZHO[i].count('this') + corpus_ZHO[i].count('that')
    ZHO_demo_sing_count.append(num_dem_sing)
    ZHO_demo_sing_freq.append(float(num_dem_sing / ZHO_length[i]))
    num_dem_pl = corpus_ZHO[i].count('these') + corpus_ZHO[i].count('those')
    ZHO_demo_pl_count.append(num_dem_pl)
    ZHO_demo_pl_freq.append(float(num_dem_pl / ZHO_length[i]))

for i in range(len(corpus_SPA)):
    # the
    num_the = corpus_SPA[i].count('the')
    SPA_the_count.append(num_the)
    SPA_the_freq.append(float(num_the / SPA_length[i]))

    # a, an
    num_ind = corpus_SPA[i].count('a') + corpus_SPA[i].count('an')
    SPA_aan_count.append(num_ind)
    SPA_aan_freq.append(float(num_ind / SPA_length[i]))

    # demonstratives
    num_dem_sing = corpus_SPA[i].count('this') + corpus_SPA[i].count('that')
    SPA_demo_sing_count.append(num_dem_sing)
    SPA_demo_sing_freq.append(float(num_dem_sing / SPA_length[i]))
    num_dem_pl = corpus_SPA[i].count('these') + corpus_SPA[i].count('those')
    SPA_demo_pl_count.append(num_dem_pl)
    SPA_demo_pl_freq.append(float(num_dem_pl / SPA_length[i]))

# Add columns to the dataframes
mandarin_L1['the_count'] = ZHO_the_count
mandarin_L1['the_freq'] = ZHO_the_freq
mandarin_L1['aan_count'] = ZHO_aan_count
mandarin_L1['aan_freq'] = ZHO_aan_freq
mandarin_L1['demo_sing_count'] = ZHO_demo_sing_count
mandarin_L1['demo_sing_freq'] = ZHO_demo_sing_freq
mandarin_L1['demo_pl_count'] = ZHO_demo_pl_count
mandarin_L1['demo_pl_freq'] = ZHO_demo_pl_freq
 
spanish_L1['the_count'] = SPA_the_count
spanish_L1['the_freq'] = SPA_the_freq
spanish_L1['aan_count'] = SPA_aan_count
spanish_L1['aan_freq'] = SPA_aan_freq
spanish_L1['demo_sing_count'] = SPA_demo_sing_count
spanish_L1['demo_sing_freq'] = SPA_demo_sing_freq
spanish_L1['demo_pl_count'] = SPA_demo_pl_count
spanish_L1['demo_pl_freq'] = SPA_demo_pl_freq

# output csv files
mandarin_L1.to_csv('cleaned_csv/mandarin_L1.csv', index = False, header = True)
spanish_L1.to_csv('cleaned_csv/spanish_L1.csv', index = False, header = True)