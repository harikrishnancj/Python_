

def dev(Number):
    n=Number+1
    i=0
    j=0
    for i in range(1,n,1):
            if Number%i==0:
                j=j+1
           
    return j
 
num=int(input("enter the number :"))
ans=dev(num)
print("f(",num,")","=",ans)