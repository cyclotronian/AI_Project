#!/bin/sh

mkdir -p cornell_dialog

cp test.utt cornell_dialog/test.utt
cp test.resp cornell_dialog/test.resp
cp train.utt cornell_dialog/train.utt
cp train.resp cornell_dialog/train.resp
cp dev.utt cornell_dialog/dev.utt
cp dev.resp cornell_dialog/dev.resp
cp vocab cornell_dialog/vocab.utt
cp vocab cornell_dialog/vocab.resp

# python -m nmt.nmt \
#     --src=utt --tgt=resp \
#     --vocab_prefix=cornell_dialog/vocab  \
#     --train_prefix=cornell_dialog/train \
#     --dev_prefix=cornell_dialog/dev  \
#     --test_prefix=cornell_dialog/test \
#     --out_dir=cornell_dialog_model_noatt \
#     --num_train_steps=12000 \
#     --steps_per_stats=100 \
#     --num_layers=2 \
#     --num_units=128 \
#     --dropout=0.2 \
#     --metrics=bleu

# python -m nmt.nmt \
#     --src=vi --tgt=en \
#     --vocab_prefix=nmt_data/vocab  \
#     --train_prefix=nmt_data/train \
#     --dev_prefix=nmt_data/tst2012  \
#     --test_prefix=nmt_data/tst2013 \
#     --out_dir=nmt_model \
#     --num_train_steps=12000 \
#     --steps_per_stats=100 \
#     --num_layers=2 \
#     --num_units=128 \
#     --dropout=0.2 \
#     --metrics=bleu