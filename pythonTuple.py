my_tuple = ("apple","Orange","Grapes")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

print(len(my_tuple))
my_tuple_2 = ("Banana",(1,2,3),["Tokyo","New York"])
print(my_tuple_2)
print(my_tuple_2[2][1])
my_tuple_2[2][1] = "Sherman"
print(my_tuple_2)
print("Banana" in my_tuple_2) # True
print("cherry" in my_tuple_2) # false