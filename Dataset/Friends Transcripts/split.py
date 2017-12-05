"""
This code splits the train.utt  and train.resp into train, validation and test set
"""
from __future__ import print_function
import sys

char = sys.argv[1] #s, joey, monica, chandler, rachel, ross, phoebe

_split = {
	'dev': 500,
	'tst': 1000
}

dev_file_utt = open('dev.utt','w')
dev_file_resp = open('dev.resp','w')

tst_file_utt = open('test.utt','w')
tst_file_resp = open('test.resp','w')

train_file_utt = open('train.utt','w')
train_file_resp = open('train.resp','w')

no_keep = {}

with open('temp.resp', 'r') as file:
	for i,line in enumerate(file):
		line_char = line.split('>')[0][1:].strip()
		if line_char == 's':
			no_keep[i] = 1
			continue
		if char != 's':
			if line_char != char:
				no_keep[i] = 1
				continue
		if i < _split['dev']:
			print (line[:-1], file = dev_file_resp)
		elif i < _split['tst']:
			print (line[:-1], file = tst_file_resp)
		else:
			print (line[:-1], file = train_file_resp)

with open('temp.utt', 'r') as file:
	for i,line in enumerate(file):
		if i in no_keep: continue
		if i < _split['dev']:
			print (line[:-1], file = dev_file_utt)
		elif i < _split['tst']:
			print (line[:-1], file = tst_file_utt)
		else:
			print (line[:-1], file = train_file_utt)
