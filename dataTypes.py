#numeric,string,squence,mapping,boolean,set
#numeric(int,float,complex)
num1 = 1000
num2 = 1000.0
num3 = 1+5j
num4 = "100"
name = "hanisha"
print(type(num1))
print(type(num2))
print(type(num3))
#string(str)
print(type(num4))
print(type(name))
#squence(list,tuple,range)
myList = [2,4,6]
myList2 = [0,2,4,6,"hanisha",0.9]
my_tuple = (0,2,4,6)
my_dict = {"uganda" : "kampala", "italy" : "Rome", "france" : "paris", "tz" : "dodoma"}

print(type(myList))
print(type(myList2))
print(type(my_tuple))
#mapping(dict)
print(type(my_dict))
#boolean(True or False)
#set()
my_set = {0,5,10,15,20}
print(my_set)
my_set2 = {10,10,5,5,15,15,20,20}
print(my_set2)
print(set(my_dict))
