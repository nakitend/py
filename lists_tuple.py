#list,tuple and dict in details
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[5])
my_list2 = [10,20,30,40,50]
print(my_list2[4])
print(my_list2[-1])
osman =[100,[200]]
print(osman[1][0])
osman2 = [1000,[[2000,3000]]]
print(osman2[1][0][1])


#examples of mutable list
osman.append(1000)
osman.pop()
print(osman)
fruits =['orange','pineapple']
fruits.append('apple')
print(fruits)
fruits.pop()
print(fruits)

my_tuple = (10,20,30,40,50)
zebra = {'name':'tongs','legs': 4, 'color': 'black & white', 'sex': 'male'}
print(zebra.keys())
print(zebra.values())
zebra.__delitem__('sex')
print(zebra)