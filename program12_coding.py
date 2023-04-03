#Assignment No. : 12
#Title          : Writing data to a text file.
#Date           :
#Submitted by   : Atharv Bharadwaj

#Code

f=open('s1.txt','w')
s='''Twinle Twinle Little Stars.
A Pocket Full Of candies.
A boy is coming here.'''
f.write(s)
f.close()

f=open('s1.txt','r')
d=f.read()
print(d)
f.close()

