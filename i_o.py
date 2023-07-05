def paye(salary,name):
    rate = 0.3
    tax = rate*salary
    net_pay = salary-tax
    print("**************")
    print("Dear: ",name)
    print("Your tax patable is ",tax)
    print("And you take home salary is: ",net_pay)
    print("..............")






    
print("Your welcome! ")
name = raw_input("please input your name here: ")
salary = input ("please input your salary here: ")


paye(salary,name)
   