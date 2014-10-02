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
        print add(num1, num2)
    elif opersign == '-':
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
entry = []
#entry = raw_input()

#entrylist = entry.split(" ")
oper = ''
x = 0
y = 0 




#print entrylist
#print oper
#print type(x)
while True:
    if oper == 'q':
        break
    else:
        entry = raw_input()
        entrylist = entry.split(" ")
        oper = entrylist[0]
        x = int(entrylist[1])
        y = int(entrylist[2])
        print calculator(oper, x, y)