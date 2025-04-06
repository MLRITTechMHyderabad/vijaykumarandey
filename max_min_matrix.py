matrix = [[1,2,3],[4,5,6]]
list = []
for i in range(len(matrix)):
    list += [max(matrix[i])]
print("maximum element is",max(list))    
for i in range(len(matrix)):
    list += [min(matrix[i])]
print("minimum element is",min(list))    


