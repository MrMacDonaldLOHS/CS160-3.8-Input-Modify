# Oh dear! This code does not work! 
# It is your job to get it working
# There are many errors in this code. Try to fix them one at a time until
# things run correctly! 

name = int(input("Hi! What's your name? "))
# These empty prints make the test results easier to read the test results when it runs
print()
print("Hi " + name + "! How are you today?")

num1 = input(name + " give me a whole number: ")
print()
num2 = int(input(name + " give me another whole number: "))
print()
answer = num1 * num2;
print (str(num1) + " * " + num2 + " = " + str(answer))
print()

num1 = int(input(name + " give me a number with a decimal point: "))
print()
num2 = float(input(name + " give me another number with a decimal point: "))
print()
answer = num1 / num2;
print (num1 + " / " + num2 + " = " + answer)

