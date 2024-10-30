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
 

args=parser.parse_args()

topic_file=args.topics
out_file=args.out
save_model=args.type

biencoder=BiEncoderWrapper(answers_file=args.answers,model_name=args.bi)
crossencoder=CrossEncoderWrapper(answers_path=args.answers,model_name=args.cross)

with open(topic_file,'r',encoding='utf-8') as topicfile:
    topics=json.loads(topicfile.read())
    
bi_dict={}
cross_dict={}

for topic in topics:
    # I'm using the same format used in the training samples
    query=topic["Title"]+" "+remove_html_tags(topic["Body"])
    id=topic["Id"]
    results=biencoder.search(query)
    reranked=crossencoder.rerank(results,query)
    
    # Assign dicts
    bi_dict[id]=results
    cross_dict[id]=reranked
    

