#remvoe the n character from the string 
def remove_chracteers(char,n):
    print("the original string",char)
    remmoved_string=char[n:]
    return remmoved_string

text=input("please enter the text that you want to process")
n1=int(input("please enter the characters that you want to remvoe from the string "))
print(remove_chracteers(text,n1))
#position based character removing the strings 
def remove_position_based_characters(text1,n2,position):
    if len(text1) > n2 :
        if position == "end":
            print("origin string is",text1)
            removed_string1=text1[:n2]
        else: 
            removed_string1=text1[n2:]
            return removed_string1
    else: 
        print("the len of the numbers should be less the lenght of the text")
text1=input("please enter the string ")
n2=int(input("please enter the most of the scenrios to get the hell "))
try:
    position=input("please enter the postion in (end/start)")
except ValueError: 
    print("some exception has occured")

print(remove_position_based_characters(text1,n2,position))