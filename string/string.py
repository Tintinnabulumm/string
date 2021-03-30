#改变大小写
name = 'ada lovelive'
print(name.title())
print(name.upper())
print(name.lower())

#添加制表符，换行符
print('\tpython')
print('\npython')

#删除空白
favourite_language = ' python '
print(favourite_language.rstrip()) #删除末尾的空白
print(favourite_language.lstrip()) #删除开头的空白
print(favourite_language.strip()) #删除两头的空白

#将数字变成字符串
age = 23
print('your age is '+ str(age))
