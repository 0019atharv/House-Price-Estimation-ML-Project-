#Assignment No. : 22
#Title          : Creating a CSV File.
#Date           :
#Submitted by   : Atharv Bharadwaj
#Code

import csv
f=open('abc.csv','w',newline='')
r=csv.writer(f)
r.writerow(['EmpNo','Empname','Empsalary'])
for i in range(5):
    Eno=int(input('Enter the employee number : '))
    Ename=input('Enter the name of employee : ')
    Esal=int(input('Enter the salary of employee : ₹ '))
    r.writerow([Eno,Ename,Esal])
f.close()
