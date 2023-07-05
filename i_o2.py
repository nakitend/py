def paye(salary,name,age,location,occupation):
    current_year = int(input("please enter the current year: "))
    Year_of_birth = int(input("please enter birth year: "))
    age = current_year-Year_of_birth
    print("your age is: ",age)
    rate = 0.3
    if salary >= 300000:
      tax = rate*salary
      net_pay = salary-tax
      print("**************")
      print("Dear: ",name,age,location,occupation)
      print("age: ",)
      
      
      print("Location: ","mpigi")
      print("Occupation: ","software_developer")
      print("Your tax patable is ",tax)
      print("And you take home salary is: ",net_pay)
      print("................................................")
    else:
       print("Dear: ",name,age,location,occupation)
       print("Your salary is none_taxable")
       print("**********************************************")




    
print("Your welcome! ")
name = raw_input("please input your name here: ")
age = input("please enter your year of birth: ")
location = raw_input("please input your location: ")
occupation = raw_input("please input your occupation: ")
salary = input ("please input your salary here: ")
print("Thank you sir/mada! ")


paye(salary,name,age,location,occupation)
   