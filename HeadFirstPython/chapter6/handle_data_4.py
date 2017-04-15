
def sanitize(time_string):
	if '-' in time_string:
		splitter='-'
	elif ':' in  time_string:
		splitter=':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter,1)
	return (mins + '.' + secs)

class Athlete:
	def __init__(self,a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
	def top3(self,c=3):
		return(sorted(set(sanitize(t) for t in self.times),reverse=True)[0:c])
	def add_time(self, time_value):
		self.times.append(time_value)
	def add_times(self,list_of_times):
		self.times.extend(list_of_times)

class NamedList(list):
	def __init__(self,a_name):
		list.__init__([])
		self.name = a_name


class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_times=[]):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	def top3v2(self, c=3):
		return(sorted(set([sanitize(t) for t in self]))[0:c])


def get_coach_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
		templ=data.strip().split(',')
		return(AthleteList(templ.pop(0),templ.pop(0),templ))
	except IOError as ioerr:
		print ('File error: ' + str(ioerr))
		return(None)

F=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
for fn in F:
	FN=get_coach_data(fn)
	print (FN.name + "'s fastest times are: " + str(FN.top3v2(5)))

vera=Athlete('vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:33'])
print ('+++++++++++++++++++++++++++++++++++++++++++++')
johnny = NamedList("Jasper Wang")
print ('johnny type is ' + str(type(johnny)))
# print (dir(johnny))
johnny.append("Bass Player")
johnny.extend(['Composer','Arranger','Musician'])
print ('********************************************************')
abcdef = {}
abcdef[johnny.name]=johnny
print (abcdef)

print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print (johnny.name)
print (johnny)
print ('+++++++++++++++++++++++++++++++++++++++++++++')

print (johnny.name + ' is a ', end=' ')
for attr in johnny:
	if attr == johnny[-1]:
		print (attr)
	else:
		print (attr + ' & ', end='')
print ('---------------------------------------------')
vera2 = AthleteList('vera2 vi')
vera2.append('1.31')
print (vera2.top3v2(5))
vera2.extend(['2.22','1-21','2.33'])
print (vera2.top3v2(5))