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
    
# fibo(7)

# count freq 
# strs = "hello"
# freq={}
# for i in strs:
#     freq[i]=freq.get(i,0)+1
# print(freq)

# remove duplicates
# n = [1,1,2,1,4,2]
# print(list(set(n)))

# def remove(n):
#     hashmap=set()
#     seen=[]
#     for i in n:
#         if i not in hashmap:
#             hashmap.add(i)
#             seen.append(i)
#     return seen 
# remove("hiello") 

#Largest element

# nums=[100,2,4,5,7,8,9,9,10145]
# def largest(nums):
#     largest = float("-inf")
#     for i in nums:
#         if i>largest:
#             largest=i 
#     return largest 
# print(largest(nums))

## second largest 
# nums=[10,20,50,10,70,60]
# def second_largest(nums):
#     largest = float("-inf")
#     sec_largest = float("-inf")
#     for num in nums:
#         if num>largest:
#             sec_largest=largest 
#             largest=num 
#         elif num>sec_largest and num!= largest:
#             sec_largest=num
#     return sec_largest 
# print(second_largest(nums)) 

##sorting list
# nums=[10,5,0,1,7,9,8]
# nums.sort(reverse=True)
# print(nums)

# def sorting(nums):
#     s1=[]

## frequency count 
# nums=[1,2,1,2,4,5,8,5,2,0,1,2,1]
# def frequency(nums):
#     freq={}
#     for i in nums:
#         freq[i]=freq.get(i,0)+1
#     return freq 
# print(frequency(nums))

## list comprehension 
# nums=[]
# for i in range(5):
#     nums.append(i)
# print(nums)

# nums=[i for i in range(5)]