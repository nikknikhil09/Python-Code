a=float(input("enter the marks in Maths\n"))
b=float(input("enter the marks in English\n"))
c=float(input("enter the marks in Hindi\n"))
d=float(input("enter the marks in Social Science\n"))
e=float(input("enter the marks in Science\n"))
avg=(a+b+c+d+e)/5
print(float(avg))
if(avg>=90 and avg<=100):
    print("your grade is A+")
elif(avg>=75 and avg<90):
    print("your grade is A")
elif(avg>=65 and avg<75):
    print("your grade is B+")
elif(avg>=50 and avg<65):
    print("your grade is B ")
elif(avg>=40 and avg<50):
    print("your grade is C+")
elif(avg>=30 and avg<40):
    print("your grade is C")
elif(avg>=0 and avg<30):
    print("your grade is F(Fail)")

else:
    print("Plz enter valid marks detail")

