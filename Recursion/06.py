# Rat Chase its cheese

def recursion(array,length,row,column,index,output):
    print(array)
    print(length,row,index,output)
    if (row < length):
        value_01=array[row]
        recursion1(value_01,index,column,output)
    return output
    pass

def recursion1(value,index,column,output):
    if (index < column):
        if(value[index] == '0'):
            output.append('1')
            return recursion1(value,index+1,column,output)
        elif(value[index] == 'x'):
            exit

if __name__ == "__main__":
    column,row=map(int,input().split())
    array=[]
    for i in range(0,column):
        array.append(list(map(str,input())))
    print(recursion(array,len(array),0,column,0,output=[]))
