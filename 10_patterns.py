'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

for i in range( 5*2):

    start = i 
    if i > 5:
        start = 2*5 - i 
    for j in range(start):
        print("*", end=" ")
    print()
