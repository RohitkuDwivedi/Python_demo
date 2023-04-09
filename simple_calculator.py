# imports:
# import pdb;pdb.set_trace()
# input from user
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
# calcualte
sign = input('operaion: [+ - / *]: ')

def calculator(input1, input2, operation):
    if operation == '+': 
        output = input1 + input2

    elif operation == '-': 
        output = input1 - input2

    elif operation == '/': 
        output = input1 / input2

    elif operation == '*': 
        output = input1 * input2
    return output

# output = calculator(num1, num2, sign)
output = calculator(input1=num1, operation=sign, input2=num2)


print(f'{num1} {sign} {num2} = {output}')

''
""
""" """


#return result


# 1. if else & elif
# 2. function definiton
# 3. formatt string
# 4. for and while 
# *** list comprehension
