from BiWrapper import BiEncoderWrapper,remove_html_tags
from CrossWrapper import CrossEncoderWrapper
from ranx import Run
import argparse
import json

parser=argparse.ArgumentParser()

parser.add_argument("-a","--answers",default="./Answers.json")
parser.add_argument("-b","--bi")
parser.add_argument("-c","--cross")
parser.add_argument("-t","--topics")
parser.add_argument("-q","--qrel")
parser.add_argument("-o","--out")
parser.add_argument("--type",action='store_true')
parser.add_argument("--fine",action='store_true')
 

args=parser.parse_args()

topic_file=args.topics
out_file=args.out
model_type=args.type
fine_tuned_query=args.fine

biencoder=BiEncoderWrapper(answers_file=args.answers,model_name=args.bi)
crossencoder=CrossEncoderWrapper(answers_path=args.answers,model_name=args.cross)

with open(topic_file,'r',encoding='utf-8') as topicfile:
    topics=json.loads(topicfile.read())
    
bi_dict={}
cross_dict={}

for topic in topics:
    # I'm using the same format used in the training samples
    query=None
    if fine_tuned_query:
        query="[TITLE]"+topic["Title"]+"[BODY]"+remove_html_tags(topic["Body"])
    else:
        query=topic["Title"]+" "+remove_html_tags(topic["Body"])
    id=topic["Id"]
    results=biencoder.search(query)
    reranked=crossencoder.rerank(results,query)
    
    # Assign dicts
    bi_dict[id]=results
    cross_dict[id]=reranked
    

# Write bi-encoder output (bi_dict) to a file
if model_type:
    Run(bi_dict).save(out_file)
    
# Write the cross-encoder output (cross_dict) to a file
else:
    Run(cross_dict).save(out_file)