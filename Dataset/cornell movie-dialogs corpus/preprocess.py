"""
This code separates the cornell movie dialogue dataset into training and label files
"""
from __future__ import print_function
import operator
from itertools import islice

counter = 0
movie_new = open('movie_lines_1.txt', 'w')

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
  '<i>': '',
  '</i>': '',
	'/': ' / '
}

with open('movie_lines.txt','r') as file:
	for i,line in enumerate(file):

		a = line[:-1].split('+++$+++')
		sentence = a[-1].lower()

		for key in punctuation:
			sentence = sentence.replace(key,punctuation[key])
		a[-1] = sentence
		print ('+++$+++'.join(a), file = movie_new)
