import re
print(f'Input Format : "h._._.l.o."')
with open('Refined_list.txt') as file:
	words = file.readlines()
	words = [word.strip('\n') for word in words]
	find = input('Enter word : ')
	while find:
		#find = input('Enter word : ')
		find = find.replace('.','')
		length = len(find)
		suspects = [word for word in words if len(word) == length] 
		
		find = find.replace('_','.')
		for suspect in suspects:
			a = re.search(find,suspect)
			if a:
				print(f'try : {suspect}')
		find = input('Enter word : ')
