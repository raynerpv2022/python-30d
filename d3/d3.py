print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# ex
    # base = int(input("Enter base: "))
    # height = int(input("Enter Height: "))
    # area = base*height*0.5
    # print("Base:",base, "Height: ", height,"Area: ", area)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = "python"
dragon = "dragon"
print("python > dragon", len(python) > len(dragon))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Is on in python and dragon :", "on" in python and "on" in dragon)
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("is jargon in the sentence? : ","jargon" in "I hope this course is not full of jargon")
len_python = str(float(len(python)))
print(len_python,type(len_python))

# even number
    # even = int(input("Even Number")) % 2
    # print(even)

print(7 // 3 == int(2.3) )

print(type("10") == type(10))

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    # age = int(input("Age lived: "))
    # print(age*365*24*60*60)
number = 1
pow = 0
n = 0
p = 0
 
print( (number+n),(number+n)**pow,(number+n)**(pow+1),(number+n)**(pow+2),(number+n)**(pow+3))
n += 1
print( (number+n),(number+n)**pow,(number+n)**(pow+1),(number+n)**(pow+2),(number+n)**(pow+3))
n+=1
print( (number+n),(number+n)**pow,(number+n)**(pow+1),(number+n)**(pow+2),(number+n)**(pow+3))
n+=1
print( (number+n),(number+n)**pow,(number+n)**(pow+1),(number+n)**(pow+2),(number+n)**(pow+3))
n+=1
print( (number+n),(number+n)**pow,(number+n)**(pow+1),(number+n)**(pow+2),(number+n)**(pow+3))
