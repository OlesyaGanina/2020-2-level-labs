"""
Concordance implementation starter
"""

from main import read_from_file
import os

if __name__ == '__main__':
    #  use data.txt file to test your program
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data = read_from_file(os.path.join(current_dir, 'data.txt'))
    stop_words = ['the', 'of']

    #  here goes your logic: calling methods from concordance.py

    tokens = main.tokenize(data)
    print("tokens:", tokens[:15])

    tokens_stop_words = main.remove_stop_words(tokens, stop_words)
    print("tokens without stop words:", tokens_stop_words[:100])

    frequencies = main.calculate_frequencies(tokens_stop_words[:600])
    print("frequencies:", frequencies[tokens_stop_words[0]])

    top_words = main.get_top_n_words(frequencies, 5)
    print("top words:", top_words)

    concordance = main.get_concordance(tokens, 'time', 1, 3)
    print(" concordance:", concordance[:3])

    RESULT = top_words
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT == ['a', 'time', 'main', 'season', 'presented'],'Concordance not working'
