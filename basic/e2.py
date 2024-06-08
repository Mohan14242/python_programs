#printing the current sum and previous sum 
previous=0 
for i in range(1,11):
    x_sum=previous+i
    print('the current number',i,"previous sum",previous)
    previous=i
