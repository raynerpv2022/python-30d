# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
ss = ['Thirty', 'Days', 'Of', 'Python']
s = " ".join(ss)
print(s)
print(len(s))
upper = s.upper()
print(upper)
lower = upper.lower()
print(lower)
cap = s.capitalize()
title = s.title()
sw = title.swapcase()
print(cap,"\n",title,"\n",sw)
# Cut(slice) out the first word of Coding For All string.
s = "Coding For All"
print(s[:s.index(" ")])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("is coding? INDEX",s.index("Coding"))
print("is coding? FIND",s.find("Coding"))
print(s.replace("All","python"))
print(s.split())
a = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(a.split(","))
print(a[-1])
s = "Python For All"
aa = s.split()
aaa = aa[0][0]+aa[1][0]+aa[2][0]
print(aaa)

because = 'You cannot end a sentence with because because because is a conjunction'
result = because[because.index("because"):because.rindex("because")+len("because")]
print(result)

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

d = '   Coding For All      '
print("/"+d.strip()+"/")

f = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" #".join(f))

print(f'{"radius"} = {10}' )
print(f'{"area"} = {3.14} * {"radius"}**{2}')