#!/usr/bin/python3

import sys
from collections import Counter
import os

is_reducer = os.path.basename(__file__) == 'reducer.py'

upvotes_word = subreddit_name = sent_word = contr_word = None
upvotes_count = sent_count = sent_sum = contr_count = word_count = 0
topics_count = Counter()

for line in sys.stdin:
    # Value could be a tuple or just an int depending on the line 
    key, value = line.strip().split("\t")
    value = eval(value)
    
    *key, case = key.split(":")
    key = ":".join(key) # handle the case where key has a :
    
    if case == "topics":
        if subreddit_name is None:
            subreddit_name = key
        elif subreddit_name != key:
            print(f"{subreddit_name}:{case}", topics_count.most_common(5), sep='\t')
            subreddit_name = key
            topics_count = Counter()
        topics_count[value[0]] += value[1]

    elif case == "upvotes":
        if upvotes_word is None:
            upvotes_word = key
        elif upvotes_word != key:
            if word_count > 100:
                print(f"{upvotes_word}:{case}", upvotes_count, sep='\t')
            upvotes_word = key
            upvotes_count = 0
            word_count = 0
        upvotes_count += value[0]
        word_count += 1


    elif case == "sent":
        if sent_word is None:
            sent_word = key
        elif sent_word != key:
            print(f"{sent_word}:{case}", sent_sum/sent_count, sep='\t')
            sent_word = key
            sent_count = 0
            sent_sum = 0
        sent_count += 1
        sent_sum += value[0]

    # else:
    #     if contr_word is None:
    #         contr_word = key
    #     elif contr_word != key:
    #         print(f"{contr_word}:{case}", contr_count, sep='\t')
    #         contr_word = key
    #         contr_count = 0
    #     contr_count += value[1]
        
if case == "topics" and subreddit_name:
    print(f"{subreddit_name}:{case}", topics_count.most_common(5), sep='\t')
if case == "upvotes" and upvotes_word:
    if word_count > 100:
        print(f"{upvotes_word}:{case}", upvotes_count, sep='\t')
if case == "sent" and sent_word:
    print(f"{sent_word}:{case}", sent_sum/sent_count, sep='\t')
# if contr_word:
#     print(f"{contr_word}:{case}", contr_count, sep='\t')
