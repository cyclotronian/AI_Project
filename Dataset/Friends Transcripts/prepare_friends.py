"""
This code separates the cornell movie dialogue dataset into training and label files
"""
from __future__ import print_function
import operator
from itertools import islice

counter = 0
train_train_utt = open('temp_temp.utt','w')
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
	# '[': ' &#91 ',
	# '[': ' &#93 ',
	# '<u>': '',
	# '</u>': '',
	'/': ' / '
}

num_line = 0
with open('friends_processed.txt','r') as file:
	for line in file:
		num_line += 1

def add_to_vocab(sentence):
	for word in sentence.split(' '):
		if word == '': continue
		if word not in vocab:
			vocab[word] = 0
		else:
			vocab[word] += 1

def format_line_utterance(sentence):
	# return sentence
	sentence = ' '.join(sentence.lower().split(' ')[1:])
	sentence = unicode(sentence, errors='ignore')
	for key in punctuation:
		sentence = sentence.replace(key,punctuation[key])
	return sentence

def format_line_response(sentence):
	# return sentence
	sentence = unicode(sentence.lower(), errors='ignore')
	for key in punctuation:
		sentence = sentence.replace(key,punctuation[key])
	return sentence

line_ctr = 0
train_file_line_ctr = 0
state = 'new_scene'
remove_lines = []
with open('friends_processed.txt','r') as file:
	for line in file:
		if line[:-1]=='< ':
			state = 'new_scene'
			line_ctr+=1
			continue

		sentence_utt = format_line_utterance(line[:-1])
		sentence_resp = format_line_response(line[:-1])

		if line_ctr==1 or state=='new_scene':
			print (sentence_utt, file = train_train_utt)
			state = 'scene'
			remove_lines.append(train_file_line_ctr)
			train_file_line_ctr+=1
			line_ctr+=1
		elif line_ctr==num_line-1:
			print (sentence_resp, file = train_resp)
		else:
			print (sentence_resp, file = train_resp)
			print (sentence_utt, file = train_train_utt)
			train_file_line_ctr+=1
			line_ctr+=1

		add_to_vocab(sentence_utt)

train_train_utt.close()

remove_lines = remove_lines[1:]
# print (remove_lines)
line_ctr = 0
train_utt = open('temp.utt','w')
with open('temp_temp.utt','r') as file:
	for line in file:
		line_ctr+=1
		if line_ctr not in remove_lines:
			print (line[:-1], file = train_utt)




# with open('friends_processed.txt','r') as file:
# 	for i,line in enumerate(file):
# 		if i == num_line-1: continue

# 		a = line[:-1].split('+++$+++')
# 		sentence = a[-1][1:].lower()

# 		sentence = unicode(sentence, errors='ignore')

# 		for key in punctuation:
# 			sentence = sentence.replace(key,punctuation[key])
		
# 		if sentence=='': continue

# 		print (sentence, file=train_utt)
# 		# print (sentence, file=train_resp)

# 		# sentence = [s for s in sentence if s.lower() not in hello_dic]
# 		# for punct in punctuation:
# 		# 	sentence = sentence.replace(punct,'')

# 		for word in sentence.split(' '):
# 			if word == '': continue
# 			if word not in vocab:
# 				vocab[word] = 0
# 			else:
# 				vocab[word] += 1

# with open('friends_processed.txt','r') as file:
# 	for i,line in enumerate(file):
# 		if i == 0: continue

# 		a = line[:-1].split('+++$+++')
# 		sentence = a[-1][1:].lower()

# 		sentence = unicode(sentence, errors='ignore')

# 		for key in punctuation:
# 			sentence = sentence.replace(key,punctuation[key])
		
# 		if sentence=='': continue

# 		print (sentence, file=train_resp)
# 		# print (sentence, file=train_utt)
	
# 		# sentence = [s for s in sentence if s.lower() not in hello_dic]
# 		# for punct in punctuation:
# 		# 	sentence = sentence.replace(punct,'')

# 		for word in sentence.split(' '):
# 			if word == '': continue
# 			if word not in vocab:
# 				vocab[word] = 0
# 			else:
# 				vocab[word] += 1


vocab_file = open('vocab','w')

sorted_x = sorted(vocab.items(), key = operator.itemgetter(1), reverse = True)

for i in sorted_x:
	if i[1] >= 0:
		print (str(i[0]), file = vocab_file)