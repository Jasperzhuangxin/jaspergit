
from nester20170405 import print_lol
import os
import sys
import pickle

man=[]  # create a blank list.
other=[]
new_man=[]
new_other=[]

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

# try:
# 	with open('man_date.txt','w') as man_file:
# 		print_lol (man, True, fn=man_file)
# 	with open('other_data.txt','w') as other_file:
# 		print_lol (other, True, fn=other_file)
# except IOError as err:
# 	print ('File Error: ' + str(err))


try:
	with open('man_data.txt','wb') as man_file:
		pickle.dump(man,man_file)
	with open('other_data.txt','wb') as other_file:
		pickle.dump(other,other_file)
except IOError as err:
	print ('File Error: ' + str(err))
except pickle.PickleError as perr:
	print ('Pickling error: ', str(perr))

try:
	with open('man_data.txt','rb') as man_file:
		new_man = pickle.load(man_file)
	with open('other_data.txt','rb') as other_file:
		new_other = pickle.load(other_file)
except IOError as err:
	print ('File error: ' + str(err))
except pickle.PickleError as perr:
	print ('Pickling error: ' + str(perr))

print_lol(new_man)
print ("---------------------------------------------------")
print_lol(new_other)
print ("---------------------------------------------------")
print (new_man[0])
print ("---------------------------------------------------")
print (new_man[-1])