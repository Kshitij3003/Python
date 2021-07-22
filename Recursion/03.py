# All indices

def recursion(a,e,i,i_a):
    length=len(a)
    if(i < length):
        if (a[i] == e):
            i_a.append(i)
            recursion(a,e,i+1,i_a)
        else:
            recursion(a,e,i+1,i_a)
    else:
        return "Not Found"
    return i_a

if __name__ == "__main__":
    array=list(map(int,input().split()))
    element=int(input())
    value=recursion(array,element,0,[])
    print(value)