import random
d = []
for i in range(1,7):
    for j in range(1,7):
        d.append([i,j])
print(d)    
dic= {}    
for i in range(2,13):
    c = 0
    for j in d:
        if i == j[0]+j[1]:
            c += 1
    dic[str(i)] = c/len(d)
print(dic)    
# input1 = int(input())
# input1 = [[1,1],[3,4]]
# input2 = [1,5]

# for i in range(input1):
#     a,b,c,d = map(int,input().split())
    

# for key,value in dic.items():
#     if str(sum(input1)) == key:
#         p1 = value
# for key,value in dic.items():
#     # print(key,value)
#     if str(sum(input2)) == key:
#         p2 = value
#         print(p2)
# if p1 < p2:
#     print("player 1 win")         
# else:
#     # print("player2 is wins")
    




