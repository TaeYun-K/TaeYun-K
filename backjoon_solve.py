import sys

n = int(input())

xlist = []

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
    
def pop(arr):
    if arr.isempty:
        return -1
    else:
        arr.pop()


for i in range(n):
    cmd, x = sys.stdin.readline().split()
    if cmd == 'push':
        push(x,xlist)
        
    elif cmd == 'pop':
        pop(xlist)
        
    elif cmd == 'size':
        print(size(xlist))
        
    elif cmd == 'empty' :
        print(empty(xlist))
        
    elif cmd == 'top':
        print(top(xlist))
        
    print(xlist)

    




# for i in xlist:
#     for j in ylist:
#         if i > j :
#             cnt+=1
            
#     arr.append(cnt)
#     cnt = 0
    
# print(*arr)

        

