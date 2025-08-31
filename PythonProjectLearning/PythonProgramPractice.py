# Loops and Control Flow Statements

# Write a Python program to print all even numbers from 1 to 100 using a for loop.
print("Even numbers from 1 to 100:")
for i in range (1,101):
    if i%2==0:
        print (i)

print("-------------------------------------------------------------------")
# Write a Python program to find the sum of all numbers from 1 to 100 using a while loop.
print("Sum of all the numbers from 1 to 100:")
i=1
sum=0
while i<=100:
    sum = sum + i
    i +=1
print(sum)

print("-------------------------------------------------------------------")
# Write a Python program to print the Fibonacci sequence up to n terms using a for loop.
x=0
y=1
num= int(input("Enter the number to print Fibonacci series: "))
print(x)
print(y)
for i in range(num):
    z=x+y
    print(z)
    x=y
    y=z

print("-------------------------------------------------------------------")
# Write a Python program to check if a given number is prime or not using a while loop.
number=int(input("Enter any number to check if prime or not:"))
count=0
num=1
while num<=number:
    if number%num==0:
        count +=1
    num +=1
if count==2:
    print("The number is prime")
else:
    print("The number is not prime")

print("-------------------------------------------------------------------")
# Write a Python program to print the multiplication table of a given number using a nested loop.
number=int(input("Enter any number for the multiplication table:"))
print("The multiplication tables till", number)
for i in range(1,number+1):
    print("Multiplication table of ", i)
    for j in range(1,11):
        print( i, "*", j, "=",  i*j)
    i +=1

print("-------------------------------------------------------------------")



print("-------------------------------------------------------------------")




