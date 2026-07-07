#Get user input
num1=int(input("Enter number a:"))
num2=int(input("Enter number b:"))
num3=int(input("Enter number c:"))

#Get the order(eg.c,b,a or c,a,b)
order=input("Enter the order:")

#Make condition

if order=="a,b,c":
    numbers=num1,num2,num3
elif order=="c,b,a":
    numbers=num3,num2,num1
elif order=="c,a,b":
    numbers=num3,num1,num2
elif order=="a,c,b":
    numbers=num1,num3,num2
elif order=="b,c,a":
    numbers=num2,num3,num1
elif order=="b,a,c":
    numbers=num2,num1,num3
else:
    print("Invalid order")
print("After swapping:", numbers)
#other solution
#a = 10
#b = 20
#c = 30

#a, b, c = c, a, b

#print(a, b, c)
