#loops helps a computer to repeatedly perform the specfic task
def my_count():
    for number in range(10):
        print(number)
my_count()
# acessing list elements using loops.
def example2():
    languages = ["python","java script","c++","c#","java"]
    for language in languages:
        print(language)
example2()

def example3(num3):
    for number in range(num3):
        print(number)
example3(10)
example3(7)

def my_lang():
    languages = ["python","java script","c++","c#","java"]
    for language in languages:
        if language == "python":
            print("you are currently in python class")
my_lang()

def odd(num):
    for number in range(num):
        if number % 2 != 0:
           print(number)
odd(10)
def power(p):
    my_po =p**2
    if my_po % 2==0:
        print("the power is an even number")
    else:
        print("the power is an odd number")
power(34)            


            

            





