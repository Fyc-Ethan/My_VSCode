# message = input(">")
# words = message.split(' ')#spilt分割输入的词语，返回这些word对应的数组形式
# #print(words)
# emojis = {
#     ":)": "smile",
#     ":(": "sad" 
# }
# output =""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

#funtion
#parameter
# def greet_user(first_name,last_name):#funtion 之后要空两行 
#     print(f'Hi {first_name} {last_name}! ')
#     print("Hi guys!")


# print("Start")
# greet_user("John","Smith")
# greet_user(last_name="Mary",first_name="Smith")#you can set keyword parameter,import code readablely
# print("Finsh")

# def square(number):
#     return number*number


# name =int(input("input number: "))
# result = square(name)
# print(result)
# print(square(name))


#change the fist code
# def emoji_converter(messge):
#     words = message.split(' ')#spilt分割输入的词语，返回这些word对应的数组形式
#     #print(words)
#     emojis = {
#         ":)": "smile",
#         ":(": "sad" 
#     }
#     output =""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input("> ")
# output = emoji_converter(message)
# print(output)

#************except error test 错误调试 try block - handle them*****************************
#类型错误和值错误，就会运行except的输出，一个exception，程序不会保错
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0') #数字运算类型错误
except ValueError:
    print('Invalid valur')

#注释
    
