#reverse String 
# str="hello"
# print (str[::-1])
# chars = list(str)

# def reverse(chars):
#     left=0
#     right=len(chars)-1
#     while left< right:
#         chars[left],chars[right]=chars[right],chars[left]
#         left+=1
#         right-=1
#     return "".join(chars)
  
# r=reverse(chars)
# print (r)

## Palindrome 
# char = "madama"
# print (char[::-1])

# strs=list(char)

# def palindrome(char):
#     left=0
#     right=len(strs)-1
#     while left<right:
#         if strs[left] != strs[right]:
#             return ("false")
#         left+=1
#         right-=1
#         return ("true")
# s1=palindrome(strs)
# print(s1)

# char = "madam"
# text = list(char)
# def pal(text):
#     return text == text[::-1]

# pal=pal("madama")
# print(pal)


## prime nUmber
# n = 10
# for i in range(2,n):
#     if n%i==0:
#         print("False")
#         break
#     else:
#         print("True") 

## factorial 5*4*3*2*1
# num = 0
# def factorial(num):
#     fact=1
#     if num<=0:
#         return "not defined"

    
#     for i in range(1,num+1):
#         fact=fact*i 
#     return fact 
# f1=factorial(num)
# print(f1)

## fibonanci num=7

# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fibo(5)
