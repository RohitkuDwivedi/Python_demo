# sum of all numbers

numbers = input('Enter space separated Numbers: ')
numbers = numbers.split()

# def sum_of_num(input_data):
#     sum_of_all = 0
#     num = len(input_data) #3
#     index = 0
#     while(index<num):
#         sum_of_all = sum_of_all + int(input_data[index])
#         index+=1   # index = index + 1
#     # length of list
#     # take 1 num at a time and & add it to
#     # and keep adding till we reach ponit 1
#     return sum_of_all

# print(f'Sum of {numbers} = {sum_of_num(numbers)}')


# for i in iterable:
#     # do something with i 
#     pass

# output_sum = 0
# for val in numbers:
#     output_sum+= int(val)

# print(f'Sum of {numbers} = {output_sum}')


## ________ output of only even numbers skip number 10 and break if number is 0 ____________##

# 1 2 3 4 5 10 22 33 4 0 33 4



even_sum = 0
import pdb;pdb.set_trace()
for i in numbers: # [1 2 10 3 0 5]
    i = int(i)
    if i==10:
        continue
    if i==0:
        break
    if i%2==0:
        even_sum = even_sum + int(i)
    

print(f'Sum of {numbers} = {even_sum}')


range(1,11)
print("SUM USING LIST COMPREHENSION: ", sum([int(i) for i in numbers]))





