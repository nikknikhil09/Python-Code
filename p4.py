#dict={'1':['a','b'],'2':['c','d']}
#a=dict['1']
#b=dict['2']
#for i in a:
 #   for j in b:
  #      print(i,end="")
   #     print(j)
   
    
"""list1=[]
n=int(input("enter no of value for fst key\n"))
print("enter value for fst key\n")
for i in range(n):
    ele=input()
    list1.append(ele)

print(list1)
list2=[]
n=int(input("enter no of value for 2nd key\n"))
print("enter value for 2nd key\n")
for i in range(n):
    elem=input()
    list.append(elem)

print(list2)

dict={'1':list1,'2':list2}
a=dict['1']
b=dict['2']
for i in a:
    for j in b:
        print(i,end="")
        print(j)"""
    

dsize=int(input("enter the number of key in dictionary:\n"))
key=[]
val=[]

for i in range(dsize):
    n=int(input("enter key no"))
    key.append(n)
    m=[]
    for j in range(int(input("enter no of value for key"))):
        v=input("enter value")
        m.append(v)
    val.append(m)

print(key)
print(val)
dictt={key[i]:val[i] for i in range(dsize)}
print(dictt)

for i in val[0]: #loop for value at 0 index
    for j in val[1:]: # loop for futher values in dict
        for k in j:     #loop for k value in value list 
            print(i,k)        

