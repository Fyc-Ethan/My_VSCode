#for
#python definition list uses []
# for item in 'Pyhon':
#     print(item)
# for item in ['Mosh','John','Sarch']:
#     print(item)
# for item in range(5,10,2):  #range create the range of number,the third argument is step
#     print(item)
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total : {total}")
#array or cooedinate
# for x in range(4):
#     for y in range(3):  #new loop ,countinue,until loop end,and go by last x,and go on  
#         print(f'({x},{y})')
numbers = [5,2,5,2,2]
x=len(numbers)
for i in range(x):
    for y in range(numbers[i]):
        print('*',end='')
    print()

#Teacher's solution
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += '*'
    print(output)

