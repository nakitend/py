'''
'''


class Girl:
    name = 'Hanisha'
    age = '22'
    gender = 'Female'
    size = '34'
    family = 'ssemwogerere'
    size_of_bra = 'small'
    def dress():
        print('nicely')
    def greet():
        print('Hello world')
        return ''
Girl.greet()
Girl.dress()
print(Girl.name)
print(f"{Girl.name} is {Girl.age} years old and {Girl.gender} is")
girl2 = Girl()
girl2.name = 'vanessa'
girl2.age = '16'
girl2.gender = 'Female'

girl3 = Girl()
girl3.name = 'trinty'
girl3.age = '18'
