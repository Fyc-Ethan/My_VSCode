#list
# names = ['John','Bob','Mosh','Sarah']
# names[1] = 'Bo'
# print(names[2:])

# numbers = [1,2,3,41,2,3,4]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

#2D list
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
# print(matrix[0][2])
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5,2,1,7,4]
# numbers.append(13)  #add
# numbers.insert(3,10)#插入
# numbers.remove(5)
# numbers.clear()
# numbers.pop() #delect last number in list

# print(5 in numbers) #
# numbers.sort()
# numbers.reverse()#反向排序
# numbers2 = numbers.copy()

# numbers = [2,2,3,1,4,5,2]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques) 

# tuple 元组,not change
# numbers = (1,2,0)
# numbers[0]


# coordinates = (1,2,3)
# x = coordinates[0]  
# y = coordinates[1]
# z = coordinates[2]

# x,y,z = coordinates #equal 49-51

#字典 键值是唯一的
# customer = {
#     "name": "John Smith",
#     "age":30,
#     "is_verified":True
# }
# customer["name"] = "Jace Smith" #update
# customer["birthdate"] = "Jan 1 1980" #add
# print(customer["name"])
# print(customer.get("name"))
# print(customer.get("N"))    #输入一个不存在的键，不用报错
# print(customer.get("N","Jan 1 1980")) #输入键值,则可以直接输出键值

number = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output = ""
phone = input("phone: ")
for ch in phone:
    #a = number[n]
    output += number.get(ch,"!") + " " #input 5 and the output will write text is !
print(output)