#!/bin/bash
python3 results.py -a Answers.json -b all-MiniLM-L6-v2             -c BAAI/bge-reranker-base       -t topics_1.json -o result_bi_1.tsv --type
python3 results.py -a Answers.json -b fine-tuned-all-MiniLM-L6-v2  -c fine-tuned-bge-reranker-base -t test.json -o result_bi_ft_1.tsv --type --fine
python3 results.py -a Answers.json -b all-MiniLM-L6-v2             -c BAAI/bge-reranker-base       -t topics_1.json -o result_ce_1.tsv
python3 results.py -a Answers.json -b fine-tuned-all-MiniLM-L6-v2  -c fine-tuned-bge-reranker-base -t test.json -o result_ce_ft_1.results.py --fine

python3 results.py -a Answers.json -b all-MiniLM-L6-v2             -c BAAI/bge-reranker-base       -t topics_2.json -o result_bi_2.tsv --type
python3 results.py -a Answers.json -b fine-tuned-all-MiniLM-L6-v2  -c fine-tuned-bge-reranker-base -t topics_2.json -o result_bi_ft_2.tsv --type --fine
python3 results.py -a Answers.json -b all-MiniLM-L6-v2             -c BAAI/bge-reranker-base       -t topics_2.json -o result_ce_2.tsv
python3 results.py -a Answers.json -b fine-tuned-all-MiniLM-L6-v2  -c fine-tuned-bge-reranker-base -t topics_2.json -o result_ce_ft_2.tsv --fine