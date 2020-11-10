import nltk.data
#nltk.download('punkt')
import os
import csv
from pdb import set_trace as bp

# download the English tokenizer from NLTK
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

DATA_DIR = "../data/OANC-GrAF/data/written_1/journal/verbatim_txt/"
CSV_FILE_NAME = 'verbatim.csv'

csv_file = open(CSV_FILE_NAME, 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerow(
    ['file_id', 'num_sent', 'word_count', 'count_the', 'count_this', 'count_that', 'count_these', 'count_those', 'count_a', 'count_an', 'count_one', 'freq_the', 'freq_this', 'freq_that', 'freq_these', 'freq_those', 'freq_a', 'freq_an', 'freq_one'])

with os.scandir(DATA_DIR) as all_files:
    for entry in all_files:
        data = open(os.path.join(DATA_DIR, entry.name))

        tokenized_sentences = sent_detector.tokenize(data.read().replace("\n", " ").replace("\t", ""))
        #print(tokenized_sentences)
        num_sent = len(tokenized_sentences)

        word_count = {
            "the" : 0,
            "this" : 0,
            "that" : 0,
            "these" : 0,
            "those" : 0,
            "a" : 0, 
            "an" : 0, 
            "one" : 0
        }

        all_word_count = 0

        for sentence in tokenized_sentences:
            sentences = sentence.split()
            all_word_count += len(sentences)
            for word in sentences:
                cleaned_word = word.lower().strip(",.!?#()[]{}'\"")
                if cleaned_word in word_count:
                    word_count[cleaned_word] += 1

        word_freq = {
            "the" : 0.0,
            "this" : 0.0,
            "that" : 0.0,
            "these" : 0.0,
            "those" : 0.0,
            "a" : 0.0, 
            "an" : 0.0, 
            "one" : 0.0
        }
        for word in word_freq:
            word_freq[word] = word_count[word] / all_word_count 

        csv_writer.writerow([str(entry.name).strip('.txt'), num_sent, all_word_count] + list(word_count.values()) + list(word_freq.values()))

csv_file.close()

