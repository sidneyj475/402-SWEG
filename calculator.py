import math
print("Welcome to Calculator")
print(" ")

print("1. Addition\n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponent \n6. Square Root")
print(" ")

operation=input("Choose an operation: ")
print(" ")

num1=input("Enter a number: ")
num2=input("Enter another number: ")
print(" ")


result1=float(num1)+float(num2)
result2=float(num1)-float(num2)
result3=float(num1)*float(num2)
result4=float(num1)/float(num2)
result5=float(num1)**float(num2)
result6=math.sqrt(float(num1))
if operation=="1":
    print(result1)
elif operation=="2":
    print(result2)
elif operation=="3":
    print(result3)
elif operation=="4":
    print(result4)
elif operation=="5":
    print(result5)
elif operation=="6":
    print(result6)