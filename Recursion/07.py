def recursion(value,array,index,length,count,rec):
    rec+=1
    print("Recursion Block:-",rec)
    if index < length:
        if value % array[index] == 0:
            count+=1
            recursion(value,array,index+1,length,count,rec)
        else:
            recursion(value,array,index+1,length,count,rec)
    return count

def friends(array,friendly,count):
    array.sort()
    length=len(array)
    for i in array:
        index,count=0,0
        value=recursion(i,array,index,length,count,0)
        print(value)
        friendly.append(value)
    return friendly


if __name__ == "__main__":
    print(friends([2,3,4,7,6],[],count=0))