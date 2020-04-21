list1 = [11, -21, 0, 45, 66, -93] 
list2=[]  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if num >= 0: 
       list2.append(num) 
print(list2)    
total=sum(list2)   
print("sum of positive number in list = ",total)