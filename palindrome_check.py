"""Check whether it is palidrome or not using Recursion"""

def check_palindrome(string,left,right):
    if left >= right:
        return True
    
    if string[left] != string[right]:
        return False
    
    return check_palindrome(string,left+1,right-1)


# a = check_palindrome("nitin",0,4)

# print(a)

def palindrome(string):
    string = string.lower()
    return check_palindrome(string,0,len(string)-1)
    

a = palindrome("NITIn")
print(a)

'''Due Ammount : 7701
Start Date : 26 Aug 2025 
1 out of 18 Emis paid
Recommended payment date : 27/10/2025
mpr : 35'''