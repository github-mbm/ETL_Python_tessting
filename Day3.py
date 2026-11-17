
#List

'''
l1=['sham','ram','gansham','ali','john']
for i in l1:
    print(i)

for i in range(5):
    print(i)


#get the 3rd item to end and craete a new list
New_list=[]
l1=['sham','ram','gansham','ali','john']
for i in range(2,5,1):
   # print(l1[i])
    New_list.append(l1[i])
print(New_list)

#using slicing
New_lists=l1[2:5:1]
print(New_lists)


#get me 1st 3rd and 5th elemt from list
l1=['sham','ram','gansham','ali','john']
New_lists=l1[0:5:2]
print(New_lists)



#Tuple
T1=('sham','ram','gansham','ali','john')
#fstring
print(f"Tuple items are {T1}")

#set
S1={'sham','ram','gansham','ali','ram'}
#print(f"set is {S1} and data type is {type(S1)}")
print(S1)
S1.add("Mohan")
print(S1)
for ele in S1:
    print(ele)
    '''




