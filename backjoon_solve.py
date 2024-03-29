import sys

n = int(input())

for i in range(n):
    cmd, x = sys.stdin.readline().split()
    print(cmd,x)
    

def push(n,arr) :
    arr.append(n)
    
def top(arr):
    return arr[len(arr)-1]
    
def size(arr):
    return len(arr)

def empty(arr):
    if arr.isempty :
        return 1
    
    else:
        return 0
    



# for i in xlist:
#     for j in ylist:
#         if i > j :
#             cnt+=1
            
#     arr.append(cnt)
#     cnt = 0
    
# print(*arr)

        

