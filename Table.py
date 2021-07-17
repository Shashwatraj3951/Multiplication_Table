import pyfiglet

text = pyfiglet.figlet_format("  Multiplication ")
text1 = pyfiglet.figlet_format("      Table     ")
print (text)
print (text1)
print ("      Program by Shashwat__Raj ")
print (" ")
# Multiplication table of any given number in Python

num = float (input("Enter a number :- "))
length = int (input("Enter a length :- "))

for i in range(1, length + 1):
 # print table of given number
   print(num, 'x', i, '=', num*i)

input()

