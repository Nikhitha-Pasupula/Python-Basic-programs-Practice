# # Print & Variables

# Write a program to print Hello World

# Store your name in a variable and print it

# Store two numbers and print their sum

# Print your name and age using f-string

print("Hello World")

name = "Sonu"
print(name)

number1 = 20
number2 = 30
number3 = number1 + number2
print(number3)

name = "Monu"
age = 30
print(f"my name is {name} and i am {age} years old")


# User Input

# Take a number from the user and print it

# Take two numbers from the user and print their sum

# Take user name and age and print a greeting message

number = int(input("Enter a number: "))
print("your number is : ",number)

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = a+b
print("Your number is : ", c)

name = input("Enter your name: ")
age  = int(input("Enter your age: "))
print(f"my name is {name} and i am {age} years old")

# 3️⃣ Data Types

# Print the data type of a variable

# Convert integer to float

# Convert string number to integer

name = "Donny"
print(type(name))

number = 20
float = float(number)
print(float)

number = "2332"
int = int(number)
print(int)
print(type(int))

# Operators

# Perform all arithmetic operations on two numbers

# Check whether one number is greater than another

# Check if a number is even or odd

a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

print(a>b)
print(b>a)

if a%2 == 0:
    print("it is even")
elif a%2!=0:
    print("it is odd")
else:
    print("it is not a number")

# 5️⃣ Conditional Statements

# Check whether a number is positive or negative

# Check whether a number is divisible by 5

# Find the largest of two numbers

# Find the largest of three numbers


a = int(input("Enter your number: "))
if a<0:
    print("it is negative number")
elif a>0:
    print("it is positive number")
elif a == 0:
    print("it is 0")
else:
    print("it is not a number")

a = int(input("Enter your number: "))
if a%5 ==0:
    print(a,"this number is divisible by 5")
else:
    print(a,"this number is not divisible by 5")

a = 20
b= 100
if a>b:
    print("The largest number is: ",a)
elif a<b:
    print("The largest   number is:",b)
else:
    print("both are same")


a = 30
b = 40
c = 120
if a>b and a>c:
    print("the largest number is: ",a)
elif b>c and b>a:
    print("the largest number is: ",b)
elif c>a and c>b:
    print("the largest number is: ",c)

# Print numbers from 1 to 10 using for loop

# Print numbers from 10 to 1 using while loop

# Print even numbers between 1 and 50

# Print multiplication table of a number

for i in range(1,11):
    print(i)

numbers = 10
while numbers >=1:
    print(numbers)
    numbers-=1

i = 2
for i in range(1,51): 
    if i%2==0:
        print(i)

number = int(input("Enter your table number:  "))
for i in range(1,11):
    print(number,"x", i ,"=", number*i)

# Find length of a string

# Reverse a string

# Check whether a string is palindrome

# Count vowels in a string

name = "Sonu"
print(len(name))

print(name[::-1]) # used with slicing

print("================")

name = "Monu"
rev = " "

for i in name:
    rev = i+rev
    print(rev) #using for loop

print("=========================")

name = "Pinky"
rev = " "
i = len(name) -1 
while i>=0:
    rev = rev + name[i]
    print(rev)
    i-=1
print(rev) # using while loop

print("====================")
name = "alphabets"
vowels = "aeiouAEIOU"
counsonents = " "

for i in name:
    if i in vowels:
        print(i) #vowels

for i in name:
    if i.isalpha() and i not in vowels:
        counsonents+=i
print(counsonents) #consonents


# Create a list and print all elements

# Find sum of list elements

# Find largest number in a list

# Count even numbers in a list

list = (2,3,5,90,4)
count = 0
print(list)
print(sum(list))
print(max(list))

print("================")

for i in list:
    if i%2==0:
        count = count +1
print(count)
        
# swap  two numbers
a = 20
b = 30
c = b,a
print(c) # without creating temp variable


a = 30
b = 40
temp = b,a
print(temp) # creating with temp variable

# Fibonacci series

n = int(input("Enter your series: "))
a = 1
b = 2
print(a,b,end = " ")

for i in range(n-2):
    c = a+b
    print(c,end = " ")
    a = b
    b = c
# leap year
Year = int(input("\n Enter your Year: "))
if (Year%400==0) or (Year%100==0 and Year%4!=0):
    print("it is leap year")
else:
    print("it is not leap year")

# factorial
number  = int(input("enter your number: "))
fact = 1
for i in range(1,number+1):
    fact = fact*i
print(fact)