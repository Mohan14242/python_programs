#creating two lists from the list containing the odd and even list 
def separating_odd_even(list1):
    even_list=[]
    odd_list=[]
    for i in list1: 
        if i%2 ==0:
            even_list.append(i)
        else: 
            odd_list.append(i)
    return even_list,odd_list
list1=[1,2,3,4,5,6,7,8,9]
even,odd=separating_odd_even(list1)
print("even list",even)
print("odd list",odd)

