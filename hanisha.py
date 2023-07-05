


'''
This is called a returning function where by if the values in test1 are  equal to the values in test2 return values in test1
else return those in test2 and after you have to enter the values of test1 and test2 on line19 and 20
"If" statement in the function is aconditional statement which works with "else" and"return" e.g
if test1 == test2:return test1,else:return those in test2 
'''


def tests(test1, test2):
	#Tests is a defined function and test1 and test2 are parameters.
	if test1 == test2:
		#If the value in test1 is equal to the values in test2 return values in test1
		return test1
	else:
		#If they  equal return the results in test2.
		return test2
#The statements below are instructing us to enter value for test1 and in test2
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
We have a defined function called courseWrk and cswork is parameter,where by we have to get the average Cswork
by adding the values in test1 and test2/2 to get the average but before that we have to get the valuses of avariable testMark by adding 
the values in test1 and test2 after that we get fnltestsCswork by getting the avgtestCswork*(40/100)
and then we print the fnlestCswork.
'''
def courseWrk(cswork):
	#The defined function is courseWrk and  (cswork)is aparameter
	testsMark = tests(test1,test2)
	#Inside the test function is called by functions test1 and test2
	avgtestsCswork = (cswork + testsMark)/2
	#We are getting the average mark for cswork
	fnltestsCswork = avgtestsCswork * (40/100)
	#This ('........................')separates the final work from the pervious work.
	print('..............................')
	#Results for fnltestCswork is printed here
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
#Here we are supposed to put the coursework
cswork = int(input('Please enter your course work Marks: '))
#We are calling the function courseWrk which is equal to the interger and it tells the user to input the course work marks
courseWrk(cswork)

'''
In python2 we had two function(input and the raw_input)though input at first it was just astatement but later on it was changed
to be a function.the input prompts a user to input values from the keyboard,however it captures everything from the
keyboard as a string.
Input is now not used in python2 but instead we use raw_input which captures strings.though even if we use the input function
we can still run the code and the input function displays everything as astring.
The reason why we have input in code it is because that we except to input the course work marks as interger,numeric and it
will displays this as astring e.g if we input(2000) the computer reads it as 2 0 0 0.
print('....................')this just seperates the work and (def) stands for defined function,(cswork) is aparameter,
(=)is an assignment operator,(*)muliplication sign,(/)division sign or operator,(==)is equal to operators.
'''
