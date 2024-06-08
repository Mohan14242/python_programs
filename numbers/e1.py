#check the number is palidrom or not 
def parlidrom_or_not(num):
    if num[::-1] == num:
        print("the number is palidrom")
    else: 
        print("the numer is not palindrom")
parlidrom_or_not("125")