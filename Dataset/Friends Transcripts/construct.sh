#!/bin/sh

suffix="$1"
folder=friends_dialog_$suffix
mkdir -p $folder

cp test.utt $folder/test.utt
cp test.resp $folder/test.resp
cp train.utt $folder/train.utt
cp train.resp $folder/train.resp
cp dev.utt $folder/dev.utt
cp dev.resp $folder/dev.resp
cp vocab $folder/vocab.utt
cp vocab $folder/vocab.resp