# First index

def recursion(a,e,i):
    length=len(a)
    if(i < length):
        if (a[i] == e):
            return i
        else:
            return recursion(a,e,i+1)
    else:
        return "Not Found"

if __name__ == "__main__":
    element=int(input())
    array=list(map(int,input().split())) 
    print(recursion(array,element,0))