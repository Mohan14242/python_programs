#check the first and last number of the list are same or not 
def check_first_last(num1,num2):
    if num1[0]==num2[-1]:
        print("both are equal ")
    else: 
        print("both are not equal")
user_input1=input("please entetr the numbers for list1")
try: 
    num1=[int(num) for num in user_input1.split(",")]
except ValueError as e: 
    print(f'the exception has occurred perform based on that',e)

user_input2=input("please enter the numbers for input2 ")
try: 
    num2=[int(num) for num in user_input2.split(",")]
except ValueError as e: 
    print("the eceptions has occured is ",e)
check_first_last(num1,num2)