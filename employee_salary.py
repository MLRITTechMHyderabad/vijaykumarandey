employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]


# employee_salary(employees)        
# list_1 = [1,2,3,4]
# res = map(lambda x:x*x,list_1)
# print(list(res))
# res = map(lambda x:list(x),employees)
# print(list(res))
a = []
for i in employees:
    a.extend(list(i.items()))
print(a)    