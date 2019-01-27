
weight = 55
print(weight)
print('its weight is', weight/2)

import numpy
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

print(type(data))
print(data.dtype)
print(data.shape)
print(data)

print('values are', data[0,0], data[2,3])
print(data[0,0:4]) #slicing
print(data[0:4,0:4])

var = data[0,0:10]
print(var)
print(var.dtype)
print(var.mean())

word = 'SpydEr pyThON'
title= word[0:3]
print(word[1],word[4],word[8:11])
print(word, 'is a', title)

print(word.lower())

for char in word:#loop
    print(char)

sw_list = ['dda','def','uyt']
print(sw_list)

for ss in sw_list:
    print(ss)

for ss in sw_list:
    print('----')
    for chart in ss:
        print(chart)

s='yutgr'
print(len(s))
print(len(sw_list))

letter='z'
print(letter)
for letter in 'abc':
    print(letter)
print(letter)

i=0
for char in s:
    i=i+1
    print(char,i)
    print(i,'wow',char)

s1='jjj'
s2='eee'
s3=s1+' '+s2
print(s3)

a='vader'
w=''
for m in a:
    w=m+w   #reverse
print(w)

a='vader'
w=''
for m in a:
    w=w+m   #not reverse
print(w)

var = 1
if var > 25:
    print('...')
else:
    print(',,,')


print ('da'=='da')

#in python, empty('')means faulse and not existing, 
#it can be used for clesning list including empty messages
if 'content':
   print('lalalal')
if '': 
   print('...')












