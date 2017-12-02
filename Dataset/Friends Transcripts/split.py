"""
This code splits the train.utt  and train.resp into train, validation and test set
"""
from __future__ import print_function

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


with open('temp.utt', 'r') as file:
	for i,line in enumerate(file):
		if i < _split['dev']:
			print (line[:-1], file = dev_file_utt)
		elif i < _split['tst']:
			print (line[:-1], file = tst_file_utt)
		else:
			print (line[:-1], file = train_file_utt)

with open('temp.resp', 'r') as file:
	for i,line in enumerate(file):
		if i < _split['dev']:
			print (line[:-1], file = dev_file_resp)
		elif i < _split['tst']:
			print (line[:-1], file = tst_file_resp)
		else:
			print (line[:-1], file = train_file_resp)