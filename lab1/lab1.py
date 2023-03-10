# number 1

# def names(name):
#     return f'hallo {name}'

# txt = names("ali")
# print(txt)


# /////////////////////////////////////////////////////////////
# number two

# def calc():
#     num1 = float(input('Enter first number: '))
#     num2 = float(input('Enter second number: '))
#     add = num1 + num2
#     mul = num1 * num2
#     sub = num1 - num2
#     div = num1 / num2
#     return f'multiplication equal:{mul} , subbtraction equal:{sub} , division equal:{div} , add equal:{add}'

# print(calc())

# /////////////////////////////////////////////////////////////
# number three
# def large():
#     li=[]
#     num=int(input('enter number of elements list'))
#     for i in range(num):
#         li.append(int(input("enter element {}".format(i+1))))
#     result = max(li)
#     return f'your biggest number is {result}'
# print(large())

# /////////////////////////////////////////////////////////////
# number four

# def age():
    
#     num1 = int(input('Enter your age: '))
    
#     if num1 >= 18:
#        return "your are able to vote"
#     else:
#        return "you can not vote"

# print(age())



# /////////////////////////////////////////////////////////////
# number five

# def large():
#     li=["ahmed","mostafa","ali","safsCCAECV"]
#     result = max(li)
#     return f'your biggest element is {result}'
# print(large())


# /////////////////////////////////////////////////////////////
# number six

# def comp():
    
#     num1 = int(input('Enter your number: '))
#     if num1==0:
#         return "you entered 0 number"
#     elif num1 %2==0:
#        return "your number is even"
#     else:
#        return "your number is odd"

# print(comp())



# /////////////////////////////////////////////////////////////
# number seven

# def countnum():
    
#     s = str(input('Enter your string: '))
#     vowels = 0
#     for i in s:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
#     return f'your vowels counts is {vowels}'

# print(countnum())


# /////////////////////////////////////////////////////////////
# number eight

# def upper():
    
#     s = str(input('Enter your string: '))
#     x = s.upper()
#     return x

# print(upper())


# /////////////////////////////////////////////////////////////
# number nine

# def large():
#     li=[]
#     li2=[]
#     num=int(input('enter number of elements list'))
#     for i in range(num):
#         num2= int(input("enter element {}".format(i+1)))
#         li.append(num2)
#         if num2 %2==0:
#             li2.append(num2)
    
#     return li2
# print(large())


# /////////////////////////////////////////////////////////////
# number ten

def sorting():
    s=[]
    s2=[]
    num=int(input('enter number of elements list'))
    for i in range(num):
        str2= str(input("enter element {}".format(i+1)))
        s.append(str2)
        for x in s:
            str3= x.lower()
            s2.append(str3)
            s2.sort()
    return s2

print(sorting())