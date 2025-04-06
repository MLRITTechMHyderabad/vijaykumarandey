# tuple = list(map(int, input().split()))
# students = {}
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]
dict = dict(students)
print(dict)
a = []
b = 0
name = ""
passed = 0
for key,values in dict.items():
    grades = sum(values)/(len(values))
    a += [grades]
    if b < grades:
        b = grades
        name = key
    if grades >= 50:
        passed += 1

print(name)
print(max(a))
print(passed)


  

    

