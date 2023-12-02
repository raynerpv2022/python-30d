list1 = []
list2 = [1,2,3,4,5]
print(len(list1), len(list2))
# Get the first item, the middle item and the last item of the list
print(list2[0],list2[len(list2)//2],list2[-1])
mix = ["resbaloso", 12, "married,", True]
print(mix)
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies, len(it_companies))
print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])
it_companies.append("Segurmatica")
it_companies.insert(len(it_companies)//2,"SIS")
it_companies[0]= it_companies[0].upper()
print(it_companies)
it_companies1 = "#;".join(it_companies)
print(it_companies1)
print("SIS is in ? :", "SIS" in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3], it_companies[-3:])
it_companies.pop(0)
it_companies.clear()
 
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end+back_end

full_stack.insert(full_stack.index("Redux")+1,["Python", "SQL"])

print(full_stack)

# ex level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages ,"MAx : ", ages[-1], "Min : ", ages[0])
ages.append(ages[-1])
ages.append(ages[0])
ages.sort()
print("Median :", (ages[len(ages)//2]+ages[len(ages)//2]+1)//2)
print(ages)
print("Average :", sum(ages)/len(ages ))
print("Range :", max(ages)-min(ages))
q,w,e,*list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(list)

