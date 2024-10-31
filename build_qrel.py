import sys
import json

# The path to the topic file
topic_file=sys.argv[1]

# The path to the qrel file
qrel_file=sys.argv[2]

# The path to the new qrel file
new_qrel_file=sys.argv[3]

# Stores the qrel file as 2d array called qrel
with open(qrel_file,'r',encoding="utf-8") as q:
    # This list comprehension says for every line in the qrel_file (from the readlines function) we need to split string by the "\t" (tab) character
    qrel=[line.split('\t') for line in q.readlines()]
    
# Loading the topic file into a dictionary called topic
with open(topic_file,'r',encoding="utf-8") as t:
    topic=json.loads(t.read())
    

# The first element in qrel and topic
print(qrel[:1])
print(topic[:1])  
    
    
"""
Now that you have the qrel in 2d array format and the topics file as an array of dictionarys you must filter the qrel object
so that only querys present in the topic will remain in the qrel.

You have to do this because many evaluation tools will have hard time dealing with uneven result-qrel pairs and because the test set
has 50 items and the original qrel has 1000 items we need to trim the qrel down to 50 elements which reflect whats in the topic file

after doing this filtering you will then write the qrel array to the file called new_qrel_file in the same format as the qrel_file
"""