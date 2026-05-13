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
char = "madama"
print (char[::-1])

strs=list(char)

def palindrome(char):
    left=0
    right=len(strs)-1
    while left<right:
        if strs[left] != strs[right]:
            return ("false")
        left+=1
        right-=1
        return ("true")
s1=palindrome(strs)
print(s1)
        