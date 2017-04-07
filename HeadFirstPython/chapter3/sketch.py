# import os
# os.chdir('../HeadFirstPython/chapter3')
# print (os.getcwd())
try:
    data=open('sketch.txt')
# print (data.readline(), end='')
# print ("--------")
# data.seek(0)

    for each_line in data:
	    try:
		    (role, line_spoken)=each_line.split(':',1)
		    print (role, end='')
		    print (' said: ',end='')
		    print (line_spoken,end='')
	    except ValueError:
		    pass

    data.close()
except IOError:
	print ('The data file is missing!')
