# data=open('sketch.txt')
# print (data.readline(), end='')
# print ('----------------------------')
# print (locals())
# print ('----------------------------')
# print (data)

# print ('----------------------------')

try:
	data=open('missing.txt')
	print (data.readline(), end='')
except IOError as err:
	print ('File Error: ' + str(err))
finally:
	if 'data' in locals():
		data.close()



