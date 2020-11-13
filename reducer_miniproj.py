#!/usr/bin/python3

import sys

upvotes_word, topics_word, sent_word, contr_word = None
upvotes_count, topics_count, sent_count, contr_count = 0

for line in sys.stdin:
    # Value could be a tuple or just an int depending on the line 
    key, value = line.strip().split()
    
    key, case = key.split(":")
    
    if "topics" == case:
        if topics_word is None:
            topics_word = key
        elif topics_word != key:
            print(topics_word, most_discussed_topic, sep='\t')
            topics_word = key
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
        

print(topics_word, most_discussed_topic, sep='\t')
print(upvotes_word, upvotes_count, sep='\t')
print(sent_word, sent_count, sep='\t')
print(contr_word, contr_count, sep='\t')
