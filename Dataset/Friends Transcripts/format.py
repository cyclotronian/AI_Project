same_dialog = 0	
same_paran = 0	#1: open paran

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
		self.script = []

	def readfile(self,filename):
		with open(filename,'r') as file:
			for line in file:
				#lowercase 
				line=line.lower()
				
				#mark end of episode
				if line[:-1] == 'End':
					self.episode_end = True
				
				a = line[:-1].split(':')
				
				#ignore lines starting with "note"
				if a[0]=='(note': continue
				
				if len(a) > 1: 

					#if a character is speaking, start a new dialog
					if len(a[0].split(' '))==1:
						
						# if self.dialog_status=='no_one_speaking':
						self.script.append(Dialog(a[0]))
						self.script[-1].append_dialog(a[1])
						self.dialog_status='some_one_speaking'

					# else:
					# 	print 'WAAAAAAAA'
					
				elif self.dialog_status=='some_one_speaking':
					if self.episode_end == True:
						self.episode_end = False
						self.dialog_status=='no_one_speaking'
						continue
					self.script[-1].append_dialog(line[:-1])

	def remove_paran(self):
		for _dialog in self.script:
			start = _dialog.dialog.find( '(' )
			end = _dialog.dialog.find( ')' )
			while (start != -1 and end != -1):
				result = _dialog.dialog[:start]+_dialog.dialog[end+1:]
				_dialog.substitute_dialog(result)
				start = _dialog.dialog.find( '(' )
				end = _dialog.dialog.find( ')' )

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
friends_script.readfile('data/friends.txt')
friends_script.remove_paran()
print(friends_script)
# friends_script.print_class()