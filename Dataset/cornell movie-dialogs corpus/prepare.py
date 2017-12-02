"""
This code separates the cornell movie dialogue dataset into training and label files
"""
from __future__ import print_function
import operator
from itertools import islice

counter = 0
train_utt = open('temp.utt','w')
train_resp = open('temp.resp','w')

vocab = {}

punctuation = {
	"'": " &apos;",
	'"': " &quot; ",
	'\t': ' ',
	'?': ' ? ',
	',': ' , ',
	'.': ' . ',
	'!': ' ! ',
	'-': ' - ',
	':': ' : ',
	# ';': ' ; ',
	'[': ' &#91 ',
	'[': ' &#93 ',
	'<u>': '',
	'</u>': '',
	'/': ' / '
}

num_line = 0
with open('movie_lines.txt','r') as file:
	for line in file:
		num_line += 1

with open('movie_lines.txt','r') as file:
	for i,line in enumerate(file):
		if i == num_line-1: continue

		a = line[:-1].split('+++$+++')
		sentence = a[-1][1:].lower()

		sentence = unicode(sentence, errors='ignore')

		for key in punctuation:
			sentence = sentence.replace(key,punctuation[key])
		
		if sentence=='': continue

		print (sentence, file=train_utt)
		# print (sentence, file=train_resp)

		# sentence = [s for s in sentence if s.lower() not in hello_dic]
		# for punct in punctuation:
		# 	sentence = sentence.replace(punct,'')

		for word in sentence.split(' '):
			if word == '': continue
			if word not in vocab:
				vocab[word] = 0
			else:
				vocab[word] += 1

with open('movie_lines.txt','r') as file:
	for i,line in enumerate(file):
		if i == 0: continue

		a = line[:-1].split('+++$+++')
		sentence = a[-1][1:].lower()

		sentence = unicode(sentence, errors='ignore')

		for key in punctuation:
			sentence = sentence.replace(key,punctuation[key])
		
		if sentence=='': continue

		print ("<s> "+sentence, file=train_resp)
		# print (sentence, file=train_utt)
	
		# sentence = [s for s in sentence if s.lower() not in hello_dic]
		# for punct in punctuation:
		# 	sentence = sentence.replace(punct,'')

		for word in sentence.split(' '):
			if word == '': continue
			if word not in vocab:
				vocab[word] = 0
			else:
				vocab[word] += 1


vocab_file = open('vocab','w')

sorted_x = sorted(vocab.items(), key = operator.itemgetter(1), reverse = True)

for i in sorted_x:
	if i[1] >= 0:
		print (str(i[0]), file = vocab_file)