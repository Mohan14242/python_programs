#display the numbers devideb ny 5 
def numbers_divide_by5(num):
    num=[1,2,3,4,5,6,7,8,9,10]
    for i,j in enumerate(num): 
        if j % 5==0: 
            print(f"the number is divided by 5 and index {i}",j)
num=[10,20,30,40,50,60]
numbers_divide_by5(num)