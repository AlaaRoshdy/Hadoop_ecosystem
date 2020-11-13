#!/usr/bin/python3

import sys
from collections import Counter
import os

is_reducer = os.path.basename(__file__) == 'reducer.py'

upvotes_word = subreddit_name = sent_word = contr_word = None
upvotes_count = sent_count = contr_count = 0
topics_count = Counter()

for line in sys.stdin:
    # Value could be a tuple or just an int depending on the line 
    key, value = line.strip().split("\t")
    value = eval(value)
    
    key, case = key.split(":")
    
    if case == "topics":
        if subreddit_name is None:
            subreddit_name = key
        elif subreddit_name != key:
            print(subreddit_name, topics_count.most_common(5), sep='\t')
            subreddit_name = key
            topics_count = 0
        topics_count[value[0]] += int(value[1]) 

    elif case == "upvotes":
        if upvotes_word is None:
            upvotes_word = key
        elif upvotes_word != key:
            print(upvotes_word, upvotes_count, sep='\t')
            upvotes_word = key
            upvotes_count = 0
        upvotes_count += int(value[0])
        

    elif case == "sent":
        if sent_word is None:
            sent_word = key
        elif sent_word != key:
            print(sent_word, sent_count, sep='\t')
            sent_word = key
            sent_count = 0 
        sent_count += float(value[0])

    else:
        if word is None:
            word = key
        elif word != key:
            print(word, contr_count, sep='\t')
            word = key
            contr_count = 0
        contr_count += int(value)
        
if subreddit_name:
    print(subreddit_name, topics_count.most_common(5), sep='\t')
if upvotes_word:
    print(upvotes_word, upvotes_count, sep='\t')
if sent_word:
    print(sent_word, sent_count, sep='\t')
if word:
    print(contr_word, contr_count, sep='\t')
