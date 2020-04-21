class Example:
    staticVariable = 5

print(Example.staticVariable) # print 5

objj =Example()
print(objj.staticVariable)

objj.staticVariable = 6
print(objj.staticVariable)

print(Example.staticVariable)


