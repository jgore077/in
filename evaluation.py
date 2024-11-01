from ranx import Run,Qrels,evaluate
import argparse

METRICS=['precision@1','precision@5','ndcg@5','mrr','map']

parser=argparse.ArgumentParser()
parser.add_argument("-r","--results",help="The path of the results file")
parser.add_argument("-q","--qrel",help="The path of the qrel file")

args=parser.parse_args()

results_file=args.results
qrel_file=args.qrel

print(f"Evaluating {results_file}")
print(evaluate(Qrels.from_file(qrel_file,kind="trec"),Run.from_file(results_file,kind="trec"),METRICS))