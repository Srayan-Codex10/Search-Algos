import binsearch as bin_s
def expo_search(arr, size, target):
    
    if(size == 0):
        print("Element not found")
        return -1
    
    bound = 1

    while( bound < size and arr[bound] < target ):
        bound *= 2
        #print("Searching for range in: ",bound)
    
    return bin_s.binsearch(arr, bound//2, min(bound, size - 1), target)


def main():
    arr = list(map(int,input("Enter numbers to search: ").split(' ')))
    print(arr , "Length of list: ",len(arr))
    target = int(input("Enter target element: "))

    result = expo_search(arr,len(arr),target)
    print("Element is at position {}".format(result))

if __name__ == "__main__":
    main()

# Enter numbers to search: 12 23 34 45 58 67 72 89 99 102 130 145 190 234 257
# [12, 23, 34, 45, 58, 67, 72, 89, 99, 102, 130, 145, 190, 234, 257] Length of list:  15
# Enter target element: 234
# Searching for range in:  2                #searching for subarray range where target is present
# Searching for range in:  4
# Searching for range in:  8
# Searching for range in:  16
# 11                                        #running binary search in subarray 2^(j-1) - 2^j
# 13
# Element is at position 13