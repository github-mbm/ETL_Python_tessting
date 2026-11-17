'''
Strings:-sequence of char enclosed in quptes

Str="ETL QA Labs"
start=0
end=len(Str)
#print(start)
#print(end)
for i in range(start,end):
    print(Str[i])


## String Slicing
#First 3 letters

print(Str[0:3])

#From 0 to end
print(Str[0::])

#Reverse string
print(Str[::-1])

'''
#step from 3
Str="ETL QA Labs"
print(Str[0:10:3])
print(Str.replace("Labs","Lab"))
print(Str.find("Labs"))
print(Str.count("L"))
Splited_list=Str.split()
print(Splited_list)

Gmail="Vandana@thegragein.com"
gmail=Gmail.split("@")
print(gmail)

Phone_num="9741-780-187"
phone=Phone_num.split("-")
print(phone)


