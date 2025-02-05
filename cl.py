# check negative number in list and sum of all postive number
a = list(map(int, input("Enter the list of numbers separated by space: ").split()))  # Input as a list of integers
n = len(a)
sum = 0  
flag = 1  

for i in a:  
    if i < 0:  
        flag = 0 
    else:
        sum=sum+i

if flag == 0:
    print("There is a negative number in the list.")
else:
    print("All numbers are non-negative.")

print("Sum of the numbers:", sum)


