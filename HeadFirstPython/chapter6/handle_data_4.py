
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
	def top3(self,c):
		return(sorted(set(sanitize(t) for t in self.times),reverse=True)[0:c])

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
		templ=data.strip().split(',')
		return(Athlete(templ.pop(0),templ.pop(0),templ))
	except IOError as ioerr:
		print ('File error: ' + str(ioerr))
		return(None)


F=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
for fn in F:
	FN=get_coach_data(fn)
	print (FN.name + "'s fastest times are: " + str(FN.top3(5)))