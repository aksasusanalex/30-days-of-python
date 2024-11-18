a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a+b>c and a+c>b and b+c>a:
    print("its a triangle")
    if a == b and b == c and a == c:
        print("its a equilateral triangle")
    elif a == b != c or a == c != b or b == c != a:
        print("Isosceles triangle")
    else:
        print("scalene triangle")


else:
    print("invalid triangle")
