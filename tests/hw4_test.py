import csv
import pytest

from pathlib import Path

def test_score_unigrams(monkeypatch, capsys):
    from score_unigrams import score_unigrams
    expected_probs = [
        {'sentence': 'It was the best of times , it was the worst of times .', 
        'unigram_prob': '-73.42220869430832'}, 
        {'sentence': 'There is no exquisite beauty without some strangeness in the proportion .', 
        'unigram_prob': '-84.09038166084301'},
        {'sentence': 'We tell ourselves stories in order to live .', 
        'unigram_prob': '-65.50666393502672'}, 
        {'sentence': 'Make it a rule never to give a child a book you would not read yourself .', 
        'unigram_prob': '-104.69385748118941'}, 
        {'sentence': 'The sky above the port was the color of television , tuned to a dead channel .', 
        'unigram_prob': '-inf'}
    ]
    result = score_unigrams(
        Path('training_data'), 
        Path('test_data/test_sentences.txt'), 
        Path('output.csv'))
    
    assert result == None

    with open(Path('output.csv')) as f:
        reader = csv.DictReader(f)
        rows = [x for x in reader]
        for i, row in enumerate(rows):
            assert row['sentence'].strip() == expected_probs[i]['sentence']
            assert row['unigram_prob'] == pytest.approx(expected_probs[i]['unigram_prob'])

def test_get_mean_valence():
    from get_mean_valence import get_mean_valence
    expected_results = {
        'Touch': 5.534434953514706, 
        'Sight': 5.579663071651515, 
        'Taste': 5.808123902468085, 
        'Smell': 5.471011590120001, 
        'Sound': 5.405192706701493
    }

    result = get_mean_valence(Path('valence_data', 'winter_2016_senses_valence.csv'))
    
    for key, val in result.items():
        assert val == pytest.approx(expected_results[key])
