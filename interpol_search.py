def interpol_search(arr, target, low, hi):
    while( arr[low] != arr[hi] and (target >= arr[low]) and (target <= arr[hi]) ):
        pos = low + ( (target - arr[low])*(hi - low)//(arr[hi]-arr[low]) )
        #print(pos)
        if(arr[pos] == target):
            return pos
        elif( arr[pos] > target):
            hi = pos - 1
        else:
            low = pos + 1

def main():

    input_list = list(map(int,(input("Enter the numbers: ").split(' '))))
    print(input_list)

    x = int(input("Enter element to search: "))
    result = interpol_search(input_list, x, 0, len(input_list)-1)
    if result != -1:
        print("Element is at index {}".format(result))
    else:
        print("Element not in list")


main()
# Enter the numbers: 23 24 29 38 47 58 60 62 65 75 79 88 94 135
# [23, 24, 29, 38, 47, 58, 60, 62, 65, 75, 79, 88, 94, 135]
# Enter element to search: 94
# Element is at index 12