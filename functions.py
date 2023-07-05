#is grouped statement
num1 = 50
num2 = 100
num3 = num1+num2
print(num3)

def sum():
    num1, num2 = 30,50
    num3 = num1+ num2
    print(num3)

sum()

def sub():
    num1, num2 = 200,100
    num3 =num1- num2
    print(num3)

sub()

def rem():
    num1, num2 = 9,5
    num3=num1%num2
    print(num3)

rem() # here am calling the function rem() above
def my_list():
    List1 =[1,2,3,4,5,6,7,8,9]
    print(List1[0])
rem() 

'''
Declaring my_tuple function.
'''

def my_tuple():
    my_tuple = (10,20,30,40,50)
    zebra = {'name':'tongs','legs': 4, 'color': 'black & white', 'sex': 'male'}
    print(zebra.keys())
    print(zebra.values())
    zebra.__delitem__('sex')
    print(zebra)

    my_tuple()
    '''
    Declaring fruits funtion.
    '''

def fruits():
    osman =[100,[200]]
    print(osman[1][0])
    osman2 = [1000,[[2000,3000]]]
    print(osman2[1][0][1])

    osman.append(1000)
    osman.pop()
    print(osman)
    fruits =['orange','pineapple']
    fruits.append('apple')
    print(fruits)
    fruits.pop()
    print(fruits)
fruits()
'''
Declaring list function.
'''

def list():
    osman =[100,[200]]
    print(osman[1][0])
    osman2 = [1000,[[2000,3000]]]
    print(osman2[1][0][1])
list()
# The above are called statics functions.    

    