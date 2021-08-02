import os

def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(size)]
    # print("Data:",data)
    items = list(range(size))
    # print("Items:",items)
    items = items[:-1]+items[::-1]
    # print("ITEMS:",items)
    for i in items:
        temp = data[-(i+1):]
        print("TEMP:",temp)
        row = temp[::-1]+temp[1:]
        # print("ROW:",row)
        print("-".join(row))
        print("-".join(row).center(n*4-3, "-"))

if __name__ == '__main__':
    os.system('cls')
    n = int(input())
    array=list(range(n))
    print(array[:-1])
    print(array[::-1])
    print_rangoli(n)