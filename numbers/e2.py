#extract each digit from an interger in reverse order
def reverse_order(num):
    print("the reverser order is ")
    for i in num[::-1]: 
        print(i)
def normao_order(num):
    print("the original order is ")
    for i in num: 
        
        print(i)

num=input("please enter your number")
reverse_order(num)
normao_order(num)


number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
