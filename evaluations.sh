#!/bin/bash
python3 evaluation.py -q qrel_1_test.tsv -r results/result_bi_ft_1.tsv
python3 evaluation.py -q qrel_1_test.tsv -r results/result_ce_ft_1.tsv
python3 evaluation.py -q qrel_1.tsv -r results/result_bi_1.tsv
python3 evaluation.py -q qrel_1.tsv -r results/result_ce_1.tsv
python3 evaluation.py -q qrel_2.tsv -r results/result_bi_2.tsv
python3 evaluation.py -q qrel_2.tsv -r results/result_bi_ft_2.tsv
python3 evaluation.py -q qrel_2.tsv -r results/result_ce_2.tsv
python3 evaluation.py -q qrel_2.tsv -r results/result_ce_ft_2.tsv