# Q1.answer

# import math
# r = 2.5
# area = math.pi * r * r
# print("area of circle is:%.2f" %area)

# --------------------------------------------------
# Q2.answer

# from modules import rev_string
# print(rev_string("hello,world"))


# --------------------------------------------------
# Q3.answer

# import random

# x = random.randint(1,10)
# print(x)
# my_list=[]

# --------------------------------------------------
# Q4.answer

# from datetime import datetime as dt
# x = dt.now()
# print(x)

# --------------------------------------------------
# Q5.answer

# with open(r"F:/python/python-lab/lab2/example.txt",'r') as file:
#     count = len(file.readlines())
#     print(count)
#     file.close()


# --------------------------------------------------
# Q6.answer
# with open(r"F:/python/python-lab/lab2/example.txt",'r') as file:
#     rev_file = file.read()
#     li=[]
#     for i in rev_file:
#         li.append(i)
#     print(li)
#     li.reverse()
#     print(li)
#     s1=' '
#     x = s1.join(li)
#     print(x)
#     file.close()


# --------------------------------------------------
# Q7.answer

# with open(r"F:/python/python-lab/lab2/example.txt",'r') as file:
#     rev_file = file.read()
#     li=[]
#     for i in rev_file:
#         li.append(i.strip())
#     print(li)
#     s1=' '
#     x = s1.join(li)
#     print(x)
#     with open(r"F:/python/python-lab/lab2/example.txt",'w') as file2:
        
#         file2.write(x)
#     file.close()


# --------------------------------------------------
# Q8.answer

# with open(r"F:/python/python-lab/lab2/example.txt",'r') as file, open("F:/python/python-lab/lab2/copy.txt",'w') as file2:
#     old_file = file.read()
#     for l in old_file:
#         new_file = file2.write(l)
#     file.close()
#     file2.close()


# --------------------------------------------------
# Q9.answer
# ================================================================================
with open(r"F:/python/python-lab/lab2/example.txt",'r') as file:
    fileContent1 = file.read().split()
    longestWord = max(fileContent1, key=len)
    print(longestWord)

    file.close()
# ================================================================================

# --------------------------------------------------
# Q10.answer
# def int_func(li):
#     sum=0
#     for i in li:
#         if i%2==0:
#             sum+=i
#     return sum

# print(int_func([1,2,3,4,5,6,7]))

# --------------------------------------------------
# Q11.answer
# ========================================================
# def string_func(li):
#     word='a'
#     for i in li:
#         if i[0].lower() == word:
#             print(str(i))

# print(string_func(['ahmed','mostafa','ali']))
# ================================================================
# --------------------------------------------------
# Q12.answer

# def dict_func(d):
#     swaping = {v: k for k,v in d.items()}
#     print(swaping)
 

# print(dict_func({1:'ahmed',2:'mostafa',3:'ali'}))


# --------------------------------------------------
# Q13.answer

# def int_func(li):
#     l=0
#     s=0
#     for i in li:
#         if i>=l:
#             l=i
#         elif i<=s:
#             s=i
#     print("the largest number is: %d "%l)
#     print("the smallest number is: %d "%s)
# print(int_func([0,1,2,3,4,5,6,7]))


# --------------------------------------------------
# Q14.answer

# import math
# def int_func(li):
#     sqr=[]
#     x=0
#     for i in li:
#        x= pow(i,2)
#        print(x)
#        sqr.append(x)
#     return sqr
# print(int_func([0,1,2,3,4,5,6,7]))

# --------------------------------------------------
# Q15.answer

# def int_func(*args):
#     new=[]
#     for i in args:
#        new+=i
#     return new
# print(int_func([0,1,2,3,4,5,6,7] , [5,8,9], [12,20,31]))


# --------------------------------------------------
# Q16.answer

# def string_func(**kwargs):
    
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
#     for k in kwargs.keys():
#          print(f"{k}")
#     for v in kwargs.values():
#         print(f"{v}")
    

# string_func(first='mostafa', mid='mohamed', last='salama')



