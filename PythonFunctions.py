#functions
def func_name(parameter):
    body

def printHello():
    print("Hello")
printHello()

def printHi(name="John"):
    print("Hi,"+name)

printHi("Andrew")
printHi()

def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)

def returnSum(a,b):
    return (a+b)
x = returnSum(10,20)
print(x)


# if else condition
x = 30
y = 30
if x>y:
    print(x,"is greatyer")
elif y>x:
    print(y, "is greater")
else:
    print( "Both are equal")

def helloUser(name):
    print("Hello", name)
helloUser("Andrew")

def helloPerson(**name):
    print("hello",name["lname"])
helloPerson(fname="Andrew", lname="Medoua")