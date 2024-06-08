#printing the chracters that are in the even indexs
text=input("pleaseenter the text")
text_with_out=text.replace(" ","")
print(text_with_out)

for i in range(0,len(text_with_out),2): 
    print(f'the index{i}',text_with_out[i])

#second solution 
text1=input("please enter the text")
text_with_out1=text1.replace(" ","")
text_with_out1=list(text_with_out1)
for i in range(0, len(text_with_out1),2):
    print(f"the index {i}",text_with_out1[i])