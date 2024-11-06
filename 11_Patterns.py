'''
1 
0 1 
1 0 1 
0 1 0 1 
'''
#replace 5 with dynamic input

for i in range(5):
    if i % 2==0:
        start = 0
    else:
        start = 1
    
    for j in range(i):
        print(start, end=" ")
        start = 1 - start 
    print()
