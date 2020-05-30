#math
# x =2.9
# print(round(x))
# print(abs(-2.9))

#import
# import math
# print(math.ceil(2.9))#取整
# print(math.floor(2.9))

#if elif else
# is_hot =False
# is_cold = True

# if is_hot:
#     print("It's a hot day")#shift+tab，取消缩紧
# elif is_cold:#else if
#     print("It's a cold day")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# price = 100000
# has_goof_credit = True

# if has_goof_credit:
#     down_payment = 0.1*price
# else:
#     down_payment = 0.2*price
# print(f"Down payment:${down_payment}")#动态的插入值

#logical operators
# has_high_income = True
# has_good_credit = True
# has_criminal_record = False#犯罪记录

# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# elif has_high_income or has_good_credit:
#     print("Eligible for loan")
# elif has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# #compare operators
# temperature = 30
# if temperature >= 30:#== <= !=
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = "J"
# name = input("please input your name:")
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) >50:
#     print("Name must be a maximun of 50 characters.")
# else:
#     print("Name looks good.")

# weight = input('Your weight: ')
# unit = input('(L)bs or K(g): ')
# if unit.upper() == "L":#unit=="L" or unit=="l":
#     weight_kg = int(weight) * 0.45
#     print(f"You are {weight_kg} kilos")
# elif unit.upper() == "K":#unit=="k"or unit=="K":
#     weight_lb = int(weight) / 0.45  #a//b得到一个整数
#     print(f"You are {weight_lb} pounds")


# #while
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1 
# print("Done")

#Guess game
# secret_number = 9
# guess_count = 0  #变量同时替换：右键+重命名符号
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else: #while if not meet the condition,we will carry out else 
#     print('Sorry, you failed')


