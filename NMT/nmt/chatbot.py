from __future__ import print_function
import subprocess
import sys

command =  ['python', '-m', 'nmt.nmt', '--out_dir=cornell_attn', '--inference_input_file=friends_dialog/infer.utt', '--inference_output_file=friends_dialog/infer.resp']

def _get_user_input():
	print('You: ', end='')
	sys.stdout.flush()
	return  sys.stdin.readline()

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

def process(string):
	for key in punctuation:
		string = string.replace(key,punctuation[key])
	return string

inp = _get_user_input()

while inp!='\n':
	inp = process(inp)

	infer = open('friends_dialog/infer.utt','w')
	print(inp, file=infer, end='')
	infer.close()

	proc = subprocess.Popen(command, stdout=subprocess.PIPE)
	(out, err) = proc.communicate()

	with open('friends_dialog/infer.resp','r') as file:
		for line in file:
			print ('Bot: ',line, end='')

	inp = _get_user_input()