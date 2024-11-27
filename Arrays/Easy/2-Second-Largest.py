class Solution:
    #2pass solution - Time - 2n
    def getSecondLargest(self, arr):
        # Code Here
    
        largest = arr[0]
    
        for i in range(1,len(arr)):
            
            if arr[i] > largest:
                largest = arr[i]
        
        secondLargest = -1
        
        for i in range(len(arr)):
            if arr[i] > secondLargest and arr[i] != largest:
                secondLargest = arr[i]
        
        return secondLargest

# 1pass solution Time - n
def getSecondLargestTwo(self, arr):
        # Code Here
    
        second = -1
        largest = arr[0]
        
        for i in range(len(arr)):
            
            if arr[i] > largest:
                second = largest
                largest = arr[i]
            elif(arr[i] < largest and arr[i] > second):
                second = arr[i]
        return second
