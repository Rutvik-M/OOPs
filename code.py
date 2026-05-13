#reverse String 
str="hello"
print (str[::-1])
chars = list(str)

def reverse(chars):
    left=0
    right=len(chars)-1
    while left< right:
        chars[left],chars[right]=chars[right],chars[left]
        left+=1
        right-=1
    return "".join(chars)
  

r=reverse(chars)
print (r)
