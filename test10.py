def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

n=int(input("enter number"))
print(add_digits(n))
#print(add_digits(59))