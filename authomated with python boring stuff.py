passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
print('Access granted')
 if typedPassword == '12345':
 print('That password is one that an idiot puts on their luggage.')
else:
 print('Access denied')

 print('Hello world!')

  spam = 40
>>> spam
40
>>> eggs = 2
v >>> spam + eggs
42
>>> spam + eggs + spam
82
w >>> spam = spam + 2
>>> spam
42
>>> spam = 'Hello'
>>> spam
'Hello'
>>> spam = 'Goodbye'
>>> spam
'Goodbye'

# This program says hello and asks for my name.
 print('Hello world!')
print('What is your name?') # ask for their name
 myName = input()
 print('It is good to meet you, ' + myName)
 print('The length of your name is:')
print(len(myName))22 Chapter 1
 print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.'

 Hello world!
What is your name?
Al
It is good to meet you, Al
The length of your name is:
2
What is your age?
4
You will be 5 in a year.

Comments
The following line is called a comment. 
 # This program says hello and asks for my name.

print('The length of your name is:')
print(len(myName))
Enter the following into the interactive shell to try this:
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.')
46 
>>> len('')
0
#Just like those examples, len(myName) evaluates to an integer. It is then 
#passed to print() to be displayed on the screen. Notice that print() allows 
#you to pass it either integer values or string values. But notice the error that 
#shows up when you type the following into the interactive shell:
 >>> print('I am ' + 29 + ' years old.')
Traceback (most recent call last):
 File "<pyshell#6>", line 1, in <module>
 print('I am ' + 29 + ' years old.')
TypeError: Can't convert 'int' object to str implicitly
#The print() function isn’t causing that error, but rather it's expression you tried to pass to print(). You get the same error message if you type 
#the expression into the interactive shell on its own.

 #str(), int(), and float() Functions
#If you want to concatenate an integer such as 29 with a string to pass to 
#print(), you’ll need to get the value '29', which is the string form of 29. The 
#str() function can be passed an integer value and will evaluate to a string 
#value version of it, as follows:
>>> str(29)
'29'
>>> print('I am ' + str(29) + ' years old.')
I am 29 years old.
#Because str(29) evaluates to '29', the expression 'I am ' + str(29) + 
#' years old.' evaluates to 'I am ' + '29' + ' years old.', which in turn 
evaluates to 'I am 29 years old.'. This is the value that is passed to the 
print() function.
#The str(), int(), and float() functions will evaluate to the string, integer, and floating-point forms of the value you pass, respectively. Try converting some values in the interactive shell with these functions, and watch 
#what happens.
>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> int('42')
42
>>> int('-99')
-99
>>> int(1.25)
1
>>> int(1.99)
1
>>> float('3.14')
3.14
>>> float(10)
10.0

      
