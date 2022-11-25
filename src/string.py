
print("###문자열")

str = 'test'
print(str)

str = "test's"
print(str)

str = "'test\"s'\nnext line"
print(str)

# 3
print(str.count('t'))

str = """test'"
next line"""
print(str)

# \ 문자로 첫번째 열은 줄바꿈 안됨 
str = """\
Usage: test
    -h
    -r
"""
print(str)

str = "1234567890"

print(str[0])
print(str[:3])
print(str[1:3])
print(str[3:])
print(str[-3:])
# IndexError: string index out of range
#print(str[11])
# slice는 범위를 벗어나도 에러 안남
print(str[:100])
print(len(str))

str = "Hello World!"
print(str.lower())
print(str.upper())
print(str.startswith("He"))
print(str.endswith("!"))
print(str.find('lo'))

str = "Hello {0}"
print(str.format('Monkey!'))

# True
print("123","123".isdecimal()) 
# True
print("123","123".isnumeric()) 
# True
print("123","123".isdigit())
# False
print("123","123".isalpha())
# True
print("123","123".isalnum())
# True
print("123","123".isascii())

# 1,2,3,4,5,6
print(",".join('123456'))
# 12X456
print("123456".replace('3','X'))
# ['1', '2', '3', '4', '5', '6']
print("1,2,3,4,5,6".split(','))
