'''
0 - - - - - - 0 
0 1 - - - - 1 0 
0 1 2 - - 2 1 0 
0 1 2 3 3 2 1 0
'''

#replace 4 with dynamic input
count = 2*(4-1)
for i in range(4):

    for j in range(i+1):
        print(j, end=" ")
    
    for j in range(count):
        print("-", end=" ")

    for j in range(i,-1,-1):
        print(j, end=" ")

    count -=2

    print()  
