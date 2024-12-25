  def findUnion(self,a,b):
        # code here 
        i = 0
        j = 0
        c = []
        while i < len(a) and j < len(b):
            
            if a[i] <= b[j]:
                if len(c) == 0 or c[-1] != a[i]:
                    c.append(a[i])
                i+=1
            else:
                if len(c) ==0 or c[-1] != b[j]:
                    c.append(b[j])
                j+=1
        
        while i < len(a):
            if c[-1] != a[i]:
                c.append(a[i])
            i+=1
        
        while j < len(b):
            if c[-1] != b[j]:
                c.append(b[j])
            j+=1
                    
        return c
