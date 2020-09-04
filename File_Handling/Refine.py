"""
i/p: pass file with list of words 
o/p: list of words which are valid
"""


def check(line):
	""" Checks for Validity letter by letter """
	
	
	for letter in line.lower():
		
		if  not 'z' >= letter >= 'a' :
			
			return False
		
	return True



with open('word_list.txt') as file:
	
	data = file.readlines()
	with open('Refined_list.txt' , 'w') as wr:
		
		for line in data:
			line = line.strip()
			
			if len(line) > 1 and check(line):
				
					
				wr.write(line + '\n') 
	









#eof

