import nltk.data
from nltk.stem.snowball import SnowballStemmer
#nltk.download('punkt')
import os
import csv
from pdb import set_trace as bp

# download the English tokenizer from NLTK
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
stemmer = SnowballStemmer("english")

# build a dictionary that maps each essay's file id to its score level
INDEX_FILE = "../data/ETS_Corpus_of_Non-Native_Written_English/data/text/index.csv"
score_dict = {}
with open(INDEX_FILE) as index_csv:
    reader = csv.DictReader(index_csv)
    for row in reader:
        score_dict[row["Filename"]] = row["Score Level"]

DATA_DIR = "../data/ETS_Corpus_of_Non-Native_Written_English/data/text/responses/spanish_only/"
CSV_FILE_NAME = '../cleaned_csv/spanish_l1_lemmatizer_column.csv'

csv_file = open(CSV_FILE_NAME, 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
#csv_writer.writerow(
#    ['file_id', 'score_level', 'num_sent', 'word_count', 'average_sent_length', 'count_the', 'count_this', 'count_that', 'count_these', 'count_those', 'count_a', 'count_an', 'count_one', 'freq_the', 'freq_this', 'freq_that', 'freq_these', 'freq_those', 'freq_a', 'freq_an', 'freq_one'])
csv_writer.writerow(['file_id', 'num_uniq_word'])

with os.scandir(DATA_DIR) as all_files:
    for entry in all_files:
        data = open(os.path.join(DATA_DIR, entry.name))

        tokenized_sentences = sent_detector.tokenize(data.read().replace("\n", " ").replace("\t", ""))
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
        unique_words = set()

        for sentence_string in tokenized_sentences:
            sentence = sentence_string.split()

            #remove puncts before counting sentence length
            punct = [',', '.', '!', '?', ':', ';', '(', ')', "'", '"']
            cleaned_sentence = []
            for word in sentence:
                if word not in punct:
                    cleaned_sentence.append(word)

            all_word_count += len(cleaned_sentence)

            for word in cleaned_sentence:
                cleaned_word = word.lower().strip(",.!?#()[]{}'\"")
                stemmed_word = stemmer.stem(cleaned_word)
                if stemmed_word not in unique_words:
                    unique_words.add(stemmed_word)
                
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

        #row_to_write = [str(entry.name), score_dict[entry.name], num_sent, all_word_count, (all_word_count / num_sent)] + list(word_count.values()) + list(word_freq.values())
        row_to_write = [str(entry.name), len(unique_words)]
        csv_writer.writerow(row_to_write)

csv_file.close()

