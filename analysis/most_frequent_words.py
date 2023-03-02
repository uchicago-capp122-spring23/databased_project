"""
Project: CAPP 122 DataBased Project
File name: most_frequent_words.py

Finds and the most frequent words associated with a candidates and newspapers.

@Author: Madeleine Roberts
@Date: Mar 1, 2023
"""
import nltk
#nltk.download("stopwords")
import sys
import os
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from utilities.data_retrieval import search_strings


def most_frequent():
    """

    """
    # will probably have to read in as data base
    df = pd.read_json('data/clean_articles.json')
    
    cand_stopwords = ['kambium', 'elijah', 'kam', 'buckner', 'jesús', 'jesus',
        'chuy', 'garcía', 'garcia', 'ja', 'mal', 'green', 'jamal', 'sophia', 'king',
        'roderick', 'sawyer', 'paul', 'vallas', 'willie', 'wilson', 'lori',
        'lightfoot', 'johnson', 'brandon', 'paul', 'buckner', 'said', 'also', 'would',
        'city', 'former']

    news_stopwords = ['said', 'also', 'would', 'city', 'former']
    
    cand_word_freq = calc_most_frequent(df, "candidate_id", cand_stopwords, "Clean Strings")
    
    news_word_freq = calc_most_frequent(df, "Newspaper_id", news_stopwords, "Clean Text")

    return cand_word_freq, news_word_freq

def calc_most_frequent(df, token, additional_stop_words, text_to_inspect):
    unique_ids = df.loc[:,[token]].drop_duplicates()
    list_ids = unique_ids[token].values.tolist()

    respective_word_dict = {}

    for identifier in list_ids:
        subset = df.loc[df[token] == identifier]

        # Concatenate all pretaining text into one string
        full_text = ""
        for row in subset.index:
            full_text += (df.iloc[row])["Clean Strings"]
            full_text += " "

        words = Counter()
        stop_words = (stopwords.words('english'))
        stop_words.extend(additional_stop_words)
        
        words.update(full_text.split())
        most_common = words.most_common(100)

        freq_list = []
        for word_freq in most_common:
            word, freq = word_freq
            if word  not in  stop_words:
                freq_list.append(word_freq)
        
        respective_word_dict[identifier] = freq_list

    return respective_word_dict


if __name__ == "__main__":
    most_frequent()



    