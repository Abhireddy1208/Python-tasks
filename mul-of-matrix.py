l1=[1,2],[3,4]
l2=[4,3],[2,1]
result=[0,0],[0,0]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        for k in range(len(l2)):
            result[i][j]+= l1[i][k]*l2[k][j]
print(result)
