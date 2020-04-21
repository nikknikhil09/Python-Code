str=input("input a string\n")
str1=""
for c in str:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        str1+='z'
    else:
        str1+=c

print(str1)
