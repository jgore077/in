import matplotlib.pyplot as plt
import sys
import json
import ranx
import os

K=50
PLOTS_PATH="plots/"
EVAL_FILE=sys.argv[1]
QREL_FILE=sys.argv[2]
TOPICS_FILE=sys.argv[3]
MODEL_NAME=sys.argv[4]

if not os.path.exists(PLOTS_PATH):
    os.mkdir(PLOTS_PATH)
METRIC="precision@5"
with open(TOPICS_FILE,'r',encoding='utf-8') as topicsfile:
    topics=json.loads(topicsfile.read())

qrel =ranx.Qrels.from_file(QREL_FILE,kind="trec").to_dict()


with open(EVAL_FILE,'r',encoding="utf-8") as eval_file:
    evaldict=json.load(eval_file)

precisions={}
for metric in evaldict:
    for query,id in zip(evaldict[metric],qrel.keys()):
        precisions[id]=query
        

val_ids=sorted(precisions.items(),key=lambda x: x[1],reverse=True)

val_ids=val_ids[:K]

print(val_ids)

plt.bar([tupl[0] for tupl in val_ids],[tupl[1] for tupl in val_ids],)
plt.title(f'precision@5 ({K} highest scores) for {MODEL_NAME}')
plt.xticks(rotation=90, ha='right')
plt.tick_params(axis='x', which='minor', labelsize=8,)
plt.xlabel('Query Id')
plt.ylabel('precision@5')
plt.savefig(f"{PLOTS_PATH}{MODEL_NAME}_ski_plot.png")