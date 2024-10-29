from BiWrapper import BiEncoderWrapper
from CrossWrapper import CrossEncoderWrapper
import argparse
import ranx

parser=argparse.ArgumentParser()

parser.add_argument("-a","--answers",default="./Answers.json")
parser.add_argument("-b","--bi")
parser.add_argument("-c","--cross")
parser.add_argument("-t","--topics")
parser.add_argument("-q","--qrel")
parser.add_argument("--out-bi")
parser.add_argument("--out-cross")


args=parser.parse_args()

topic=args.topics
qrel=args.qrel
biencoder_output=args.out_bi
crossencoder_outpout=args.out_cross

biencoder=BiEncoderWrapper(answers_file=args.answers,model_name=args.bi)
crossencoder=CrossEncoderWrapper(answers_path=args.answers,model_name=args.cross)

Q="cheap flights to usa from britain"
results=biencoder.search(Q)
reranked=crossencoder.rerank(results,Q)
