a=int(input("enter first side of triangle"))
b=int(input("enter second side of triangle"))
c=int(input("enter third side of triangle"))
if a+b>c and b+c>a and c+a>b:
    print("it is triangle")
    if a==b and b==c and c==a:
        print("it is equilatral triangle")
    elif a==b!=c and b==c!=a and c==a!=b:
        print("it is isoceles triangle")
    else:
        print("scalene triangle")

else:
    print("invalid triangle")