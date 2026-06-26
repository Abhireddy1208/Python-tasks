#  5. Alphabet Triangle
#  A 
#  A B
#  A B C
#  A B C D
#  A B C D E 

n=5
for i in range(n):
    val=65
    for j in range(i+1):
        print(chr(val), end=" ")
        val=val+1
    print()