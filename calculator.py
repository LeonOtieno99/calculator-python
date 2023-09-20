import sys
import os

print('************************')
print('***    calculator    ***')
print('************************')

#math operations
def calculate(operator, a,b):
    result = None
    a = float(a)
    b = float(b)
    match operator:
        case 1:
            result = a + b
        case 2:
            result = a - b
        case 3:
            result = a * b
        case 4:
            if b == 0:
                print('Math Error: can\'t divide by zero!!!')
                os.system('cls' if os.name == 'nt' else 'clear')
                first_page()
            else:
                result = a / b
        case _:
            result = None
    return result

#opening page
def first_page():
    print('\nWhat operation would you like to perform?')
    print('1.Addition')
    print('2.Substraction')
    print('3.Multiplication')
    print('4.Division')

    operator = int(input('\nSelect_(use values):\n'))
    value1 = int(input('Enter your first value?\n'))
    value2 = int(input('Enter your second value?\n'))

    result = calculate(operator, value1, value2)
    print(f'The answer is {result}\n')

#loop
def choices(choice):
    match choice:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            first_page()
        case 2:
            sys.exit()

#first call
first_page()

print('Ready for next operation')
print('1.continue')
print('2.quit\n')
choice = int(input('Select_(use values):\n'))
#second call
choices(choice)


