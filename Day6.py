'''
#String Slicing
#s[Start:Stop:Step]
s="Banglore"
#first 4 chars
print(s[0:4])

#last 4 char

end=len(s)
start=end-4
print(s[start:end])

print(s[-1:-4-1:-1] # Prints reverse

len=len(s)
start=end-4
end=len-1
print(s[start:end+1])


st="BangaloreCity"
#Q1   print from 4th to 10th
start=3
end=10
print(st[start:end])

#Q2  second lsdt chsr to 4rh last har
start=-1
end=-4
print(st[start:end-1:-1])

#reverse a string

print(st[::-1])

'''

#Q3 reverse a words in strin
s="ETL QA Labs" #outpt Labs QA ETL
words=s.split()
rev=" ".join(words[::-1])
print(rev)
Sarra@1234@dev
#Q6. How to return a substring which starts with “Q” and ends with “B”
s1 = "ETLQALABS"
start=s1.find("Q")
end=s1.find("B")
print(s1[start:end+1])
