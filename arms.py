number=int(input("enter the number\n"))
s=0;tmp=number
while tmp>0:
    n=tmp%10
    s=s+n**3
    tmp//=10
if number==s:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
