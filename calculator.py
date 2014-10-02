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

def calculator(opersign, num1, num2):
    if opersign == '+':
        return add(num1, num2)
    elif opersign == '-':
        return subtract(num1, num2)
    elif opersign == '*':
        return multiply(num1, num2)
    elif opersign == '/':
        return divide(num1, num2)  
    elif opersign == 'square':
        return square(num1)
    elif opersign == 'cube':
        return cube(num1)
    elif opersign == 'pow':
        return power(num1, num2)
    elif opersign == 'mod':
        return mod(num1, num2) 
    else:    
        return "That's not an operator."

oper = ''
x = 0
y = 0 

while True:
    entrylist = raw_input()

    if entrylist[0] == 'q':
        print "Bye!"
        break
    else:

        entrylist = entrylist.split(" ")
        oper = entrylist[0]
        x = int(entrylist[1])
        y = int(entrylist[2])
        print calculator(oper, x, y)
