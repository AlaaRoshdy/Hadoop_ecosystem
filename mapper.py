#!/usr/bin/python3

import sys
import json
import re
import os

sys.path.insert(0, 'nltk')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import math

nltk.data.path.insert(0, "nltk_data") # Make NTLK look in the current path on folder nltk_data

def read_vocabulary(file_path):
    with open(file_path) as file:
        return file.read().strip().split()
    
stopwords_english = stopwords.words('english')
stemmer = PorterStemmer() # stemmer object 

with open("freqs.json", "r") as f:
    word_freqs = json.load(f) # Word-senetimemt Frequency dictionary key: <word>:<1/0>, <count>, pre calculated

theta = [7.252278398693534e-08, 0.000523899772669574, -0.0005551707363468511] # pre-trained sentiment analysis weights (LR)

def sigmoid(z):
    return 1 / (1 + math.exp(z))

for line in sys.stdin:
    # Converting line JSON to python dictionary
    line_dict = json.loads(line)
    # preprrocess test
    body = re.sub(r'[^A-Za-z0-9 ]+', '', line_dict["body"]) # Remove non alphanumeric and non space characters
    body = re.sub(r'https?:\/\/.*[\r\n]*', '', body) # Remove links
    words = word_tokenize(body)
    subreddit_name = line_dict["subreddit"]

    features = [1, 0, 0] # Simple features for sentiment analysis

    # Per word Operation
    for word in words:
        if word not in stopwords_english: # skip stopwords
            word_stem = stemmer.stem(word)
            # Word ( as topic ) count per Subreddit
            print(f"{subreddit_name}:topics", (word_stem, 1), sep='\t')

            # Word ( as topic ) with UpVotes
            print(f"{word_stem}:upvotes", line_dict["ups"], sep='\t')

            # Word occurence in +ve examples default as 0
            features[1] += word_freqs.get(f"{word_stem}:1", 0)

            # Word occurence in -ve examples default as 0
            features[2] += word_freqs.get(f"{word_stem}:0", 0)

    # Comment sentiment / subreddit
    sentiment = sigmoid(sum([f * th for f, th in zip(features, theta)]))
    print(f"{subreddit_name}:sent", sentiment, sep="\t")

    # Controversiality
    print(f"{line_dict['parent_id']}:contr", ("count", 1), sep='\t')
    print(f"{line_dict['id']}:contr", ("controversiality", line_dict["controversiality"]), sep='\t')
