# Convert string to integer without using any built-in modules

def recursion(number,length,index,output):
    dictionary={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    if (index < length):
        output=output*10+dictionary[number[index]]
        return recursion(number,length,index+1,output)
    return output

if __name__ == "__main__":
    number="123"
    # output=0
    print(recursion(number,len(number),0,0))