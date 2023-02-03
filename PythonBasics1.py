print("hello world...")
# variable
x = 5
y = "Automation"
print(x)
print(y)
print ("hello" + y)
x = 15
y = 20
print (x+y)
# syntex
if 10 > 5:
    print ("10 is greater than 5")

# function
def sum(a,b):
    print(a+b)

x = sum(20,30)

#CommandLine
#comment
#numbers
x = 5
y = 2.5
z = 4j
print(type(x))
print(type(y))
print(type(z))
#casting
x = int(2)     # 2
y = int(2.5)   # 2
z = float(1)   # 1.0
p = str(10)    #"10"
print(x)
print(y)
print(z)
print(p)
# sting operations
x = "   Hello world.."
print(x.split(","))  # index position 1, group 6 to 11 (x[6:11]) caracters, lenght (len(x)), lower, upper (x.lower()),(x.strip()), (x.replace("e","a")), (x.split(","))
# input function
print("Enter your name : ")
x = input()
print("hello, "+x)