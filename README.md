# Installation
To install this repo you need to run this command to collect its python deps
```
pip install -r requirements.txt
```

# Python Scripts 

## `results.py`
This is the script that generates results files, I got this help message by running `python results.py -h`
```
usage: results.py [-h] [-a ANSWERS] [-b BI] [-c CROSS] [-t TOPICS] [-q QREL] [-o OUT] [--type] [--fine]

options:
  -h, --help            show this help message and exit
  -a ANSWERS, --answers ANSWERS
                        path to the answers file
  -b BI, --bi BI        The name of the bi-encoder model
  -c CROSS, --cross CROSS
                        The name of the cross-encoder model
  -t TOPICS, --topics TOPICS
                        The path to the topics file
  -q QREL, --qrel QREL  The path to qrel file
  -o OUT, --out OUT     Determines where the results of the model will be stored
  --type                Add this argument to save the results of the bi-encoder, saves cross-encoder by default
  --fine                Tells the script that the model its running is fine-tuned and can use special tokens
```
### Sample Usage
This line was pulled directly from `results.sh`
```bash
python results.py -a Answers.json -b all-MiniLM-L6-v2 -c BAAI/bge-reranker-base -t topics_1.json -o result_bi_1.tsv --type
```
## `evaluate.py`
This script is used to evaluate a results file along with its corresponding qrel file. It calculates p@1, p@5, nDCG@5, mrr@5, and map.
```
usage: evaluation.py [-h] [-r RESULTS] [-q QREL]

options:
  -h, --help            show this help message and exit
  -r RESULTS, --results RESULTS
                        The path of the results file
  -q QREL, --qrel QREL  The path of the qrel file
```

## `build_qrel.py`
This file will take three arguments: a topics file, a qrel file, and a output path for a new qrel file. This script was needed because our split sets (`train.json`, `validation.json`, `test.json`) are all subsets of the original `topics_1.json`. Therefore this script produces a subset of the input qrel so the `ranx` can work with it.
```
python build_qrel.py <topics_path>.json <qrel_path>.tsv <new_qrel_path>.tsv
```
This is how we used it to produce `qrel_1_test.tsv` a subset of `qrel_1.tsv` for `test.json`
```
python build_qrel.py test.json qrel_1.tsv qrel_1_test.tsv 
```
## `sbert_crossencoder.py`
This scripts produces a fine-tuned bi-encoder and a fine-tuned cross-encoder.

## `build_test_train_split.py`
This script aims to produce a well distributed dataset split by keeping the average number of answers per query the same across all three sets (train,val,test). The split is 90 5 5 by default but that can be changed by adjusting the `TRAIN`, `VAL`, & `TEST` constants at the top of the file.
### Usage
```
python build_test_train_split.py <topics_path>.json <qrel_path>.tsv 
```

# Bash Scripts

## `results.sh`
This script will generate all 8 results files for each model.
```
./results.sh
```
## `evaluations.sh`
This script will produce the metrics for each result file. You can take lines out of this file to do specific evaluations if you don't want to run the entire script.
```
./evaluations.sh
```
