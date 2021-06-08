

#1.Write a program that uses input to prompt a user for their name and then welcomes them.

name = input('Enter your name')
print('Welcome',name)

#2.Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature."""

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

#3.Write a Python program to convert degree to radian."""

pi=22/7
degree= float(input("input degrees :"))
radian= degree*(pi/180)
print('%.2f degree is: %0.2f radian' %(degree, radian))
