a =input("print if enter the number")
a=int (a)
if a>0:
    b=str(a)
    c=len(b)
    print("lenth=",c)
elif a<0:
    b=float(a)
    d=a*a
    print("square",d)
else:
  print("a cannot be zero")