#类型转换
# birth_year = input('Birth year：')
# print(type(birth_year))
# age = 2020 - int(birth_year)#要将字符串转为int类型
# print(type(age))
# age=str(age)#type打印类型
# print('Your age is :'+age)#py输出只能是字符串+字符串

# #联系
# weight_lbs = input('Your weight(lbs):')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

#ctrl+K ctrl+c 多行注释，ctrl+K ctrl+U 取消注释 

#字符串
# course = "Python's Course for Beginners"
# course = 'Python Course for "Beginners"'
# course = '''
# hi John,
# ThanK you,'''
# #多行字符串
# course = 'Python for Beginners'
# print(course[0])
# print(course[-1])#指定字符的输出
# print(course[0:3])#返回索引0-3
# print(course[1:])
# print(course[:5])#默认以0开始
# another = course[:]
# print(another)
# print(course[1:-1])

# first = 'John'
# last = 'Smith'
# message = first + '[' + last + '] is a coder'
# msg = f'{first}[{last}] is a coder'#在字符串前面加入f+再加入{}，就可以在字符串中动态的插入值
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(len(course))#len字符串长度
# course.upper()#behind of the . we often call this function is a method, the method belong to a special object
# print(course.upper())#Upper case //lower
# print(course.lower())
# print(course.find('P'))#return the find the index of the first character(str) of the text
# print(course.replace('Begin','Absoulte Begin'))#replace the character of the text
# print('Python' in course)#judge if this character exsit in this text ture or false and return the boolean type
# #in
# print(course.title())


#arithmetic operation
print(10 // 3) #get a integer number/result
print(10 ** 3 )#power 次方？
#增广赋值运算符号 augmented assignment operation symbol
#Operator percedence 操作优先符
x = 3
x += 3
#parenthesis --()
#exponentiation 2**3
#  multiplication or division
#addition or subtraction

k = 1000
while k>1:
    print(k)
    k = k/2 





