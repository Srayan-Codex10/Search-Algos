from math import sqrt,floor
def jumpsearch(arr, key, size):
    block = floor(sqrt(size))
    k = 0
    while(arr[min(block, size) - 1] < key):
        k = block
        block += floor(sqrt(size))
        if (k >= size):
            print('no such element')
            return -1

    #print(k,block)
    while(k < block):
        if(arr[k] == key):
            print("Element {} found at position {}".format(x[k],k))
            return k
        k += 1
    
    print("no such element")
    return -1

x = list(range(1,25))
print(x)
key = int(input("Enter element to search: "))

target_index = jumpsearch(x,key,len(x))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Enter element to search: 9
# 6 9
# Element 9 found at position 8

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# Enter element to search: 15
# Element 15 found at position 14