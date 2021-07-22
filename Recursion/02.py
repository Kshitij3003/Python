# Last index

def recursion(a,e,l,i):
    if(i < l):
        if (a[l] == e):
            return l
        else:
            return recursion(a,e,l-1,i)
    else:
        return "Not Found"

if __name__ == "__main__":
    element=int(input())
    array=list(map(int,input().split()))
    length=len(array) 
    print(recursion(array,element,length-1,0))