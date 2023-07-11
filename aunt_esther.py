my_list = []  
def student():
    print("**************************")
    print("Your are welcome to esther junior school")
    name_of_child = input("please enter your name here: ")
    first_name = input("please enter your first name: ")
    last_name = input("please enter your last name: ")
    date_of_birth = int(input("please enter your date of birth: "))
    class_of_child = input("please enter your class: ")
    location = input("please enter your location: ")
    parent_name = input("please enter parent name: ")
    payment_status = input("enter payment status of a child(yes/no):")

    
    students = {"Name":name_of_child,
                'firstname':first_name,
                'lastname':last_name,
                'dateofbirth':date_of_birth,
                'level': class_of_child,
                'location':location,
                'parentname':parent_name,
                'paymentstatus': payment_status
                
                          
                       
                }
       
    my_list.append(students)
    print(my_list)
    print("amount_paid:100000")
    

student()