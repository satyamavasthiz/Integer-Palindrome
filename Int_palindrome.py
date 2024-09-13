# "PANLINDROME"

# Using Mathematics logic:

def palindrome(n):
    
    if n<0:
        return False
    origional = n
    reverse = 0
    while n>0:
        last_digit = n%10
        reverse = reverse*10 + last_digit
        n = n//10
        
    return origional == reverse
number = eval(input("Enter minimum two digit Number (Using Mathematics logic): "))
if palindrome(number):
    print(f"{number} is palindrome")
    
else:
    print(f"{number} is not palindrome")
    
    
# Using Reversed Function:    
    
n = int(input("Enter minimum Two Digit Number (Using Reversed Function): "))
s = str(n)
reverse = ''.join(reversed(s))
if s == reverse:
    print(f"{n} is palindrome")
    
else:
    print(f"{n} is not palindrome")
    
# Using Slicing:   

n = input("Enter minimum Two Digit Number (Using Slicing): ")

reverse = s[::-1]
if s == reverse:
    print(f"{n} is palindrome")
    
else:
    print(f"{n} is not palindrome")
    
    
    
    
   
