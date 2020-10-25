import nltk.data
#nltk.download('punkt')
import os
import csv
from pdb import set_trace as bp

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
DATA_DIR = "../data/OANC-GrAF/data/written_2/technical/plos_txt/"

csv_file = open('plos.csv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerow(['file_id', 'num_sent', 'count_the', 'count_this', 'count_that', 'count_these', 'count_those', 'count_a', 'count_an', 'count_one'])

with os.scandir(DATA_DIR) as all_files:
    for entry in all_files:
        data = open(os.path.join(DATA_DIR, entry.name))

        tokenized_sentences = sent_detector.tokenize(data.read().replace("\n", " ").replace("\t", ""))
        #print(tokenized_sentences)
        num_sent = len(tokenized_sentences)

        word_freq = {
            "the" : 0,
            "this" : 0,
            "that" : 0,
            "these" : 0,
            "those" : 0,
            "a" : 0, 
            "an" : 0, 
            "one" : 0
        }

        for sentence in tokenized_sentences:
            for word in sentence.split():
                cleaned_word = word.lower().strip(",.!?#'\"")
                if cleaned_word in word_freq:
                    word_freq[cleaned_word] += 1
        csv_writer.writerow([entry.name, num_sent] + list(word_freq.values()))

csv_file.close()

