from ranx import Run,Qrels,evaluate
import argparse
import json
import json_fix # import this anytime before the JSON.dumps gets called

# create a converter
import numpy
json.fallback_table[numpy.ndarray] = lambda array: array.tolist()


METRICS=['precision@1','precision@5','ndcg@5','mrr','map']

parser=argparse.ArgumentParser()
parser.add_argument("-r","--results",help="The path of the results file")
parser.add_argument("-q","--qrel",help="The path of the qrel file")
parser.add_argument("--no-mean",action="store_false",help="Returns per query scores")

args=parser.parse_args()

results_file=args.results
qrel_file=args.qrel
mean=args.no_mean

print(f"Evaluating {results_file}")
results=evaluate(Qrels.from_file(qrel_file,kind="trec"),Run.from_file(results_file,kind="trec"),METRICS,return_mean=mean)
if mean:
    print(results)
else:
    with open(f"{results_file.split('.')[0].split('/')[1]}_eval.json",'w') as eval_file:
        eval_file.write(json.dumps(results,indent=4))