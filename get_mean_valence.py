# The file valence_data/winter_2016_senses_valence.csv contains data from an 
# experiment that asked people to provide valence ratings for words associated
# with each of the five senses (touch, taste, smell, sight, sound). The file has
# three columns: Word, Modality, and Val. Word contains the word, Modality the
# sensory modality, and Val contains the mean valence rating for that word,
# where higher valence corresponds to more positive emotional states.

# The question we'll try to answer is whether certain sensory modalities have 
# higher or lower mean valences than others.
# 
#  Write a function called get_mean_valence that takes a Path to a CSV file
#  as input. You can assume the file will be formatted as described above.
#  Your function should return a dictionary with keys corresponding to each
#  of the five modalities. The value for each key should be its mean valence
#  score across all of the words in the CSV file.

# The data are from the paper 
#
# Winter, B. (2016). Taste and smell words form an affectively loaded and emotionally
# flexible part of the English lexicon. Language, Cognition and Neuroscience, 31(8), 
# 975-988.

#######################
import csv
def get_mean_valence (Path):
    modalities_with_averages = {}
    modalities_with_val = {}
    modalities_count = {}
    with open (Path) as file:
        reader = csv.DictReader(file)
        modalities = [row for row in reader]
    for word_info in modalities:
        modality = word_info['Modality']
        valence = float(word_info['Val'])
        if modality not in modalities_with_val:
            modalities_with_val[modality] = 0
            modalities_count[modality] = 0
        modalities_with_val[modality] += valence
        modalities_count[modality] += 1
    for key in modalities_with_val:
        modalities_with_averages[key] = modalities_with_val[key]/modalities_count[key]

    return modalities_with_averages
    
#######################

# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    print(get_mean_valence('valence_data/winter_2016_senses_valence.csv'))
    expected_results = {
        'Touch': 5.534434953514706, 
        'Sight': 5.579663071651515, 
        'Taste': 5.808123902468085, 
        'Smell': 5.471011590120001, 
        'Sound': 5.405192706701493
    }
    
    pass 
