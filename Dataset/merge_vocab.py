from __future__ import print_function
vocab = {}
files = ['./cornell movie-dialogs corpus/cornell_dialog/vocab.utt', './Friends Transcripts/friends_dialog/vocab.utt']
out_files = ['./cornell movie-dialogs corpus/cornell_dialog/vocab.utt', './cornell movie-dialogs corpus/cornell_dialog/vocab.resp']
for filename in files:
    with open(filename, 'r') as file:
        for line in file:
            vocab[line[:-1]] = 1

for filename in out_files:
    out_file_d = open(filename, 'w')
    for key in vocab:
        print(key,file=out_file_d)
