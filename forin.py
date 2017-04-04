list1 = ['1', '1']
list2 = ['A','B']

for x in list1, list2:
    result = x[:]
    print (result)    # type=list

print ("---------")

print (list1, list2)

print ("#############")

list1 = ['1', '1']
list2 = ['A','B']

for x in list1, list2:
    result = x[:]
print (result)    # type=list

print ("---------")

print (list1, list2)

print ("#############")





# simple
dir = {'A': 'a', 'B': 'b'}
       
xq = list(dir.keys())
yw = list(dir.values())


for i in xq, yw:
    answer, question = i[:]
    print (answer, ",", question)

print ("---------")

# complex
for j in xq:
    answer_ = j[:]
    print (answer_, ",",)
    
print ("\n")

for k in yw:
    question_ = k[:]
    print (question_, ",",)





