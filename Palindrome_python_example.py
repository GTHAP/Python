# Checking if word is a palindrome is relatively simple but a good way to understand basics of coding in python
# I thought I would add it here in order to understand how while loops, conditional statements work in python

def ispalindrome(stringtocheck):
    start = 0
    end = len(stringtocheck) - 1
    while start < end:
        if stringtocheck[start] == stringtocheck[end]:
            start += 1
            end -= 1
        elif stringtocheck[start] != stringtocheck[end]:
            return print(False)    
    return print(True)
                                 
string = "anana"
ispalindrome(string)
