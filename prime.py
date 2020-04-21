n=int(input("enter number\n"))
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("Number not prime")
            break
    else:
         print("Number is prime")
else:
    print("num not Prime")
