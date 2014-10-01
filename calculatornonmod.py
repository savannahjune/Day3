def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return float(num1) / float(num2)

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def calculator(opersign, num1, num2): # defines function calculator with three args
    if opersign == '+':  # if opersign is plus, calls add function on num1 and num2
        print add(num1, num2) # prints result of add function
    elif opersign == '-': # if opersign is subtract, calls subtract function on num1 and num2
        print subtract(num1, num2)
    elif opersign == '*':
        print multiply(num1, num2)
    elif opersign == '/':
        print divide(num1, num2)  
    elif opersign == 'square':
        print square(num1)
    elif opersign == 'cube':
        print cube(num1)
    elif opersign == 'pow':
        print power(num1, num2)
    elif opersign == 'mod':
        print mod(num1, num2) 
    else:
        opersign = 'q'    
        print "Bye!"

# ask user for input
oper = ''
x = 0
y = 0

while oper != 'q':
    entry = raw_input()  # ask user for input
    entrylist = entry.split(" ") # takes that input and makes it a list
    oper = entrylist[0] # defines oper as first item in list
    x = int(entrylist[1]) # defines x as second item in list and makes it an integer
    y = int(entrylist[2]) # defines y as third item in list and makes it an integer
    print calculator(oper, x, y) # calls function with oper, x, and y as arguments