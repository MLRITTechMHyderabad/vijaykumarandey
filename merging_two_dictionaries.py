x = {"a":3,"b":2}
y = {"a":2,"b":4}
merged = {}
def merging_dictionaries(x,y):
    for key in x:
        merged[key] = x[key]
    for key in y:
        merged[key] = y[key]
    return merged   
print(merging_dictionaries(x,y))

 