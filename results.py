from BiWrapper import BiEncoderWrapper,remove_html_tags
from CrossWrapper import CrossEncoderWrapper
from ranx import Run
from tqdm import tqdm
import argparse
import json
import os

RESULTS_DIRECTORY="results/"

parser=argparse.ArgumentParser()

parser.add_argument("-a","--answers",default="./Answers.json")
parser.add_argument("-b","--bi")
parser.add_argument("-c","--cross")
parser.add_argument("-t","--topics")
parser.add_argument("-q","--qrel")
parser.add_argument("-o","--out")
parser.add_argument("--type",action='store_true')
parser.add_argument("--fine",action='store_true')
 

if not os.path.exists(RESULTS_DIRECTORY):
    os.mkdir(RESULTS_DIRECTORY)
    
args=parser.parse_args()

topic_file=args.topics
out_file=RESULTS_DIRECTORY+args.out
model_type=args.type
fine_tuned_query=args.fine

biencoder=BiEncoderWrapper(answers_file=args.answers,model_name=args.bi)
crossencoder=CrossEncoderWrapper(answers_path=args.answers,model_name=args.cross)

with open(topic_file,'r',encoding='utf-8') as topicfile:
    topics=json.loads(topicfile.read())
    
bi_dict={}
cross_dict={}

print(f"Generating results for {args.bi} and {args.cross} then saving output to {out_file}")
for topic in tqdm(topics,desc="Doing retrieval"):
    # I'm using the same format used in the training samples
    query=None
    if fine_tuned_query:
        query="[TITLE]"+topic["Title"]+"[BODY]"+remove_html_tags(topic["Body"])
    else:
        query=topic["Title"]+" "+remove_html_tags(topic["Body"])
    id=topic["Id"]
    
    results=biencoder.search(query)
    bi_dict[id]=results
    
    # If we are only generating results for a bi-encoder we can save time by skipping the cross-encoder
    if not model_type:
        reranked=crossencoder.rerank(results,query)
        cross_dict[id]=reranked
    

trec_out_file=out_file+".trec"
# Write bi-encoder output (bi_dict) to a file
if model_type:
    Run(bi_dict,name=args.bi).save(trec_out_file)
    
# Write the cross-encoder output (cross_dict) to a file
else:
    Run(cross_dict,name=args.cross).save(trec_out_file)

# Rename the .trec file because it was easier to use ranx to save the file
os.rename(trec_out_file,out_file)