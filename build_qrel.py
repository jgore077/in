import csv
import sys
import json
import pandas as pd

# The path to the topic file
topic_file = sys.argv[1]

# The path to the qrel file
qrel_file = sys.argv[2]

# The path to the new qrel file - relevant queries between the two files
new_qrel_file = sys.argv[3]

tsv_file = 'qrel_1_test.tsv'

# Stores the qrel file as 2d array called qrel
with open(qrel_file,'r',encoding="utf-8") as q:
    # This list comprehension says for every line in the qrel_file (from the readlines function) we need to split string by the "\t" (tab) character
    qrel = [line.split('\t') for line in q.readlines()]
    
# Loading the topic file into a dictionary called topic
with open(topic_file,'r',encoding="utf-8") as t:
    topic = json.loads(t.read())
    

# The first element in qrel and topic
print(qrel[:1])
print(topic[:1])


# Filter qrel file, keep only queries present in topic file
def filter_qrel(topic_file, qrel_file, new_qrel_file):

    with open(topic_file, 'r') as f:
        topics = json.load(f)
        topic_ids = set(topic['query_id'] for topic in topics)

    # Write qrel array to the file new_qrel_file in the same format as the qrel_file
    with open(qrel_file, 'r') as f, open(new_qrel_file, 'w') as out_f:
        for line in f:
            query_id, _, _, _ = line.strip().split('\t')
            if query_id in topic_ids:
                out_f.write(line)




def qrel_to_tsv(new_qrel_file, tsv_file):
    """Converts a QREL file to a TSV file."""

    with open(new_qrel_file, 'r') as f, open(tsv_file, 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        for line in f:
            writer.writerow(line.strip().split('\t'))

    # with open(new_qrel_file, 'r') as f:
    #     lines = f.readlines()
    #
    # data = []
    # for line in lines:
    #     parts = line.strip().split()
    #     data.append({
    #         'query_id': parts[0],
    #         'iteration': parts[1],
    #         'doc_id': parts[2],
    #         'relevance': parts[3]
    #     })
    #
    # df = pd.DataFrame(data)
    # df.to_csv(tsv_file, sep='\t', index=False)


filter_qrel(qrel_file, topic_file, new_qrel_file)
new_qrel_file = 'qrel.txt'
tsv_file = 'qrel.tsv'
qrel_to_tsv(new_qrel_file, tsv_file)
print(f"Saving TSV file to: {tsv_file}")

"""
Now that you have the qrel in 2d array format and the topics file as an array of dictionarys you must filter the qrel object
so that only querys present in the topic2 will remain in the qrel.

You have to do this because many evaluation tools will have hard time dealing with uneven result-qrel pairs and because the test set
has 50 items and the original qrel has 1000 items we need to trim the qrel down to 50 elements which reflect whats in the topic file

after doing this filtering you will then write the qrel array to the file called new_qrel_file in the same format as the qrel_file
"""

