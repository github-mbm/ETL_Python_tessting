'''
Name=input("enter your name")
print(Name)
'''

#Control Statements

'''
age=50
if age <18:
    print("Child")
elif age >18 and age<30:
    print("Adult")
else:
    print("Elder")
print("complated")

'''

#looping
#Range=> Gives sequence =Range(20)=start from 0 end 19 and stepping 1
#range(1,20,2)=1,3,5,7,9,11,13,15,17,19
#range(2,20,3)=2,5,8.. start from 2 step at 3 .here 3 means 2,3,4 so 5 will come
'''
#Total no of record counts

Source=1000
Target=900
if Source==Target:
    print("Total records from source to target matching")
else:
    print("Records not matching")
Missing_records=Source-Target
print("Misisng records",Missing_records)

#Every 5th recorded is failing
records=20
for i in range(1,21):
    if i%5==0:
        print(i)
        



n=4
fact=1
for i in range  (1,n+1):
    fact=fact*i
print(fact)



N=10
for i in range(2,N):
    if N%i==0:
        print("not prime number")
        break
    else:
        print("prime")

Input: n = 12345
Output: 5
Explanation: (Number of digits in 12345 is 5)
'''
n=5
sum=0
for i in range(n+1):
     sum=sum+i
print(sum)


