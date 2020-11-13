#!/usr/bin/python3

import sys
from Collections import Counter

upvotes_word, subreddit_name, sent_word, contr_word = None
upvotes_count, topics_count, sent_count, contr_count = 0

for line in sys.stdin:
    # Value could be a tuple or just an int depending on the line 
    key, value = line.strip().split("\t")
    value = eval(value)
    
    key, case = key.split(":")
    
    if "topics" == case:
        if subreddit_name is None:
            subreddit_name = key
        elif subreddit_name != key:
            print(subreddit_name, most_discussed_topic, sep='\t')
            subreddit_name = key
            topics_count = 0
        topics_count += int(value[1]) 
        most_discussed_topic = (value[0], topics_count)

    else if "upvotes" == case:
        if upvotes_word is None:
            upvotes_word = key
        elif upvotes_word != key:
            print(upvotes_word, upvotes_count, sep='\t')
            upvotes_word = key
            upvotes_count = 0
        upvotes_count += int(value)
        

    else if "sent" == case:
        if sent_word is None:
            sent_word = key
        elif sent_word != key:
            print(sent_word, sent_count, sep='\t')
            sent_word = key
            sent_count = 0 
        sent_count += int(value)

    else:
        if word is None:
            word = key
        elif word != key:
            print(word, contr_count, sep='\t')
            word = key
            contr_count = 0
        contr_count += int(value)
        

print(subreddit_name, most_discussed_topic, sep='\t')
print(upvotes_word, upvotes_count, sep='\t')
print(sent_word, sent_count, sep='\t')
print(contr_word, contr_count, sep='\t')
