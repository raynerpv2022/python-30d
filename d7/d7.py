it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("twitter")
print(it_companies)
it_companies.update(["aaaa","bbbbb"])
print(it_companies)
delete = it_companies.pop()
print(delete)

it_companies.discard("hdjskhk")
# it_companies.remove("aaaads")
# A.update(B)
print(A)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.update(B)
B.update(A)
print(A,B)
A.update([9090])
print(A.symmetric_difference(B))
ageSet = set(age)
print(ageSet)
print(len(age) > len(ageSet))

text = "I am a teacher and I love to inspire and teach people"
 
a = text.split()
print(a)
text2 = set(a)
print(len(text2 ), text2)

 