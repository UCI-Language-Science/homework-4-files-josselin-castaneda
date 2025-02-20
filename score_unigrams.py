# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf
import csv
from pathlib import Path


#######################
def score_unigrams(trainingfiles, testfile, outputfile):
    
    contents_list = []
    training_path = Path(trainingfiles)
    txt_files = training_path.glob("*.txt")


#txt files contents in list
    for txt_file in txt_files:
        with open(txt_file, "r") as file:
            contents = file.read().lower().split()
            contents_list.extend(contents)

#counting how many times each character is counted
    word_counter = {}
    for word in contents_list:
        word_counter[word] = word_counter.get(word,0) + 1 
    total_words = sum(word_counter.values())

    word_probability = {word: count/ total_words for word, count in word_counter.items()}

#sentence prob
    sent_prob = []

    with open(testfile, "r") as file:
        for line in file:
            sentence = line.strip()
            no_caps_sent = sentence.lower()
            words = no_caps_sent.split()

#log probabilities
            log_prob = 0 
            for word in words:
                if word in word_probability:
                    log_prob += log(word_probability[word])
                else:
                    log_prob = -inf
                    break
            sent_prob.append((sentence, log_prob))

#write results to CSV
    with open(outputfile, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["sentence","unigram_prob"])
        writer.writeheader()

        for sentence, prob in sent_prob:
            if prob == -inf:
                writer.writerow({"sentence": sentence, "unigram_prob": "-inf"})
            else:
                writer.writerow({"sentence": sentence, "unigram_prob": str(prob)})

    return None
#######################

# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
