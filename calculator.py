def add(nums):
    print nums
    total = 0
    for i in nums:
        total = total + int(i)

    return total

def subtract(nums):
    print nums
    total = int(nums[0])
    for i in nums[1:]:
        total = total - int(i)
    return total

def multiply(nums):
    print nums
    total = int(nums[0])
    for i in nums[1:]:
        total = total * int(i)
    return total

def divide(*nums):
    num1, num2 = nums
    return float(num1) / float(num2)

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def calculator(opersign, nums):

    if opersign == '+':
        return add(nums)
    elif opersign == '-':
        return subtract(nums)
    elif opersign == '*':
        return multiply(nums)
    elif opersign == '/':
        return divide(nums)  
    elif opersign == 'square':
        return square(nums)
    elif opersign == 'cube':
        return cube(nums)
    elif opersign == 'pow':
        return power(nums)
    elif opersign == 'mod':
        return mod(nums) 
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

        print calculator(oper, entrylist[1:])
