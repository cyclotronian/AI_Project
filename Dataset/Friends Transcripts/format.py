from __future__ import print_function
import sys

class Dialog:

	valid = ['joey','monica','chandler','phoebe','ross','rachel','[scene']

	def __init__(self):
		self.speaker = ''
		self.dialog = ''

	def __init__(self, _speaker):
		if _speaker in self.valid:
			self.speaker = _speaker
		else:
			self.speaker = 's'
		self.dialog = ''

	def append_dialog(self,_str):
		self.dialog+=_str

	def substitute_dialog(self,_str):
		self.dialog = _str

	def add_speaker(self,_speaker):
		self.speaker = _speaker

	def __str__(self):
		p = ''
		p+= '<'+self.speaker+'>'
		p+= self.dialog+'\n'
		return p

class Script:

	def __init__(self):
		self.dialog_status = 'no_one_speaking'
		self.paran_status = 'closed'
		self.episode_end = False
		self.speaker = ''
		self.script = ['']

	def readfile(self,filename,out_file):
		out_f = open(out_file,'w')
		with open(filename,'r') as file:
			for line in file:
				#lowercase 
				line=line.lower()
				
				#mark end of episode
				if line[:-1] == 'end' or line[:-1] == 'the end':
					self.episode_end = True
				
				a = line[:-1].split(':')
				
				#ignore lines starting with "note"
				if a[0]=='(note': continue
				
				if len(a) > 1: 

					#if a character is speaking, start a new dialog
					if len(a[0].split(' '))==1:
						
						# if self.dialog_status=='no_one_speaking':
						print (self.script[0], end='',file=out_f)
						a[0] = a[0].replace(' ','_')
						self.script[0] = Dialog(a[0])
						self.script[-1].append_dialog(a[1]+' ')
						self.dialog_status='some_one_speaking'

					# else:
					# 	print 'WAAAAAAAA'
					
				elif self.dialog_status=='some_one_speaking':
					if self.episode_end == True:
						self.episode_end = False
						self.dialog_status=='no_one_speaking'
						continue
					self.script[-1].append_dialog(line[:-1]+' ')

	def remove_paran(self,filename):
		with open(filename,'r') as file:
			for line in file:
				# print (line)
				start = line[:-1].find( '(' )
				end = line[:-1].find( ')' )
				result = line[:-1]
				while (start != -1 and end != -1):
					result = result[:start]+result[end+1:]
					# _dialog.substitute_dialog(result)
					start = result.find( '(' )
					end = result.find( ')' )

				start = result.find( '[' )
				end = result.find( ']' )
				while (start != -1 and end != -1):
					result = result[:start]+result[end+1:]
					# _dialog.substitute_dialog(result)
					start = result.find( '[' )
					end = result.find( ']' )

				print (result)

	def __str__(self):
		p = ''
		for _dialog in self.script:
			p+=str(_dialog)
		return p

	def print_class(self):
		p = ''
		for _dialog in self.script:
			print(_dialog)

friends_script = Script()

if sys.argv[1] == '1':
	friends_script.readfile('data/friends.txt','data/output')
else:
	friends_script.remove_paran('data/output')
# print(friends_script)
# friends_script.print_class()