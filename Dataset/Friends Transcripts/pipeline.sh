#!/bin/sh

python format.py 1
python format.py 2 > output
cp output friends_processed.txt
python prepare_friends.py 
python split.py 
bash construct.sh 

# python -m nmt.nmt \
#     --attention=scaled_luong \
#     --src=utt --tgt=resp \
#     --vocab_prefix=friends_dialog/vocab  \
#     --train_prefix=friends_dialog/train \
#     --dev_prefix=friends_dialog/dev  \
#     --test_prefix=friends_dialog/test \
#     --out_dir=friends_attn \
#     --num_train_steps=6000 \
#     --steps_per_stats=100 \
#     --num_layers=2 \
#     --num_units=128 \
#     --dropout=0.2 \
#     --metrics=bleu
