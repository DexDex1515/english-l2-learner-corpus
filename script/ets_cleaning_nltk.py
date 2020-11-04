import pandas as pd
import numpy as np
import nltk

# Data paths
ZHO_path = 'data/mandarin_only/'

# Split dataframe for Mandarin L1
index = pd.read_csv('data/ETS_Corpus_of_Non-Native_Written_English/data/text/index.csv')
mandarin_L1 = index.loc[index['Language'] == 'ZHO']

# File names as lists
ZHO_file = mandarin_L1['Filename'].to_list()

ZHO_length = []
ZHO_num_sentences = []
ZHO_the_count = []
ZHO_aan_count = []
ZHO_one_count = []
ZHO_this_count = []
ZHO_that_count = []
ZHO_these_count = []
ZHO_those_count = []
ZHO_noun_count = []
ZHO_verb_count = []
ZHO_modal_count = []
ZHO_adj_count = []

puncs = [',', '.', '!', '?', ':', ';', '(', ')', "'", '"']
verb_tag = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
noun_tag = ['NN', 'NNS', 'NNS', 'NNP', 'NNPS']
adj_tag = ['JJ', 'JJR', 'JJS']
for f in ZHO_file:
	f_name = ZHO_path + f
	temp = open(f_name, 'r')
	num_sentence = 0
	ones = 0
	determiners = []
	nouns = []
	verbs = []
	adjs = []
	modal = []
	words = 0 # number of words
	for line in temp:
		arr = line.strip().split()
		if not len(arr) == 0:
			line_tokenized = nltk.word_tokenize(line.lower())
			tagged = [list(ele) for ele in nltk.pos_tag(line_tokenized)]
			tagged = [ele for ele in tagged if ele[0] not in puncs] # leave out punctuations
			words += len(tagged)
			one = np.array([x for x in tagged if x[0] == 'one'])
			dt = np.array([x for x in tagged if x[1] == 'DT'])
			n = np.array([x for x in tagged if x[1] in noun_tag])
			v = np.array([x for x in tagged if x[1] in verb_tag])
			a = np.array([x for x in tagged if x[1] in adj_tag])
			m = np.array([x for x in tagged if x[1] == 'MD'])
			ones += len(one)
			if dt.shape[0] != 0:
				determiners += list(dt[:, 0])
			if n.shape[0] != 0:
				nouns += list(n[:, 0])
			if v.shape[0] != 0:
				verbs += list(v[:, 0])
			if a.shape[0] != 0:
				adjs += list(a[:, 0])
			if m.shape[0] != 0:
				modal += list(m[:, 0])
			num_sentence += 1
	temp.close()
	# Counting
	ZHO_length.append(words)
	ZHO_num_sentences.append(num_sentence)
	ZHO_one_count.append(ones)
	ZHO_the_count.append(determiners.count('the'))
	ZHO_aan_count.append(determiners.count('a') + determiners.count('an'))
	ZHO_this_count.append(determiners.count('this'))
	ZHO_that_count.append(determiners.count('that'))
	ZHO_these_count.append(determiners.count('these'))
	ZHO_those_count.append(determiners.count('those'))
	ZHO_noun_count.append(len(nouns))
	ZHO_verb_count.append(len(verbs))
	ZHO_adj_count.append(len(adjs))
	ZHO_modal_count.append(len(modal))

mandarin_L1['essay_len'] = ZHO_length
mandarin_L1['num_sentence'] = ZHO_num_sentences

mandarin_L1['noun_count'] = ZHO_noun_count
mandarin_L1['verb_count'] = ZHO_verb_count
mandarin_L1['adj_count'] = ZHO_adj_count
mandarin_L1['modal_count'] = ZHO_modal_count
mandarin_L1['noun/sentence'] = mandarin_L1['noun_count'] / mandarin_L1['num_sentence']
mandarin_L1['verb/sentence'] = mandarin_L1['verb_count'] / mandarin_L1['num_sentence']
mandarin_L1['adj/sentence'] = mandarin_L1['adj_count'] / mandarin_L1['num_sentence']
mandarin_L1['modal/sentence'] = mandarin_L1['modal_count'] / mandarin_L1['num_sentence']

mandarin_L1['the_count'] = ZHO_the_count
mandarin_L1['aan_count'] = ZHO_aan_count
mandarin_L1['one_count'] = ZHO_one_count
mandarin_L1['this_count'] = ZHO_this_count
mandarin_L1['that_count'] = ZHO_that_count
mandarin_L1['these_count'] = ZHO_these_count
mandarin_L1['those_count'] = ZHO_those_count
mandarin_L1['the_freq'] = mandarin_L1['the_count'] / mandarin_L1['essay_len']
mandarin_L1['aan_freq'] = mandarin_L1['aan_count'] / mandarin_L1['essay_len']
mandarin_L1['one_freq'] = mandarin_L1['one_count'] / mandarin_L1['essay_len']
mandarin_L1['this_freq'] = mandarin_L1['this_count'] / mandarin_L1['essay_len']
mandarin_L1['that_freq'] = mandarin_L1['that_count'] / mandarin_L1['essay_len']
mandarin_L1['these_freq'] = mandarin_L1['these_count'] / mandarin_L1['essay_len']
mandarin_L1['those_freq'] = mandarin_L1['those_count'] / mandarin_L1['essay_len']

mandarin_L1.to_csv('cleaned_csv/mandarin_L1_nltk.csv', index = False, header = True)