# from nester20170405 import print_lol

# james_ts=[]
# julie_ts=[]
# mikey_ts=[]
# sarah_ts=[]


# try:

# 	with open('james.txt','r') as jaf:
# 		data=jaf.readline()
# 	james=data.strip().split(',') # transfer char into list.
# #	for ts in james:
# #		james_ts.append(sanitize(ts))

# 	with open('julie.txt','r') as juf:
# 		data=juf.readline()
# 	julie=data.strip().split(',')
# #	for ts in julie:
# #		julie_ts.append(sanitize(ts))
# 	julie=[sanitize(each_t) for each_t in julie]
# 	for each_t in julie:
# 		if each_t not in julie_ts:
# 			julie_ts.append(each_t)
# #		else:
# #			pass

# 	with open('mikey.txt','r') as mif:
# 		data=mif.readline()
# 	mikey=data.strip().split(',')
# #	for ts in mikey:
# #		mikey_ts.append(sanitize(ts))
# 	mikey_ts=[sanitize(each_t) for each_t in mikey]

# 	with open('sarah.txt','r') as saf:
# 		data=saf.readline()
# 	sarah=data.strip().split(',')
# 	for ts in sarah:
# 		sarah_ts.append(sanitize(ts))


	# print (sorted((sanitize(james_ts) for james_ts in james),reverse=True)[0:3])
	# print (sorted(julie_ts,reverse=True))
	# print (sorted(mikey_ts))
	# print (sorted(set(sarah_ts),reverse=True))

# except IOError as err:
# 	print ('File error: ' + str(err))


def sanitize(time_string):
	if '-' in time_string:
		splitter='-'
	elif ':' in  time_string:
		splitter=':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print ('File error: ' + str(ioerr))
		return(None)

F=['james.txt','julie.txt','mikey.txt','sarah.txt']
for fn in F:
	FD=get_coach_data(fn)
	print (fn,end='  ')
	print (sorted(set(sanitize(Fe) for Fe in FD),reverse=True)[0:3])