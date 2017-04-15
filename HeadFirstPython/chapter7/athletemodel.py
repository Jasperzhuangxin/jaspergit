import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	# Not shown here as it has not changed since the last chapter.
	try:
		with open(filename) as f:
			data=f.readline()
		templ=data.strip().split(',')
		return(AthleteList(templ.pop(0),templ.pop(0),templ))
	except IOError as ioerr:
		print ('File error: ' + str(ioerr))
		return(None)

def put_to_store(files_list): 
	# It should provide a file name as a single parameter while call this function.
	all_athletes = {}
	for each_file in files_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print ('File error (put_to_store): ' + str(ioerr))
	return(all_athletes)


def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print ('File error (get_from_store): ' + str(ioerr))
	return(all_athletes)

# print (dir())
F=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
data=put_to_store(F)
print (data)

print ('********************************************************')

for each_athlete in data:
	print (data[each_athlete].name + '  ' + data[each_athlete].dob)

print ('********************************************************')

data_copy = get_from_store()
for each_athlete in data_copy:
	print (data[each_athlete].name + '  ' + data[each_athlete].dob)

