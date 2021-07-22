# Replace all occurance of "pi" with 3.14

def recursion(array,length,index,output):
    if (index < len(array)):
        string=array[index]
        output.append(string.replace("pi","3.14"))
        recursion(array,length,index+1,output)
    else:
        return array
    return output

if __name__ == "__main__":
    lines=int(input())
    array=[]
    for i in range(0,lines):
        array.append(input())
    value=recursion(array,lines,0,[])
    for i in value:
        print(i)
