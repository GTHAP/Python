# Call by reference in python
a = 10
b = a # variable 'b' points to the memory location of the variable 'a'
print(a, hex(id(a)), b, hex(id(b)))
a = 20 # When the value for 'a' changes the value for the variable 'b' remains the same
print(a, hex(id(a)), b, hex(id(b)))
b = a
print(a, hex(id(a)), b, hex(id(b)))
b = 10
print(a, hex(id(a)), b, hex(id(b)))
