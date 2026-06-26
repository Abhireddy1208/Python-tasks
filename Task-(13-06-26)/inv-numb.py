#  7. Inverted Number Triangle 
#  1 2 3 4 5 
#  1 2 3 4
#  1 2 3
#  1 2
#  1
n=5

for i in range(n-1,-1,-1):
    val=1
    for j in range(i+1):
        print(val, end=" ")
        val+=1
    print()
