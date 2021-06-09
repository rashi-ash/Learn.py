# 1)  Write a program which takes a number as input from the user and check whether the number is odd or even.
#     If odd print the number is odd if not print it is even.
num = int(input("Enter a number: "))
if (num % 2) == 1:
   print("Entered number is odd")
else:
   print("Entered number is even")
 


 # 2) Write a program to find the largest among three numbers and print the largest number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1>num2) :
  print("Largest number is ",num1)
elif (num2>num3):
  print("Largest number is ",num2)
else:
  print ("Largest number is ",num3)

  # 3) Write a function to prompt for a score between 0.0 and 1.0.

score=float(input("enter the score :"))

if score<=1.0:

   if score >=0.9:

       print("A")

   elif score>=0.8:

       print("B")

   elif score>=0.7:

       print("C")

   elif score>=0.6:

       print("D")

   else:

       print("F")

else:

   print("Error! please print the marks between '0.0 - 1.0")