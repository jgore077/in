import sys
import json

TRAIN=.80
VAL=.10
TEST=.10

qrel=sys.argv[1]
topic=sys.argv[2]

num_answers_dict={}
number_query_dict={}


QUERY_ID=0
ANSWER_ID=1
with open(qrel,'r',encoding='utf-8') as qrelfile:
    qrels=qrelfile.readlines()
    for line in qrels:
        line=line.split('\t')
        if line[QUERY_ID] not in num_answers_dict:
            num_answers_dict[line[QUERY_ID]]=1
        else:
            num_answers_dict[line[QUERY_ID]]+=1

size=len(num_answers_dict)
# train, val, test
t=round(size*TRAIN)
v=round(size*VAL)
te=round(size*TEST)
sizes=[t,v,te]
dicts=[[None,t,[]],[None,v,[]],[None,te,[]]]

# we need to check that our new dataset will be the same size
assert size==(t+v+te)
for id,num in num_answers_dict.items():
    if num in number_query_dict:
        number_query_dict[num].append(id)
    else:
        number_query_dict[num]=[id]
        
number_query_dict=dict(sorted(number_query_dict.items(), key=lambda x: x[0],reverse=True))


# I meant for this loop to keep the average number of qrel entries per query in the topic file
# but I think that iterating over a sorted dict popping one off at a time is good enough
while size!=0:
    i=0
    for avg_size,split_size,lst in dicts:
        # If we have already fulled saturated a split just continue to the next
        if not split_size:
            continue
        for qrel_size in number_query_dict:
                id=number_query_dict[qrel_size].pop()
                if not number_query_dict[qrel_size]:
                    del number_query_dict[qrel_size]
                dicts[i][2].append(id)
                dicts[i][1]=dicts[i][1]-1
                if not dicts[i][0]:
                    dicts[i][0]=qrel_size
                else:
                    dicts[i][0]+=qrel_size
                size-=1
                break
        i+=1
        
saves=[["train.json",dicts[0][2],[]],["validation.json",dicts[1][2],[]],["test.json",dicts[2][2],[]]]

# Populate the topics part of the saves array
with open(topic,'r',encoding='utf-8') as topicsfile:
    topics=json.loads(topicsfile.read())
    while topics:
        for i,save in enumerate(saves):
            for j,topic_dict in enumerate(topics):
                if topic_dict["Id"] in save[1]:
                    saves[i][2].append(topic_dict)
                    del topics[j]
                    break


# Save content back out into file
for save in saves:
    file=save[0]
    content=save[2]
    with open(file,'w',encoding='utf-8') as savefile:
        savefile.write(json.dumps(content,indent=4))
    
