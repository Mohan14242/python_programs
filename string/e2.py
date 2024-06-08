#return the count of the given substring from a string 
def counting_string(text,sub):
    counts=text.count(sub)
    return counts
text=input("please enter the string ")
sub=input("please enter the substing")
print(counting_string(text,sub))

#another way 
def count(text1,sub1):
    print("given string",text1)
    text1=text1.replace(" ","")# herer we are removing the spaces form 
    count=0
    l=len(sub1)  
    for i in range(len(text1)):
        if text1[i:i+l] ==sub1:
            count +=1
    print("the number of occurences in the string is ",count)

text1=input("please enter the sting ")
sub1=input("please enter string ")
print(count(text1,sub1))






   