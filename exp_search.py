import binsearch as bin_s
def expo_search(arr, size, target):
    
    if(size == 0):
        print("Element not found")
        return -1
    
    bound = 1

    while( bound < size and arr[bound] < target ):
        bound *= 2
        print("Searching for range in: ",bound)
    
    return bin_s.binsearch(arr, bound//2, min(bound, size - 1), target)


def main():
    arr = list(map(int,input("Enter numbers to search: ").split(' ')))
    print(arr , "Length of list: ",len(arr))
    target = int(input("Enter target element: "))

    result = expo_search(arr,len(arr),target)
    print("Element is at position {}".format(result))

if __name__ == "__main__":
    main()

