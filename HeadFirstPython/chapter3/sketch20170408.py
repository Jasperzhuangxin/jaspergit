
from nester20170405 import print_lol
import os
import sys

man=[]
other=[]
try:
	data=open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken)=each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
			# print (role, end='')
			# print (' said: ', end='')
			# print (line_spoken, end='')
		except ValueError:
			pass
	data.close()

except IOError:
	print ('The data file is missing!')

# try:
# 	man_file=open('man_date.txt','w')
# 	other_file=open('other_data.txt','w')
# 	print (man,file=man_file)
# 	print (other,file=other_file)
# except IOError:
# 	print ('File Error.')

# finally:
# 	if 'man_file' in locals():
# 		man_file.close()
# 	if 'other_file' in locals():
# 		other_file.close()

try:
	with open('man_date.txt','w') as man_file:
		print_lol (man, True, fn=man_file)
	with open('other_data.txt','w') as other_file:
		print_lol (other, True, fn=other_file)
except IOError as err:
	print ('File Error: ' + str(err))





